## 给GNSS发送控制命令：AT+CGNSCMD

语法规则：

| 命令类型 | 语法                                                     | 返回                              |
| -------- | -------------------------------------------------------- | --------------------------------- |
| 设置命令 | AT+CGNSCMD=<cmdType>,<cmdString>,<CmdHeadString>] <br>OK | OK                                |
|          |                                                          | +CME ERROR:<err>                  |
| 测试命令 | AT+CGNSCMD=?                                             | +CGNSCMD:(0-1),"cmdString" <br>OK |

 

参数定义：

| 参数            | 定义       | 取值 | 对取值的说明                           |
| --------------- | ---------- | ---- | -------------------------------------- |
| <cmdType>       | 命令类型   | 0    | NMEA style command。目前仅支持这种。   |
|                 |            | 1    | HEX style command。                    |
| <cmdString>     | 命令字符串 |      | 字符串类型                             |
| <CmdHeadString> | 应答特征   |      | 填入应答的特征字符，用于捕获命令的结果 |
