## 保存HTTP应用上下文：AT+HTTPSCONT

执行命令保存包含 AT 命令参数的 HTTP 应用上下文，当系统重启时，参数将自动载入。

查询命令返回 HTTP 应用上下文。

语法规则：

| 命令类型 | 语法          | 返回                                                         |
| -------- | ------------- | ------------------------------------------------------------ |
| 执行命令 | AT+HTTPSCONT  | `+HTTPREAD: (list of supported <start_address>s),( list of supported<byte_size>s) `<br>OK |
| 查询命令 | AT+HTTPSCONT? | `+HTTPSCONT:<mode>`<br>`CID:<value>`<br>`URL: <value>`<br>`UA: <value>`<br>`PROIP: <value>`<br>`PROPORT: <value>`<br>`REDIR: <value>`<br>`BREAK: <value>`<br>`BREAKEND: <value>`<br>`USERDATA:<data> `<br>OK |

 

参数定义：

| 参数     | 定义               | 取值 | 对取值的说明       |
| -------- | ------------------ | ---- | ------------------ |
| `<mode>` | HTTP上下文保存模式 | 0    | 保存，值取自 NVRAM |
|          |                    | 1    | 未保存，值取自 RAM |
