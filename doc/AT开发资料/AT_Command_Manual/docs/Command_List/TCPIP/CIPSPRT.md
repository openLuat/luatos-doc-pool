## 设置发送数据时是否显示‘>’和发送情况提示：AT+CIPSPRT

语法规则：

| 命令类型 | 语法                       | 返回                                       |
| -------- | -------------------------- | ------------------------------------------ |
| 设置命令 | `AT+CIPSPRT=<send prompt>` | OK                                         |
| 查询命令 | AT+CIPSPRT?                | `+CIPSPRT: <send prompt> `<br>OK           |
| 测试命令 | AT+CIPSPRT=?               | `+CIPSPRT: (<send prompt>取值列表) `<br>OK |

 

参数定义：

| 参数            | 定义                                                         | 取值 | 对取值的说明                                                 |
| --------------- | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
| `<send prompt>` | 执行 AT+CIPSEND 后是否显示‘>’ 和发送情况提示（即‘SEND OK‘或‘DATA ACCEPT‘）。<br>整数型 | 0    | 不显示‘>’，但返回 "SEND OK"或"DATA ACCEPT" <br>**注:**返回 "SEND OK"或"DATA ACCEPT"由AT+CIPQSEND这个命令的设定来决定 |
|                 |                                                              | 1    | 显示‘>’，且返回 "SEND OK" 或"DATA ACCEPT"缺省值<br>**注:**返回 "SEND OK"或"DATA ACCEPT" 由AT+CIPQSEND这个命令的设定来决定 |
|                 |                                                              | 2    | 不显示‘>’，不返回 "SEND OK" 或"DATA ACCEPT"                  |
