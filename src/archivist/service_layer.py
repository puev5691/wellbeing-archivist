from __future__ import annotations

from typing import Any

from .bootstrap_packages import (
    DEFAULT_BOOTSTRAP_PACKAGES_ROOT,
    collect_bootstrap_package_summary,
    list_bootstrap_packages,
)

from .db import Database
from .entities_registry import ensure_entities_table, get_entity_state
from .steps_registry import (
    ensure_steps_table,
    get_active_step,
    get_last_confirmed_step,
    list_recent_artifacts,
)


def build_service_query_payload(
    db: Database,
    *,
    query_type: str,
    callsign: str | None = None,
    entity_id: int | None = None,
    limit: int = 10,
    packages_root: str | None = None,
    package_dir: str | None = None,
) -> tuple[dict[str, Any], int]:
    if query_type == "bootstrap-packages":
        root = packages_root or DEFAULT_BOOTSTRAP_PACKAGES_ROOT
        items = list_bootstrap_packages(root)
        if limit > 0:
            items = items[:limit]
        payload = {
            "ok": True,
            "query_type": query_type,
            "data": {
                "items": items,
                "count": len(items),
                "packages_root": str(root),
            },
        }
        return payload, 0

    if query_type == "bootstrap-package-summary":
        if not package_dir:
            payload = {
                "ok": False,
                "query_type": query_type,
                "error": "package_dir_required",
            }
            return payload, 2
        payload = {
            "ok": True,
            "query_type": query_type,
            "data": collect_bootstrap_package_summary(package_dir),
        }
        return payload, 0

    db.init_schema()
    ensure_entities_table(db)
    ensure_steps_table(db)

    entity = get_entity_state(
        db,
        entity_id=entity_id,
        callsign=callsign,
    )
    if entity is None:
        payload = {
            "ok": False,
            "query_type": query_type,
            "error": "entity_not_found",
            "callsign": callsign,
            "entity_id": entity_id,
        }
        return payload, 1

    real_entity_id = int(entity["id"])
    active_step = get_active_step(db, entity_id=real_entity_id)
    last_confirmed_step = get_last_confirmed_step(db, entity_id=real_entity_id)

    if active_step is not None:
        operational_state_text = "active step present"
    elif last_confirmed_step is not None:
        operational_state_text = "idle with confirmed history"
    else:
        operational_state_text = "no active step"

    if query_type == "active-step":
        data: dict[str, Any] = {
            "active_step": active_step,
        }
    elif query_type == "entity-summary":
        data = {
            "active_step": active_step,
            "last_confirmed_step": last_confirmed_step,
            "operational_state_text": operational_state_text,
        }
    elif query_type == "recent-artifacts":
        items = list_recent_artifacts(
            db,
            entity_id=real_entity_id,
            limit=limit,
        )
        data = {
            "items": items,
            "count": len(items),
        }
    else:
        payload = {
            "ok": False,
            "query_type": query_type,
            "error": "unsupported_query_type",
        }
        return payload, 2

    payload = {
        "ok": True,
        "query_type": query_type,
        "entity": {
            "id": entity.get("id"),
            "callsign": entity.get("callsign"),
            "contour": entity.get("contour"),
            "role": entity.get("role"),
            "status": entity.get("status"),
            "current_phase": entity.get("current_phase"),
            "package_path": entity.get("package_path"),
        },
        "data": data,
    }
    return payload, 0
