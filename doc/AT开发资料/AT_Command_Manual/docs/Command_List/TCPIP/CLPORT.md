## 配置本地TCP端口：AT+CLPORT

语法规则：

| 命令类型 | 语法                                                         | 返回                                                         |                  |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------- |
| 设置命令 | 单链接：`AT+CLPORT=<mode>,<port> `<br>多链接：`AT+CLPORT=<n>,<mode>,<port>` | OK<br>或<br>ERROR                                            |                  |
| 查询命令 | AT+CLPORT?                                                   | `+CLPORT: <TCP port>,<UDP port>`<br> OK                      | 单链接(CIPMUX=0) |
|          |                                                              | `+CLPORT: 0,<TCP port>,<UDP port>`<br>`+CLPORT: 1,<TCP port>,<UDP port>`<br>`+CLPORT: 2,<TCP port>,<UDP port>`<br>`+CLPORT: 3,<TCP port>,<UDP port>`<br>`+CLPORT: 4,<TCP port>,<UDP port>`<br>`+CLPORT: 5,<TCP port>,<UDP port> `<br>OK | 多链接(CIPMUX=1) |
| 测试命令 | AT+CLPORT=?                                                  | +CLPORT: ("TCP","UDP"),(0-65535)<br> OK                      | 单链接(CIPMUX=0) |
|          |                                                              | +CLPORT: (0-5),("TCP","UDP"),(0-65535)<br> OK                | 多链接(CIPMUX=1) |

 

参数定义：

| `<n>`    | Link No.                               | 0~5     | 整数型，表示连接序号 |
| -------- | -------------------------------------- | ------- | -------------------- |
| `<mode>` | 连接类型，字符串型（双引号可加可不加） | "TCP"   | 建立TCP连接          |
|          |                                        | "UDP"   | 建立UDP连接          |
| `<port>` | 模块服务端口                           | 1~65535 | 整数型               |
