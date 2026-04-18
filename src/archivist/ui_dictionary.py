from __future__ import annotations
from pathlib import Path
import html
import json
import re

LABEL_ALIASES = {
    "Layer": "layer",
    "Protected class": "protected class",
    "Safe next step": "safe next step",
    "Short summary": "short summary",
    "Why protected": "why protected",
    "Why selected": "why selected",
    "Manifest-related": "manifest_related",
    "Long-form priority": "long_form_priority",
    "Review package": "review package",
    "Overview": "overview",
    "Shortlist": "shortlist",
    "Group summary": "group summary",
    "Cards": "cards",
    "Compare": "compare",
    "Source of truth": "source of truth",
    "Runtime/service": "runtime/service",
    "Operator working layout": "operator working layout",
    "Logical canonical layout": "logical canonical layout",
}

VALUE_ALIASES = {
    "repo-mirror": "repo-mirror",
    "shared-canon": "shared-canon",
    "system-archive": "system-archive",
    "entity-homes": "entity-homes",
    "entity-sources": "entity-sources",
    "entity-exchange": "entity-exchange",
    "legacy/source long-form field": "legacy/source long-form field",
    "runtime/service": "runtime/service",
    "operator-working": "operator-working",
    "runtime-protected": "runtime-protected",
    "canonical-protected": "canonical-protected",
    "legacy-source-only": "legacy-source-only",
    "requires-separate-route-decision": "requires-separate-route-decision",
    "archive-only-candidate": "archive-only-candidate",
    "review-object": "review-object",
    "keep-as-trace": "keep-as-trace",
}

def load_ui_dict(path: str | Path) -> dict:
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8"))

def _replace_strong_label(text: str, eng: str, ru: str, hint: str) -> str:
    title_attr = f' title="{html.escape(hint, quote=True)}"' if hint else ""
    pattern = re.compile(rf"<strong>\s*{re.escape(eng)}\s*:?\s*</strong>", re.IGNORECASE)
    return pattern.sub(f"<strong{title_attr}>{ru}:</strong>", text)

def _replace_tag_text(text: str, eng: str, ru: str) -> str:
    text = re.sub(rf">(\s*){re.escape(eng)}(\s*)<", f">{ru}<", text)
    text = re.sub(rf">(\s*){re.escape(eng)}:(\s*)<", f">{ru}:<", text)
    return text

def apply_html_dictionary(html_text: str, ui_dict: dict) -> str:
    if "<!-- ru-ui-dict-applied -->" in html_text:
        return html_text

    labels = ui_dict.get("labels", {})
    values = ui_dict.get("values", {})
    hints = ui_dict.get("hints", {})

    for eng, key in LABEL_ALIASES.items():
        ru = labels.get(key)
        if not ru:
            continue
        hint = hints.get(key, "")
        html_text = _replace_strong_label(html_text, eng, ru, hint)
        html_text = _replace_tag_text(html_text, eng, ru)

    for eng, key in VALUE_ALIASES.items():
        ru = values.get(key)
        if not ru:
            continue
        html_text = _replace_tag_text(html_text, eng, ru)

    marker = "<!-- ru-ui-dict-applied -->\n"
    return marker + html_text

def apply_html_dictionary_tree(root: str | Path, dict_path: str | Path) -> dict:
    root = Path(root)
    ui_dict = load_ui_dict(dict_path)
    changed = 0
    scanned = 0
    changed_files = []
    for p in sorted(root.rglob("*.html")):
        scanned += 1
        original = p.read_text(encoding="utf-8")
        updated = apply_html_dictionary(original, ui_dict)
        if updated != original:
            p.write_text(updated, encoding="utf-8")
            changed += 1
            changed_files.append(str(p))
    return {"scanned": scanned, "changed": changed, "changed_files": changed_files}
