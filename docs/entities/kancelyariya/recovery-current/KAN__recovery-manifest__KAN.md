# Recovery manifest: КАНЦЕЛЯР

## Назначение

Минимальный recovery-пакет KAN после значимого speech-этапа и накопления нового операционного опыта.

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

## Значимые внешние результаты, входящие в current-state

### Speech legal-semantic map
- artifact: `puev5691/wellbeing-hq/entities/kancelar/outbox/KAN__speech-legal-semantic-map__KOO.md`
- commit: `649780fb0eef8e6bf441dcd7986def6f364ad727`
- blob: `dda9215c1084e003edd0064322db3377e9174cde`
- dispatch: `routes/dispatch/KAN__speech-legal-semantic-map__KOO.md`
- acceptance: `not_observed_at_checkpoint`

### Speech claims boundary
- artifact: `puev5691/wellbeing-hq/entities/kancelar/outbox/KAN__speech-claims-boundary__ARH.md`
- commit: `c8a4315f75e0ce7f8fe62642893150fee743b8dc`
- blob: `9559858a27cc7d105a1eff5c32c2e515ae9c0f93`
- dispatch: `routes/dispatch/KAN__speech-claims-boundary__ARH.md`
- acceptance: `not_observed_at_checkpoint`

### Activation boundary evidence
- commit: `d31705975e31dbfcd41f19862284a4a687aab6ae`
- result: detector PASS / activation requested / exact Entity-chat resume failed

## Локальный значимый артефакт с неподтверждённой внешней доставкой

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
2. Read initiation, snapshot, manifest.
3. Fetch external recovery locator.
4. Verify all three content files against `sha256sums.txt`.
5. Check immutable speech-artifact identities in `wellbeing-hq`.
6. Check current KAN inbox/dispatch/receipts; do not infer completion from stale inbox pointers.
7. Re-verify automation state before creating any watch.
8. Record one of:
   - `initiation_verified`
   - `initiation_loaded_external_unverified`
   - `initiation_failed`
9. Do not reconstruct missing state from memory.

## Preservation/readback boundary

Publication is not readback. Final publication/readback state is fixed only after external fetch of the final package version.

## Recoverability boundary

Structural sufficiency is not full recoverability. Full recoverability requires actual initiation test or equivalent ARH verification.

---

document_type: recovery-manifest
entity: KAN
status: current_package_pending_external_readback
recovery_canon: v1.4-approved
publication_state: pending_by_kan
readback_state: pending_by_kan
archive_acceptance_state: pending_arh
project_time: omitted; trusted project-time source not used
