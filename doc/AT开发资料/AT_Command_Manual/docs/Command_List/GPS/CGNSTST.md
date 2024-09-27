## 将读取到的GNSS数据发送到AT口：AT+CGNSTST

语法规则：

| 命令类型 | 语法                       | 返回                     |
| -------- | -------------------------- | ------------------------ |
| 设置命令 | `AT+CGNSTST=<mode>` <br>OK | OK                       |
|          |                            | `+CME ERROR:<err>`       |
| 测试命令 | AT+CGNSTST?                | `+CGNSTST:<mode>` <br>OK |
| 测试命令 | AT+CGNSTST=?               | +CGNSTST:(0-1) <br>OK    |

 

参数定义：

| 参数     | 定义 | 取值 | 对取值的说明 |
| -------- | ---- | ---- | ------------ |
| `<mode>` | 开关 | 0    | switch off   |
|          |      | 1    | switch on    |
