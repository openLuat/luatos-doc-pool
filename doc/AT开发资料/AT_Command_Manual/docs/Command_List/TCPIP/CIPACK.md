## 查询已连接数据传输状态：AT+CIPACK

语法规则：

| 命令类型 | 语法                                                         | 返回                                           |
| -------- | ------------------------------------------------------------ | ---------------------------------------------- |
| 设置命令 | 多路连接(+CIPMUX=1)： <br>`AT+CIPACK=<n>`                    | `+CIPACK: <txlen>, <acklen>, <nacklen>`<br> OK |
| 执行命令 | 单路连接(AT+CIPMUX=0)： <br>AT+CIPACK                        | `+CIPACK: <txlen>, <acklen>, <nacklen>` <br>OK |
| 测试命令 | AT+CIPACK=?                                                  | OK                                             |
| 注意事项 | 当链接建立后，查询AT`+CIPACK，<txlen>, <acklen>, <nacklen>`三个参数的初始值都是0，每发一笔数据，这三个参数都会累积增加。<br>AT+CIPSHUT后或链接断链后重连，查询AT+CIPACK，三个参数都重置为0 |                                                |

 

参数定义：

| 参数        | 定义                                              | 取值 | 对取值的说明                                     |
| ----------- | ------------------------------------------------- | ---- | ------------------------------------------------ |
| `<n>`       | Link No.                                          | 0~5  | 整数型，表示连接序号。与+CIPSTRAT中`<n>`定义一致 |
| `<txlen>`   | 链接`<n>`建立以来累计已发送的数据字节数           | -    | 整数型                                           |
| `<acklen>`  | 链接`<n>`建立以来累计服务器已确认收到的数据字节数 | -    | 整数型                                           |
| `<nacklen>` | 链接`<n>`建立以来服务器尙未确认收到的数据字节数   | -    | 整数型                                           |
