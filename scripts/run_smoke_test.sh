#!/data/data/com.termux/files/usr/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
CONFIG_PATH="$ROOT_DIR/config/default_config.json"

echo "== Step 1: build sample data =="
bash "$ROOT_DIR/scripts/make_sample_data.sh"

echo
echo "== Step 2: init database =="
python "$ROOT_DIR/archivist.py" --config "$CONFIG_PATH" init-db

echo
echo "== Step 3: run index =="
python "$ROOT_DIR/archivist.py" --config "$CONFIG_PATH" index

echo
echo "== Step 4: show stats =="
python "$ROOT_DIR/archivist.py" --config "$CONFIG_PATH" stats

echo
echo "== Step 5: search by name =="
python "$ROOT_DIR/archivist.py" --config "$CONFIG_PATH" search-name "test"

echo
echo "== Step 6: search by text =="
python "$ROOT_DIR/archivist.py" --config "$CONFIG_PATH" search-text "архивариус"

echo
echo "== Smoke test completed successfully =="
