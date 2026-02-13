# Bitable 操作要点

## 查询/过滤
- Date 过滤：支持 `is/isGreater/isLess/isEmpty/isNotEmpty`；`CurrentWeek` 仅用于 `is`。
- 时间戳：毫秒，转 Asia/Shanghai 当地 00:00。
- 排序后按结束日期降序，可提前停页（结束日期 < 周起）减少开销。

## 写入
- DuplexLink 用 **record_id 字符串数组**，不要写对象。
- Single/MultiSelect 用选项“名称”字符串，避免生成乱码新选项。
- 不新增选项/记录，除非业务明确要求。

## 常见错误
- 权限/租户不匹配：404 隐匿；确认文档与 token 数据域。
- 日期格式错误：校验 ms 时间戳，避免秒级。
- 批量写失败：回退单记录写。

## 任务查询准则（WBS）
- 本周到期未完结：状态 != 已完成；结束日期在本周；结束日期非空。
- 周期：周一 00:00:00 至周日 23:59:59（Asia/Shanghai）。
