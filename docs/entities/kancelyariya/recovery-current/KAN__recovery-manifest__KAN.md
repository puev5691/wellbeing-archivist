# Recovery manifest: КАНЦЕЛЯР

## Назначение

Минимальный recovery-пакет KAN после перехода approved role-source с v2.2 на v2.3 и фиксации текущих значимых задач.

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

Checksum table covers three substantive recovery files and does not include its own hash.

## Current approved Project Sources

| Source | SHA-256 |
|---|---|
| `project-instructions-core-v2_1-approved.md` | `8a86945c28e361b5adf7ecc96326a1591a193118ce7be258a9c0a21ddd2ace26` |
| `entity-roles-short-v2_3-approved.md` | `e50df08b5d11765ac5e38197b298ad476333e5f14e717e13a631f9d802dfe10a` |
| `file-work-canon-universal-v2_3-approved.md` | `5ec75e480c0b78a72bb2faa702a21064b32bd3b919b225b1ae25a30dd0a700e5` |
| `entity-state-preservation-and-recovery-canon-v1_4-approved.md` | `984871a22aab1910fc4ab3217c16488eac1e472734bdfd1948fd57c213566fda` |
| `source-loading-policy-v2-approved.md` | `2661a3a266547a5e0f6b70c3dab8a02add2bb788b4a90b1136b7e9445b2d6061` |

Role-source v2.3 approved locator:
`puev5691/wellbeing-archivist/docs/entities/kancelyariya/approved/shd-staff-role-v2_3/entity-roles-short-v2_3-approved.md@4254dd8e1154433b57bc06e1b1eaa1f75531ba57`

Git blob:
`402e229eef44de65f0a2d81a42e446d96c66189c`

## Significant current evidence

### SHD organizational update
- KOO artifact: `puev5691/wellbeing-hq/entities/koordinator/outbox/KOO__shd-staff-role-update__ALL.md`
- commit: `2d4046ef5b9ad52130bd00b517efd677180e1b52`
- blob: `10699f80fcec9038b486535cb684626aa605a0c2`
- future software contour: `planned_not_separately_activated`

### Entity Runner
- KAN experiment program commit: `17b00c6f7fc8566730ac56da0fc8ade05589499c`
- KAN status delta commit: `50482f21df0a544f50db7efc00dd03431f25c800`
- corrected package commit: `f1f20fc1142d54b75f5966a82c5b045778da036c`
- KOO integrity decision commit: `206481f0f9b3325ff26d0cef11b20e06e8c1ecc3`
- current provider runtime state: `not_yet_proven`
- provider-side action: `not_authorized`

### Literary candidate
- KAN operator-delta commit: `63f96bb7483dec2789cff5da63a061cab368c022`
- RED v0.3 task commit: `888cb04781def0eb29baeace1ba7fcc042551232`
- publication state: `not_authorized / awaiting_RED_v03_then_KAN_delta`

### Previous preservation
- previous recovery commit: `e2b861fdf33f87048242043efacf003eec4a91ab`
- ARH structural acceptance artifact commit: `3d8aaefc2cd09b98a0a468a0024ddbfbeed8c085`
- full recoverability: `not_yet_verified`

## Local significant artifact with unresolved external delivery

- file: `KAN__COOP-concept-claim-map__KOO.md`
- SHA-256: `155eba12a68aeed76f07df50a527d0494148e17e3d44de496f776a4e374844a5`
- state: `local_significant_artifact`
- external_delivery: `not_verified`

## Recovery procedure

1. Verify five current approved Project Sources, specifically role-source v2.3.
2. Read initiation, snapshot and manifest.
3. Fetch external recovery locator and verify checksum table.
4. Run fresh KAN GitHub-preflight.
5. Check RED v0.3 / Entity Runner / source-change receipts before treating pointers as open.
6. Re-verify automation state rather than inheriting it.
7. Record initiation outcome.
8. Do not reconstruct missing state from memory.

## Preservation/readback boundary

KAN performed immutable readback of the staged source-change package at commit `0746d5bd47dd41aa134b9ff427d2bf0e7a12112a`.

Verified:
- initiation SHA-256 matches checksum table;
- snapshot SHA-256 matches checksum table;
- manifest SHA-256 matches checksum table;
- checksum table itself was read back immutably;
- active role-source is v2.3 with verified SHA-256 `e50df08b5d11765ac5e38197b298ad476333e5f14e717e13a631f9d802dfe10a`.

This manifest status update is finalized with a second checksum update and final immutable readback. Publication/readback does not imply ARH acceptance.

## Recoverability boundary

A source-correct current package does not by itself prove practical recoverability. Full verification still requires controlled cold-start or equivalent test.

---

document_type: recovery-manifest
entity: KAN
status: current_package_kan_readback_verified_pending_arh_acceptance
recovery_canon: v1.4-approved
active_role_source: entity-roles-short-v2_3-approved.md
publication_state: confirmed_by_kan
readback_state: verified_by_kan
archive_acceptance_state: pending_arh_for_this_checkpoint
recoverability_state: practical_initiation_test_required_for_full_verification
project_time: omitted; trusted project-time source not used
