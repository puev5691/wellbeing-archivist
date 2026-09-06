# Recovery manifest: КАНЦЕЛЯР

## Назначение

Минимальный проверяемый пакет восстановления для запуска нового чата КАНЦЕЛЯР.

## Внешний locator

    store: github
    repository: puev5691/wellbeing-archivist
    path: docs/entities/kancelyariya/recovery-current
    ref: main
    manifest: KAN__recovery-manifest__KAN.md
    checksums: sha256sums.txt

## Файлы пакета

- `KAN__snapshot__KAN.md` — текущее состояние и подтверждённые хвосты;
- `KAN__initiation-current__KAN.md` — роль, ограничения и порядок запуска;
- `KAN__recovery-manifest__KAN.md` — этот манифест;
- `sha256sums.txt` — контрольные суммы пакета.

## Обязательные project-level источники

После фактической миграции активного набора:

- `project-instructions-core-v2-approved.md`;
- `file-work-canon-universal-v2_2-approved.md`;
- `entity-roles-short-v2-approved.md`;
- `source-loading-policy-v2-approved.md`;
- `blagopoluchie-concept-core-v02-approved.md`;
- `entity-state-preservation-and-recovery-canon-v1_2-approved.md`.

## Порядок восстановления

1. Прочитать обязательные управляющие источники.
2. Прочитать initiation, snapshot и этот manifest.
3. Открыть внешний locator.
4. Проверить наличие фактического состава пакета.
5. Сопоставить контрольные суммы с `sha256sums.txt`.
6. Зафиксировать `initiation_verified`, `initiation_loaded_external_unverified` или `initiation_failed`.
7. Только после `initiation_verified` считать внешнее recovery полностью подтверждённым.
8. Не продолжать автоматически старые исследования; ждать конкретной задачи.

## Статус

Пакет приведён к утверждённому recovery-канону v1.2.

---

document_type: recovery-manifest  
entity: КАНЦЕЛЯР  
status: current  
recovery_canon: v1.2 approved  
project_time: generated_without_trusted_project_time
