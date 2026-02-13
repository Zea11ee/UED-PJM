# Timezone Rules (Bitable/WBS)

- All WBS scheduling is in Beijing time (Asia/Shanghai).
- Bitable date fields are Unix milliseconds (UTC). Always convert to Asia/Shanghai before reasoning.
- Off-by-one day errors usually mean UTC dates were used.

Example:
- 1769616000000 (UTC) = 2026-01-29 00:00 (Asia/Shanghai)
