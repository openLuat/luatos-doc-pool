## 启动多IP连接：AT+CIPMUX

语法规则：

| 命令类型 | 语法                                               | 返回                  |
| -------- | -------------------------------------------------- | --------------------- |
| 设置命令 | `AT+CIPMUX=<n>`                                    | OK                    |
| 查询命令 | AT+CIPMUX?                                         | `+CIPMUX: <n>` <br>OK |
| 测试命令 | AT+CIPMUX=?                                        | +CIPMUX: (0,1) <br>OK |
| 注意事项 | 只在 IP initial 状态，本命令的设置命令才能设置成功 |                       |

 

参数定义：

| 参数  | 定义         | 取值 | 对取值的说明       |
| ----- | ------------ | ---- | ------------------ |
| `<n>` | 多路连接开关 | 0    | 单路连接（缺省值） |
|       |              | 1    | 多路连接           |
