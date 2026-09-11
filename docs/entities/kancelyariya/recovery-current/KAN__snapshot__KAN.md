# Self-snapshot Сущности КАНЦЕЛЯР

## Назначение

Этот snapshot фиксирует current-state KAN после bounded acceptance двух значимых результатов КАНЦЕЛЯРА и обработки входящих решений KOO.

Источник истины:
- current approved Project Sources;
- проверяемые GitHub locator/version identities;
- явные KOO/ARH решения;
- подтверждённые tool results текущего прохода.

## confirmed/current

### 1. Active Project Sources

Current approved set остаётся:

- `project-instructions-core-v2_1-approved.md`
  - SHA-256: `8a86945c28e361b5adf7ecc96326a1591a193118ce7be258a9c0a21ddd2ace26`
- `entity-roles-short-v2_2-approved.md`
  - SHA-256: `c8103b1c2dc6c3f4b489f118e9bcf4053add6bea384427f23dad5dddced2ae3d`
- `file-work-canon-universal-v2_3-approved.md`
  - SHA-256: `5ec75e480c0b78a72bb2faa702a21064b32bd3b919b225b1ae25a30dd0a700e5`
- `entity-state-preservation-and-recovery-canon-v1_4-approved.md`
  - SHA-256: `984871a22aab1910fc4ab3217c16488eac1e472734bdfd1948fd57c213566fda`
- `source-loading-policy-v2-approved.md`
  - SHA-256: `2661a3a266547a5e0f6b70c3dab8a02add2bb788b4a90b1136b7e9445b2d6061`

Source barrier для этой линии ранее пройден; новых Project Sources текущим checkpoint не создаётся.

### 2. Current role

KAN отвечает за границы понятий, ответственности и внешних обязательств; различает факт, определение, гипотезу, нормативное предложение и обещание; готовит bounded policy/disclaimer/regulation. Не заменяет профильного юриста.

### 3. GitHub information-entry Stage A — KAN gate закрыт в bounded границе

KAN artifact:

`entities/kancelar/outbox/KAN__github-info-entry-public-legal-boundary__KOO.md`

- commit: `6545a413dab7cc29e1d8485176402f24c23367f9`
- blob: `e071667b6b124060a49b9c86f653b7703ad3f9af`
- SHA-256 локального идентичного результата: `85e92602e128c6829e67eff701a696fe1252a8a39ea67bc46bdeac98431155d7`

KOO decision:

`entities/koordinator/outbox/KOO__github-info-entry-kan-decision__KAN.md`

- commit: `c1a0b52e44559678ec299cc8dbcdcd0ac7961e16`
- blob: `988b6a34cd046f56e305aceed0e46cebcdb8cdbf`
- decision: `ACCEPTED_BOUNDED_STAGE_A_WORKING_RESULT`

KAN прочитал decision по immutable commit и создал receipt:

`routes/receipts/KOO__github-info-entry-kan-decision__KAN.receipt.md`

- receipt commit: `6d3f037b69bb901138acabee8f0d9891ddab7eff`
- receipt blob: `ea9ee8b01bd9540c57594a6e83dde6a5a9c0d204`

Принятая граница:
- public visibility не создаёт разрешение на reuse;
- semantic status/provenance сохраняются;
- `allowed / allowed-with-conditions / blocked / unknown` допустимы как bounded Stage A outcomes;
- secrets и sensitive personal data blocked;
- candidate/draft/research не представляются как approved/current;
- third-party material без rights basis не зеркалируется;
- fundraising/donation/payment и WBN/WBNP financial/investment claims остаются за отдельным authority/review;
- KAN legal boundary не заменяет RED editorial readiness и SIS infrastructure/security review.

Новые Project Sources, production publication, settings change и authority expansion этим acceptance не создаются.

### 4. Speech legal-semantic map — bounded acceptance подтверждён

KAN artifact:

`entities/kancelar/outbox/KAN__speech-legal-semantic-map__KOO.md`

- commit: `649780fb0eef8e6bf441dcd7986def6f364ad727`
- blob: `dda9215c1084e003edd0064322db3377e9174cde`

KOO decision:

`entities/koordinator/outbox/KOO__speech-legal-semantic-map-decision__KAN.md`

- commit: `8e7088c3c94e668c961d1e666bcc05cc9435029b`
- blob: `463251c060df52f19bdfd2bb2effe5a6fa5a00e6`
- decision: `ACCEPTED_AS_BOUNDED_SPEECH_GUIDANCE`

KAN receipt:

`routes/receipts/KOO__speech-legal-semantic-map-decision__KAN.receipt.md`

- commit: `b5d4fc04428ff958c5d54e062054044e8da4e5d5`
- blob: `77613df71054f540ce1c0ff2468f6e9f06c26464`

Acceptance:
- не превращает map в Project Source;
- не является legal approval конкретного публичного текста;
- не создаёт нового speech drafting task;
- используется как bounded semantic/legal constraint при будущей редакторской работе.

### 5. Speech claims boundary ARH

`KAN__speech-claims-boundary__ARH.md` ранее доставлен АРХИВАРИУСУ и интегрирован им в speech source-pack. Это подтверждает downstream use результата, но snapshot не подменяет этим отдельный formal acceptance, если он не зафиксирован как таковой.

### 6. Preservation предыдущего recovery package

Recovery commit:

`97d12b996f3a68cf757d7d2aa4389f4310dca6ed`

АРХИВАРИУС независимо проверил package и зафиксировал:

- `archive_preservation_state: accepted_structurally`
- `immutable_readback_state: verified_by_arh`
- `checksum_table_state: consistent_verified_by_arh`
- `bytewise_sha256_recompute_state: not_performed`
- `recoverability_state: practical_initiation_test_required_for_full_verification`

ARH check artifact:

`entities/archivarius/outbox/ARH__KAN-preservation-check__KAN.md`

KAN receipt этого решения:

`routes/receipts/ARH__KAN-preservation-check__KAN.receipt.md`

- receipt commit: `c0f98bc03552500da17ee8a2311e1b700278321f`

### 7. Automation-state

Текущий инструментальный preflight показал, что прежняя модель «один общий watch» больше не является текущим account-level состоянием: активны отдельные рабочие автоматизации нескольких Сущностей, а KAN watch выключен.

Это **не включается как долговременная норма**. Новый экземпляр обязан повторно проверять automation-state, потому что оно изменчиво.

## open / pending

### 1. Practical recovery test

Full `recoverability_verified` не заявляется до controlled cold-start нового KAN instance или эквивалентной проверки по current recovery package.

### 2. COOP concept/claim map

Локально существует:

`KAN__COOP-concept-claim-map__KOO.md`

SHA-256:

`155eba12a68aeed76f07df50a527d0494148e17e3d44de496f776a4e374844a5`

Внешняя публикация/delivery этого файла в `wellbeing-hq` текущим checkpoint не подтверждена.

Статус:

`local_significant_artifact / external_delivery_not_verified`

Не считать доставленным без actual outbox + dispatch + recipient route.

### 3. Legacy KAN recovery path

Current locator остаётся:

`puev5691/wellbeing-archivist/docs/entities/kancelyariya/recovery-current`

Миграция path отдельно не утверждена.

## parked / not revalidated

- Obsidian/graph pilot: `parked / not_revalidated_after_source_change`
- старые исследовательские темы прежних snapshot: `historical_reference / current_relevance_not_checked`

## unknown / not checked

- другие verified KAN instances: `unknown_not_checked`
- внешний writer-registry KAN: `not_checked`
- practical cold-start после этого checkpoint: `not_performed`
- будущий automation-state: `must_reverify`

## Опыт

### Опыт 1: bounded acceptance не равен canon

- **Идея:** после профильного результата нужен независимый downstream decision.
- **Проба:** KAN передал Stage A matrix и speech map, KOO отдельно прочитал и принял их в ограниченной области.
- **Результат:** оба результата usable downstream, но не стали Project Sources.
- **Оценка:** успех.
- **Фиксация:** `result → receipt → acceptance` является полноценной цепочкой; acceptance всегда читается буквально по scope.

### Опыт 2: task pointer не доказывает execution

- **Идея:** проверить реальную границу activation.
- **Проба:** адресный task попал в KAN inbox; detector PASS не запустил exact Entity-chat.
- **Результат:** профильная работа началась только после фактического пользовательского запуска текущего KAN и immutable task read.
- **Оценка:** частичный технологический успех.
- **Фиксация:** `detected != processing_started`; реальный result/receipt важнее activation marker.

### Опыт 3: automation-state быстро устаревает

- **Идея:** сократить число дублирующих GitHub-watch.
- **Проба:** ранее watches были консолидированы.
- **Результат:** позднее проект создал отдельные profile-work automations; старое состояние snapshot перестало быть текущим.
- **Оценка:** урок.
- **Фиксация:** automation-state нельзя хранить как долговременную истину recovery; только как observation with mandatory recheck.

## writer-state

- `entity: KAN`
- `current_instance_role: authoritative_current_writer_for_this_checkpoint`
- `source_barrier: passed`
- `writer_conflict_observed: no_in_current_task`
- `other_verified_instances: unknown_not_checked`

## safe next step

После publication/readback этого checkpoint:

> выполнить следующий GitHub-preflight; если нового exact KAN task нет, не придумывать себе содержательную работу. Отдельно остаются practical recovery test и неподтверждённая внешняя доставка локального COOP concept/claim map.

---

document_type: entity-self-snapshot
entity: KAN
status: current_for_preservation_checkpoint
trigger: bounded_acceptance_stageA_and_speech_decisions
project_time: omitted; trusted project-time source not used
