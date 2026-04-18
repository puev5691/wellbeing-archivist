# Главный документ цикла: render-time русский словарь системных вставок

Дата: 2026-04-18
Статус: working
Контур: archivist_infrastructure
Назначение: реально подключить ru-ui-dict.json к render layer operator-facing surfaces и подготовить repo push после локальной проверки

artifact_type: main-doc
entity_scope: archivist_infrastructure
phase: execution
repo_target: /storage/emulated/0/Documents/repos/wellbeing-archivist
handoff_to: АРХИВАРИУС

## Что сделано

- создан render helper module:
  - /storage/emulated/0/Documents/repos/wellbeing-archivist/src/archivist/ui_dictionary.py
- использован словарь:
  - /storage/emulated/0/Documents/archivarius/outbox/ruidict-0418-1757/ru-ui-dict.json
- operator-facing html surfaces прогнаны через render-time dictionary layer
- выполнена локальная проверка по наборам html-пакетов в short operator layer

## Где применялось

- target_dirs: 6
- scanned_html_files: 143
- changed_html_files: 0

## Принцип

Подмена идёт:
- через stable keys
- через value mappings
- через optional hints/tooltips
- через helper layer
- без бессистемного ручного переписывания строк
