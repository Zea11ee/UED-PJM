# UED Tables App Config (Fixed)

## 1) UED 项目管理
- app_token: MUKoblHoZaRddds7r3ScDw9gnqf
- WBS: tblxpFKHh8eJaZb7
- 任务源: tblBOuVv29OZVkDI
- 项目库: tblLc6VxEUbVBrNC
- 人员映射: tblRgK2eemK7SF8i
- UED 需求管理（同步表）: tblB1Iq7fGcrTIDa
- 其他表: 缺陷管理 tblTtjE11XiN7hHp / 线上问题 tblCqpC0KeYDQoT8 / 变更记录 tbljSHcyDTRbEXp4

## 2) UED 需求总表
- app_token: X2zabbNYUaTlGgsgfKdcQSOCnaf
- UED 需求管理: tblesE69fcAUGRwD
- 任务源（同步表）: tbl4JRHi6419e0dF

## 3) UED 项目大节点
- app_token: RtFlbZ0d1apT9Ms838ic2PiunId
- 大节点: tbl3fjwfw7bLe28z
- 项目列表: tbl11tRhUWl1WjA4
- HS 页面列表: tblRgaq1Nxuu9z2M
- 任务源: tbluo6awg0DZ5E7d

## Lookup (if values change)
1) wiki 搜索目标表，拿 node_token
2) wiki_v2_space_getNode → obj_token (bitable)
3) bitable_v1_appTable_list 列表匹配表名→ table_id

## 常用入口链接
- UED 项目管理： https://fastbase.feishu.cn/wiki/V7PBwEHn2iZIg5kGyQPc4eTLnrf?table=tblxpFKHh8eJaZb7&view=vewFP2NpMF
- UED 需求总表： https://fastbase.feishu.cn/wiki/LRt0w2zM1iliqNk0njFcYrnFnFh?table=tblesE69fcAUGRwD&view=vewDekCPA3
- UED 项目大节点： https://fastbase.feishu.cn/wiki/PWx5wpAEjiPRPXkNw6bc0ud9nnb?table=tbl3fjwfw7bLe28z&view=vew5YgSEn9

## 表间关系说明（简版）
- 需求总表 是外部需求入口与汇总，内含“UED 需求管理”与同步“任务源”。
- 项目管理 是执行主库，包含 任务源/WBS/项目库 等，并同步一张“UED 需求管理”。
- 项目大节点 用于节奏与里程碑视图，含“大节点/项目列表/任务源”等。
