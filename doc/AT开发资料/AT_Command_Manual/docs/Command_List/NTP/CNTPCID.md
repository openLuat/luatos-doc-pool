## 设置GPRS承载场景ID：AT+CNTPCID

| 命令类型 | 语法               | 返回                              |
| -------- | ------------------ | --------------------------------- |
| 设置命令 | `AT+CNTPCID=<cid>` | OK                                |
| 查询命令 | AT+CNTPCID?        | `+CNTPCID:<cid>` <br>OK           |
| 测试命令 | AT+CNTPCID=?       | `+CNTPCID:(<cid>取值范围)` <br>OK |

 

参数定义：

| 参数    | 定义       | 取值 | 对取值的说明              |
| ------- | ---------- | ---- | ------------------------- |
| `<cid>` | 承载场景id | 1-3  | 取值同+SAPBR命令的`<cid>` |
