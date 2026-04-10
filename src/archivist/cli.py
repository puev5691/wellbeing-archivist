from __future__ import annotations
import argparse
from pathlib import Path

from .classify_files import classify_package_files
from .config import load_config
from .copy_map import parse_copy_map
from .copy_map_candidate import build_copy_map_candidate, render_copy_map_candidate
from .copy_map_coverage import build_copy_map_coverage_report
from .copy_map_recommendations import build_copy_map_recommendations, render_copy_map_recommendations
from .db import Database
from .draft_copy_map import collect_draft_copy_map_entries, render_draft_copy_map
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

    generate_copy_map_draft = subparsers.add_parser(
        "generate-copy-map-draft",
        help="Generate draft .wb-copy-map for a chat package by package ID",
    )
    generate_copy_map_draft.add_argument("package_id", type=int)
    generate_copy_map_draft.add_argument(
        "--write",
        action="store_true",
        help="Write draft to .wb-copy-map.generated.tsv inside the package",
    )

    classify_package = subparsers.add_parser(
        "classify-package-files",
        help="Classify files inside a chat package by package ID",
    )
    classify_package.add_argument("package_id", type=int)

    check_copy_map_coverage = subparsers.add_parser(
        "check-copy-map-coverage",
        help="Check how well .wb-copy-map.tsv covers the files of a chat package",
    )
    check_copy_map_coverage.add_argument("package_id", type=int)

    recommend_copy_map = subparsers.add_parser(
        "recommend-copy-map-additions",
        help="Recommend new lines to add into .wb-copy-map.tsv for uncovered files",
    )
    recommend_copy_map.add_argument("package_id", type=int)

    build_copy_map_candidate_cmd = subparsers.add_parser(
        "build-copy-map-candidate",
        help="Build merged candidate copy map from existing map and recommendations",
    )
    build_copy_map_candidate_cmd.add_argument("package_id", type=int)
    build_copy_map_candidate_cmd.add_argument(
        "--write",
        action="store_true",
        help="Write merged candidate to .wb-copy-map.candidate.tsv inside the package",
    )

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
    if args.command == "generate-copy-map-draft":
        return cmd_generate_copy_map_draft(args)
    if args.command == "classify-package-files":
        return cmd_classify_package_files(args)
    if args.command == "check-copy-map-coverage":
        return cmd_check_copy_map_coverage(args)
    if args.command == "recommend-copy-map-additions":
        return cmd_recommend_copy_map_additions(args)
    if args.command == "build-copy-map-candidate":
        return cmd_build_copy_map_candidate(args)

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


def cmd_generate_copy_map_draft(args) -> int:
    db = _db_from_args(args)
    package = db.get_chat_package_by_id(args.package_id)
    if package is None:
        print("Chat package not found.")
        return 1

    package_path = package.get("package_path")
    if not package_path:
        print("Package path is not set.")
        return 1

    entries = collect_draft_copy_map_entries(package_path)
    draft_text = render_draft_copy_map(entries)

    print(f"Draft copy map for package: {package.get('package_name')}")
    print(f"  package_path: {package_path}")
    print()

    if args.write:
        output_path = Path(package_path) / ".wb-copy-map.generated.tsv"
        output_path.write_text(draft_text, encoding="utf-8")
        print(f"Draft written to: {output_path}")
        print()

    print(draft_text, end="")
    return 0


def cmd_classify_package_files(args) -> int:
    db = _db_from_args(args)
    package = db.get_chat_package_by_id(args.package_id)
    if package is None:
        print("Chat package not found.")
        return 1

    package_path = package.get("package_path")
    if not package_path:
        print("Package path is not set.")
        return 1

    classified = classify_package_files(package_path)

    print(f"Package file classification: {package.get('package_name')}")
    print(f"  package_path: {package_path}")
    print()

    for idx, item in enumerate(classified, start=1):
        print(f"[{idx}] {item.filename}")
        print(f"  file_type: {item.file_type}")
        print(f"  reason: {item.reason}")

    return 0


def cmd_check_copy_map_coverage(args) -> int:
    db = _db_from_args(args)
    package = db.get_chat_package_by_id(args.package_id)
    if package is None:
        print("Chat package not found.")
        return 1

    package_path = package.get("package_path")
    copy_map_path = package.get("copy_map_file_path")

    if not package_path:
        print("Package path is not set.")
        return 1

    if not copy_map_path:
        print("Copy map is not set for this chat package.")
        return 1

    report = build_copy_map_coverage_report(package_path, copy_map_path)

    print(f"Copy map coverage for package: {package.get('package_name')}")
    print(f"  package_path: {report.package_path}")
    print(f"  copy_map_path: {report.copy_map_path}")
    print()
    print(f"  covered_files: {len(report.covered_files)}")
    print(f"  uncovered_files: {len(report.uncovered_files)}")
    print(f"  missing_from_package: {len(report.missing_from_package)}")
    print(f"  ignored_files: {len(report.ignored_files)}")
    print()

    if report.covered_files:
        print("Covered files:")
        for name in report.covered_files:
            print(f"  - {name}")
        print()

    if report.uncovered_files:
        print("Uncovered files:")
        for name in report.uncovered_files:
            print(f"  - {name}")
        print()

    if report.missing_from_package:
        print("Missing from package but referenced by copy map:")
        for name in report.missing_from_package:
            print(f"  - {name}")
        print()

    if report.ignored_files:
        print("Ignored files:")
        for name in report.ignored_files:
            print(f"  - {name}")
        print()

    return 0


def cmd_recommend_copy_map_additions(args) -> int:
    db = _db_from_args(args)
    package = db.get_chat_package_by_id(args.package_id)
    if package is None:
        print("Chat package not found.")
        return 1

    package_path = package.get("package_path")
    copy_map_path = package.get("copy_map_file_path")

    if not package_path:
        print("Package path is not set.")
        return 1

    if not copy_map_path:
        print("Copy map is not set for this chat package.")
        return 1

    recommendations = build_copy_map_recommendations(package_path, copy_map_path)

    print(f"Recommended copy map additions for package: {package.get('package_name')}")
    print(f"  package_path: {package_path}")
    print(f"  copy_map_path: {copy_map_path}")
    print()

    if not recommendations:
        print("No uncovered files to recommend.")
        return 0

    for idx, item in enumerate(recommendations, start=1):
        print(f"[{idx}] {item.source_filename}")
        print(f"  file_type: {item.file_type}")
        print(f"  suggested_target_relative_directory: {item.suggested_target_relative_directory}")
        print(f"  reason: {item.reason}")
        print()

    print("Suggested lines to append:")
    print(render_copy_map_recommendations(recommendations), end="")
    return 0


def cmd_build_copy_map_candidate(args) -> int:
    db = _db_from_args(args)
    package = db.get_chat_package_by_id(args.package_id)
    if package is None:
        print("Chat package not found.")
        return 1

    package_path = package.get("package_path")
    copy_map_path = package.get("copy_map_file_path")

    if not package_path:
        print("Package path is not set.")
        return 1

    if not copy_map_path:
        print("Copy map is not set for this chat package.")
        return 1

    candidate_entries = build_copy_map_candidate(package_path, copy_map_path)
    candidate_text = render_copy_map_candidate(candidate_entries)

    print(f"Copy map candidate for package: {package.get('package_name')}")
    print(f"  package_path: {package_path}")
    print(f"  source_copy_map_path: {copy_map_path}")
    print()

    if args.write:
        output_path = Path(package_path) / ".wb-copy-map.candidate.tsv"
        output_path.write_text(candidate_text, encoding="utf-8")
        print(f"Candidate written to: {output_path}")
        print()

    print(candidate_text, end="")
    return 0
