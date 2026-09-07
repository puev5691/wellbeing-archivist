# Recovery manifest: КАНЦЕЛЯР

## Назначение

Текущий минимальный проверяемый recovery-пакет KAN после source-change checkpoint по roles v2.2 / recovery v1.4.

## External locator

    store: github
    repository: puev5691/wellbeing-archivist
    path: docs/entities/kancelyariya/recovery-current
    ref: main
    manifest: KAN__recovery-manifest__KAN.md
    checksums: sha256sums.txt

Этот locator существовал до checkpoint. Его прежнее содержимое было stale и обновляется текущим пакетом.

## Package files

- `KAN__initiation-current__KAN.md`
- `KAN__snapshot__KAN.md`
- `KAN__recovery-manifest__KAN.md`
- `sha256sums.txt`

`sha256sums.txt` является байтовой картой трёх содержательных recovery-файлов. Сам checksum-файл не включает собственный hash, чтобы не создавать самоссылку.

## Current approved Project Sources

| Source | SHA-256 |
|---|---|
| `project-instructions-core-v2_1-approved.md` | `8a86945c28e361b5adf7ecc96326a1591a193118ce7be258a9c0a21ddd2ace26` |
| `entity-roles-short-v2_2-approved.md` | `c8103b1c2dc6c3f4b489f118e9bcf4053add6bea384427f23dad5dddced2ae3d` |
| `file-work-canon-universal-v2_3-approved.md` | `5ec75e480c0b78a72bb2faa702a21064b32bd3b919b225b1ae25a30dd0a700e5` |
| `entity-state-preservation-and-recovery-canon-v1_4-approved.md` | `984871a22aab1910fc4ab3217c16488eac1e472734bdfd1948fd57c213566fda` |
| `source-loading-policy-v2-approved.md` | `2661a3a266547a5e0f6b70c3dab8a02add2bb788b4a90b1136b7e9445b2d6061` |

## Provenance

Source-change checkpoint:

- identity: `ARH__source-change-preservation-checkpoint__KAN.md`
- source_entity: `ARH`
- SHA-256: `88e76ad0319e064c7404e55ba275c9a7312d5e6124fb36248e4e5588d062ecb4`
- purpose: trigger current-writer KAN self-preservation after activation roles v2.2 / recovery v1.4

Previous external recovery was read from the same locator and identified as stale because its manifest/initiation/snapshot referred to older Project Sources and recovery v1.2.

## Writer-state

- `self_snapshot_author: KAN authoritative current-writer for this checkpoint`
- `archive_process_owner: ARH`
- `other_verified_instances: unknown_not_checked`
- `writer_conflict_observed: no_in_current_task`

## Recovery procedure

1. Read and verify five current approved Project Sources.
2. Read initiation, snapshot and manifest.
3. Open external locator.
4. Verify package files against `sha256sums.txt`.
5. Verify required source versions/checksums.
6. Confirm that snapshot distinguishes confirmed/current, open/parked and unknown/not_checked.
7. Record:
   - `initiation_verified`;
   - `initiation_loaded_external_unverified`; or
   - `initiation_failed`.
8. Load profile/topic sources only for the active task.
9. Do not reconstruct missing state from memory or historical files.

## Preservation/readback boundary

Publication of this package is not equivalent to readback.

After publication, the external files must be fetched again and their bytes/version identities checked. The final immutable Git commit of the publication cycle is recorded outside this manifest in the checkpoint result returned to ARH, because embedding that commit here would change the commit itself.

## Recoverability boundary

This package is intended to be structurally sufficient for initiation, but full recoverability is not claimed until an actual initiation test or equivalent ARH verification is performed.

---

document_type: recovery-manifest
entity: KAN
status: current_candidate_pending_external_readback
recovery_canon: v1.4-approved
project_time: generated_without_trusted_project_time
