#!/data/data/com.termux/files/usr/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SAMPLE_ROOT="$ROOT_DIR/data/sample/Blagopoluchie"

echo "Preparing sample data in: $SAMPLE_ROOT"

rm -rf "$SAMPLE_ROOT"

mkdir -p "$SAMPLE_ROOT/00_INBOX/test-chat-package"
mkdir -p "$SAMPLE_ROOT/01_CORE"
mkdir -p "$SAMPLE_ROOT/03_LAB"
mkdir -p "$SAMPLE_ROOT/09_ADMIN"

cat > "$SAMPLE_ROOT/00_INBOX/test-chat-package/README-chat-folder.md" <<'EOF'
# Тестовый пакет чата

Статус: тест
Назначение: учебный пакет для проверки Архивариуса
EOF

cat > "$SAMPLE_ROOT/00_INBOX/test-chat-package/.wb-copy-map.tsv" <<'EOF'
1010-0904-2026-test-note.md	03_LAB
EOF

cat > "$SAMPLE_ROOT/00_INBOX/test-chat-package/chat-card.md" <<'EOF'
# Карточка чата

Тема: test_archivist
Статус: active
EOF

cat > "$SAMPLE_ROOT/00_INBOX/test-chat-package/1010-0904-2026-test-note.md" <<'EOF'
# Тестовая заметка

Архивариус должен уметь находить этот файл по имени и по тексту.

Ключевые слова:
- архивариус
- тест
- пакет чата
EOF

cat > "$SAMPLE_ROOT/01_CORE/0900-0904-2026-core-concept.md" <<'EOF'
# Ядро проекта

Это файл из ядра проекта Благополучие.
Он нужен для проверки проектного контура 01_CORE.
EOF

cat > "$SAMPLE_ROOT/03_LAB/0910-0904-2026-lab-experiment.md" <<'EOF'
# Лабораторный эксперимент

Проверка индексации markdown-файлов и поиска по содержимому.
EOF

cat > "$SAMPLE_ROOT/09_ADMIN/0920-0904-2026-admin-note.md" <<'EOF'
# Административная заметка

Нужна для проверки контура 09_ADMIN и базового поиска.
EOF

echo "Sample data prepared."
find "$SAMPLE_ROOT" -type f | sort
