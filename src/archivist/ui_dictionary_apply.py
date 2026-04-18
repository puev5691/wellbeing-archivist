from __future__ import annotations
from pathlib import Path
from .ui_dictionary import apply_html_dictionary_tree

def run(root: str | Path, dict_path: str | Path) -> dict:
    return apply_html_dictionary_tree(root, dict_path)
