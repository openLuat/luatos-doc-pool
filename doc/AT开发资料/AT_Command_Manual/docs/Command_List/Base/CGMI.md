## 查询制造商名称：AT+CGMI

语法规则：

| 命令类型 | 语法    | 返回                   |
| -------- | ------- | ---------------------- |
| 执行命令 | AT+CGMI | `<manufacturer>`<br>OK |

参数定义：

| 参数             | 定义        | 取值 | 对取值的说明       |
| ---------------- | ----------- | ---- | ------------------ |
| `<manufacturer>` | 生产厂商 ID |      | 取值由模块厂商定义 |

举例：

| 命令（→）/返回（←） | 实例               | 解释和说明             |
| ------------------- | ------------------ | ---------------------- |
| →                   | AT+CGMI            | 查询模块的生产厂商的ID |
| ←                   | +CGMI: "AirM2M" OK | 返回查询结果           |
