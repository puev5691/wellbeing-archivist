# Recovery manifest: КАНЦЕЛЯР

## Назначение

Минимальный recovery-пакет KAN после bounded acceptance Stage A public/legal result и speech legal-semantic guidance.

## External locator

    store: github
    repository: puev5691/wellbeing-archivist
    path: docs/entities/kancelyariya/recovery-current
    ref: main
    manifest: KAN__recovery-manifest__KAN.md
    checksums: sha256sums.txt

## Package files

- `KAN__initiation-current__KAN.md`
- `KAN__snapshot__KAN.md`
- `KAN__recovery-manifest__KAN.md`
- `sha256sums.txt`

`sha256sums.txt` проверяет три содержательных recovery-файла и не включает собственный hash.

## Current approved Project Sources

| Source | SHA-256 |
|---|---|
| `project-instructions-core-v2_1-approved.md` | `8a86945c28e361b5adf7ecc96326a1591a193118ce7be258a9c0a21ddd2ace26` |
| `entity-roles-short-v2_2-approved.md` | `c8103b1c2dc6c3f4b489f118e9bcf4053add6bea384427f23dad5dddced2ae3d` |
| `file-work-canon-universal-v2_3-approved.md` | `5ec75e480c0b78a72bb2faa702a21064b32bd3b919b225b1ae25a30dd0a700e5` |
| `entity-state-preservation-and-recovery-canon-v1_4-approved.md` | `984871a22aab1910fc4ab3217c16488eac1e472734bdfd1948fd57c213566fda` |
| `source-loading-policy-v2-approved.md` | `2661a3a266547a5e0f6b70c3dab8a02add2bb788b4a90b1136b7e9445b2d6061` |

## Current significant results

### GitHub information-entry Stage A public/legal boundary
- artifact: `puev5691/wellbeing-hq/entities/kancelar/outbox/KAN__github-info-entry-public-legal-boundary__KOO.md`
- result commit: `6545a413dab7cc29e1d8485176402f24c23367f9`
- result blob: `e071667b6b124060a49b9c86f653b7703ad3f9af`
- KOO decision commit: `c1a0b52e44559678ec299cc8dbcdcd0ac7961e16`
- decision: `ACCEPTED_BOUNDED_STAGE_A_WORKING_RESULT`
- KAN decision-receipt commit: `6d3f037b69bb901138acabee8f0d9891ddab7eff`

### Speech legal-semantic map
- artifact: `puev5691/wellbeing-hq/entities/kancelar/outbox/KAN__speech-legal-semantic-map__KOO.md`
- result commit: `649780fb0eef8e6bf441dcd7986def6f364ad727`
- result blob: `dda9215c1084e003edd0064322db3377e9174cde`
- KOO decision commit: `8e7088c3c94e668c961d1e666bcc05cc9435029b`
- decision: `ACCEPTED_AS_BOUNDED_SPEECH_GUIDANCE`
- KAN decision-receipt commit: `b5d4fc04428ff958c5d54e062054044e8da4e5d5`

### Previous preservation acceptance
- previous recovery commit: `97d12b996f3a68cf757d7d2aa4389f4310dca6ed`
- ARH preservation state: `accepted_structurally`
- ARH immutable readback: `verified_by_arh`
- full recoverability: `not_yet_verified`
- remaining gate: practical initiation test

## Local significant artifact with unresolved external delivery

- file: `KAN__COOP-concept-claim-map__KOO.md`
- SHA-256: `155eba12a68aeed76f07df50a527d0494148e17e3d44de496f776a4e374844a5`
- state: `local_significant_artifact`
- external_delivery: `not_verified`

## Writer-state

- `self_snapshot_author: KAN authoritative current-writer for this checkpoint`
- `archive_process_owner: ARH`
- `other_verified_instances: unknown_not_checked`
- `writer_conflict_observed: no_in_current_task`

## Recovery procedure

1. Verify five current approved Project Sources.
2. Read initiation, snapshot and manifest.
3. Fetch external recovery locator.
4. Verify content files against `sha256sums.txt`.
5. Check immutable Stage A and speech result/decision identities in `wellbeing-hq`.
6. Run fresh KAN GitHub-preflight before selecting work.
7. Do not treat stale inbox pointers as open work without comparing result/receipt/acceptance.
8. Re-verify automation state instead of inheriting it.
9. Record `initiation_verified`, `initiation_loaded_external_unverified` or `initiation_failed`.
10. Do not reconstruct missing state from memory.

## Preservation/readback boundary

KAN выполнил immutable external readback staged package и проверил доступность initiation/snapshot/manifest/checksum table. Финальная версия checksum file обновляется после перевода manifest в readback-verified state и затем повторно читается по финальному immutable commit.

## Recoverability boundary

Предыдущий package был structurally accepted АРХИВАРИУСОМ. Новый package сохраняет это подтверждённое состояние, но не заявляет full recoverability без practical initiation test и независимой ARH-проверки нового checkpoint.

---

document_type: recovery-manifest
entity: KAN
status: current_package_kan_readback_verified_pending_arh_acceptance
recovery_canon: v1.4-approved
publication_state: confirmed_by_kan
readback_state: verified_by_kan
archive_acceptance_state: pending_arh_for_this_checkpoint
recoverability_state: practical_initiation_test_required_for_full_verification
project_time: omitted; trusted project-time source not used
