from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ClassifiedPackageFile:
    filename: str
    file_type: str
    reason: str


def read_file_header(path: Path, max_chars: int = 1200) -> str:
    try:
        return path.read_text(encoding="utf-8")[:max_chars].lower()
    except Exception:
        return ""


def classify_file(path: str | Path) -> ClassifiedPackageFile:
    file_path = Path(path).expanduser().resolve()
    name = file_path.name
    lower_name = name.lower()
    suffix = file_path.suffix.lower()

    if name == "README-chat-folder.md":
        return ClassifiedPackageFile(name, "readme", "special package readme filename")

    if name == ".wb-copy-map.tsv":
        return ClassifiedPackageFile(name, "copy_map", "special copy map filename")

    if name == ".wb-copy-map.generated.tsv":
        return ClassifiedPackageFile(name, "copy_map_generated", "generated copy map filename")

    if name == "chat-card.md":
        return ClassifiedPackageFile(name, "chat_card", "special chat card filename")

    if suffix == ".sh":
        return ClassifiedPackageFile(name, "script", "shell script extension")

    if lower_name == "other.txt":
        return ClassifiedPackageFile(name, "scratch", "generic scratch or recovery text filename")

    if any(token in lower_name for token in ("scene", "story", "synopsis", "literary", "media")):
        return ClassifiedPackageFile(name, "literary", "matched literary keywords in filename")

    if any(token in lower_name for token in ("technical-specification", "entity-model", "mvp-plan", "sqlite-schema", "python-code-draft", "code-structure")):
        return ClassifiedPackageFile(name, "engineering", "matched engineering keywords in filename")

    if any(token in lower_name for token in ("log", "journal", "summary", "instruction", "regulation", "plan")):
        return ClassifiedPackageFile(name, "log", "matched log or regulation keywords in filename")

    header = read_file_header(file_path)

    if "сцена " in header or "синопсис" in header or "литератур" in header:
        return ClassifiedPackageFile(name, "literary", "matched literary keywords in file header")

    if "техническое задание" in header or "mvp" in header or "sqlite" in header or "проектный документ" in header:
        return ClassifiedPackageFile(name, "engineering", "matched engineering keywords in file header")

    if "журнал" in header or "журналная запись" in header:
        return ClassifiedPackageFile(name, "log", "matched journal keywords in file header")

    if suffix in {".md", ".txt", ".tsv", ".json", ".yaml", ".yml", ".csv", ".log"}:
        return ClassifiedPackageFile(name, "unknown", "known text extension but no stronger classification")

    return ClassifiedPackageFile(name, "unknown", "no classification rule matched")


def classify_package_files(package_path: str | Path) -> list[ClassifiedPackageFile]:
    package_dir = Path(package_path).expanduser().resolve()
    if not package_dir.exists() or not package_dir.is_dir():
        raise FileNotFoundError(f"Chat package directory not found: {package_dir}")

    results: list[ClassifiedPackageFile] = []

    for path in sorted(package_dir.iterdir(), key=lambda p: p.name.lower()):
        if not path.is_file():
            continue
        results.append(classify_file(path))

    return results
