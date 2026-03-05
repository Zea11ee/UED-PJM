#!/usr/bin/env python3
"""Append a confirmed demand event row into project knowledge base markdown."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


PROJECT_FILE_MAP = {
    "ANTA": "ANTA.md",
    "REDMAGIC": "REDMAGIC.md",
    "RM": "REDMAGIC.md",
    "HYPERSHELL": "HYPERSHELL.md",
}


def bj_today() -> str:
    return datetime.now(ZoneInfo("Asia/Shanghai")).date().isoformat()


def normalize_project(value: str) -> str:
    return "".join(ch for ch in value.upper() if ch.isalnum())


def safe_cell(value: str) -> str:
    return value.replace("\n", " ").replace("|", "\\|").strip()


def parse_ids(raw: str) -> list[str]:
    if not raw:
        return []
    return [item.strip() for item in raw.split(",") if item.strip()]


def project_file_name(project: str) -> str:
    normalized = normalize_project(project)
    if normalized in PROJECT_FILE_MAP:
        return PROJECT_FILE_MAP[normalized]
    return f"{normalized}.md"


def ensure_project_file(project_file: Path, template_file: Path, project: str) -> None:
    if project_file.exists():
        return
    if template_file.exists():
        body = template_file.read_text(encoding="utf-8").replace("<PROJECT_NAME>", project.strip().upper())
    else:
        body = (
            f"# {project.strip().upper()}\n\n"
            "## 已确认变更事件（按时间倒序）\n"
            "| 日期 | 需求编号 | 页面/模块 | 功能/交互变化 | 状态 | 关联记录 |\n"
            "|---|---|---|---|---|---|\n"
        )
    project_file.write_text(body, encoding="utf-8")


def build_row(
    date: str,
    demand_id: str,
    module: str,
    change: str,
    status: str,
    parent_record_id: str,
    wbs_record_ids: list[str],
) -> str:
    links = []
    if parent_record_id:
        links.append(parent_record_id.strip())
    links.extend(wbs_record_ids)
    records = " / ".join(links) if links else "待补"
    cells = [
        safe_cell(date),
        safe_cell(demand_id),
        safe_cell(module),
        safe_cell(change),
        safe_cell(status),
        safe_cell(records),
    ]
    return "| " + " | ".join(cells) + " |"


def has_same_event(lines: list[str], demand_id: str, module: str, change: str) -> bool:
    key = (
        safe_cell(demand_id).lower(),
        safe_cell(module).lower(),
        safe_cell(change).lower(),
    )
    for raw in lines:
        line = raw.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        parts = [item.strip() for item in line.strip("|").split("|")]
        if len(parts) < 4:
            continue
        if (parts[1].lower(), parts[2].lower(), parts[3].lower()) == key:
            return True
    return False


def append_row(project_file: Path, row: str, demand_id: str, module: str, change: str, allow_duplicate: bool) -> str:
    lines = project_file.read_text(encoding="utf-8").splitlines()
    lines = [line for line in lines if not line.strip().startswith("| YYYY-MM-DD | XXX | XXX | XXX |")]

    if not allow_duplicate and has_same_event(lines, demand_id, module, change):
        return "skip_duplicate"

    insert_index = -1
    for idx, line in enumerate(lines):
        if line.strip().startswith("|---"):
            insert_index = idx + 1
            break

    if insert_index == -1:
        lines.extend(
            [
                "",
                "## 已确认变更事件（按时间倒序）",
                "| 日期 | 需求编号 | 页面/模块 | 功能/交互变化 | 状态 | 关联记录 |",
                "|---|---|---|---|---|---|",
                row,
            ]
        )
    else:
        lines.insert(insert_index, row)

    project_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return "appended"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append one project KB event row after demand write.")
    parser.add_argument("--project", required=True, help="Project name, e.g. ANTA/REDMAGIC/HYPERSHELL")
    parser.add_argument("--date", default=bj_today(), help="Event date, default Asia/Shanghai today")
    parser.add_argument("--demand-id", required=True, help="Demand ID or source number")
    parser.add_argument("--module", required=True, help="Page/module")
    parser.add_argument("--change", required=True, help="Feature/interaction change")
    parser.add_argument("--status", default="已排期", help="Status text")
    parser.add_argument("--parent-record-id", default="", help="Parent task record_id")
    parser.add_argument(
        "--wbs-record-ids",
        default="",
        help="Comma separated WBS record_ids, e.g. rec_a,rec_b",
    )
    parser.add_argument("--allow-duplicate", action="store_true", help="Allow duplicated events")
    parser.add_argument("--dry-run", action="store_true", help="Only print row and target file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    root_dir = Path(__file__).resolve().parents[2]
    kb_dir = root_dir / "references" / "project-kb"
    kb_dir.mkdir(parents=True, exist_ok=True)
    template_file = kb_dir / "_TEMPLATE.md"
    project_file = kb_dir / project_file_name(args.project)
    ensure_project_file(project_file, template_file, args.project)

    row = build_row(
        date=args.date,
        demand_id=args.demand_id,
        module=args.module,
        change=args.change,
        status=args.status,
        parent_record_id=args.parent_record_id,
        wbs_record_ids=parse_ids(args.wbs_record_ids),
    )

    if args.dry_run:
        print(f"[DRY-RUN] target={project_file}")
        print(f"[DRY-RUN] row={row}")
        return 0

    result = append_row(
        project_file=project_file,
        row=row,
        demand_id=args.demand_id,
        module=args.module,
        change=args.change,
        allow_duplicate=args.allow_duplicate,
    )

    if result == "skip_duplicate":
        print(f"[SKIP] Duplicate event already exists in {project_file}")
    else:
        print(f"[OK] Appended project KB row -> {project_file}")
        print(row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
