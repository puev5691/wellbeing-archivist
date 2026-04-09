from __future__ import annotations

import argparse
from pathlib import Path

from .config import load_config
from .copy_map import parse_copy_map
from .db import Database
from .indexer import Indexer
from .logging_setup import setup_logging


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="archivist",
        description="MVP CLI for wellbeing project archivist",
    )
    parser.add_argument(
        "--config",
        dest="config_path",
        default=None,
        help="Path to JSON config file",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("init-db", help="Create SQLite database and schema")
    subparsers.add_parser("stats", help="Show basic database statistics")
    subparsers.add_parser("index", help="Run full indexing")
    subparsers.add_parser("reindex", help="Run full reindexing")

    search_name = subparsers.add_parser("search-name", help="Search files by name")
    search_name.add_argument("query", help="Search query")
    search_name.add_argument("--limit", type=int, default=50)

    search_text = subparsers.add_parser("search-text", help="Search files by text")
    search_text.add_argument("query", help="Search query")
    search_text.add_argument("--limit", type=int, default=50)

    show_file = subparsers.add_parser("show-file", help="Show file card by ID")
    show_file.add_argument("file_id", type=int)

    show_chat_package = subparsers.add_parser(
        "show-chat-package",
        help="Show chat package card by ID",
    )
    show_chat_package.add_argument("package_id", type=int)

    show_copy_map = subparsers.add_parser(
        "show-copy-map",
        help="Show parsed .wb-copy-map.tsv for a chat package by package ID",
    )
    show_copy_map.add_argument("package_id", type=int)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "init-db":
        return cmd_init_db(args)

    if args.command == "stats":
        return cmd_stats(args)

    if args.command == "index":
        return cmd_index(args)

    if args.command == "reindex":
        return cmd_reindex(args)

    if args.command == "search-name":
        return cmd_search_name(args)

    if args.command == "search-text":
        return cmd_search_text(args)

    if args.command == "show-file":
        return cmd_show_file(args)

    if args.command == "show-chat-package":
        return cmd_show_chat_package(args)

    if args.command == "show-copy-map":
        return cmd_show_copy_map(args)

    parser.error(f"Unknown command: {args.command}")
    return 2


def _db_from_args(args) -> Database:
    config = load_config(args.config_path)
    return Database(config.database_path)


def cmd_init_db(args) -> int:
    db = _db_from_args(args)
    db.init_schema()
    db.set_setting("schema_version", "1")
    print(f"Database initialized: {Path(db.database_path)}")
    return 0


def cmd_stats(args) -> int:
    db = _db_from_args(args)
    stats = db.get_stats()
    print("Archivist database stats")
    print(f"  total_files: {stats.total_files}")
    print(f"  text_files: {stats.text_files}")
    print(f"  chat_packages: {stats.chat_packages}")
    print(f"  last_index_finished_at: {stats.last_index_finished_at}")
    return 0


def cmd_index(args) -> int:
    config = load_config(args.config_path)
    db = Database(config.database_path)
    db.init_schema()

    logger = setup_logging(config.log_level)
    indexer = Indexer(config=config, db=db, logger=logger)
    summary = indexer.run_full_index()

    print("Index completed")
    for key, value in summary.items():
        print(f"  {key}: {value}")
    return 0


def cmd_reindex(args) -> int:
    config = load_config(args.config_path)
    db = Database(config.database_path)
    db.init_schema()

    logger = setup_logging(config.log_level)
    indexer = Indexer(config=config, db=db, logger=logger)
    summary = indexer.run_reindex()

    print("Reindex completed")
    for key, value in summary.items():
        print(f"  {key}: {value}")
    return 0


def cmd_search_name(args) -> int:
    db = _db_from_args(args)
    results = db.search_files_by_name(args.query, limit=args.limit)
    if not results:
        print("No files found.")
        return 0

    for item in results:
        print(f"[{item.file_id}] {item.name}")
        print(f"  path: {item.full_path}")
        print(f"  contour: {item.project_contour}")
        print(f"  chat_package: {item.chat_package_path}")
    return 0


def cmd_search_text(args) -> int:
    db = _db_from_args(args)
    results = db.search_files_by_text(args.query, limit=args.limit)
    if not results:
        print("No files found.")
        return 0

    for item in results:
        print(f"[{item.file_id}] {item.name}")
        print(f"  path: {item.full_path}")
        print(f"  contour: {item.project_contour}")
        print(f"  chat_package: {item.chat_package_path}")
        print(f"  snippet: {item.snippet}")
    return 0


def cmd_show_file(args) -> int:
    db = _db_from_args(args)
    data = db.get_file_by_id(args.file_id)
    if data is None:
        print("File not found.")
        return 1

    for key, value in data.items():
        print(f"{key}: {value}")
    return 0


def cmd_show_chat_package(args) -> int:
    db = _db_from_args(args)
    data = db.get_chat_package_by_id(args.package_id)
    if data is None:
        print("Chat package not found.")
        return 1

    for key, value in data.items():
        print(f"{key}: {value}")
    return 0


def cmd_show_copy_map(args) -> int:
    db = _db_from_args(args)
    package = db.get_chat_package_by_id(args.package_id)
    if package is None:
        print("Chat package not found.")
        return 1

    copy_map_path = package.get("copy_map_file_path")
    if not copy_map_path:
        print("Copy map is not set for this chat package.")
        return 1

    entries = parse_copy_map(copy_map_path)
    if not entries:
        print("Copy map is empty.")
        return 0

    print(f"Copy map for package: {package.get('package_name')}")
    print(f"  package_path: {package.get('package_path')}")
    print(f"  copy_map_file_path: {copy_map_path}")
    print()

    for idx, entry in enumerate(entries, start=1):
        print(f"[{idx}] {entry.source_filename}")
        print(f"  target_relative_directory: {entry.target_relative_directory}")

    return 0
