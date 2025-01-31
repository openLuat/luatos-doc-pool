## 发起呼叫：ATD

此命令可用于进行PPP拨号和手机通话两个功能。

语法规则：

| 命令类型         | 语法             | 返回                                                         |
| ---------------- | ---------------- | ------------------------------------------------------------ |
| 执行命令         | ATD<dial_string> | 命令成功，则返回：<br>OK\<br>通话建立成功：<br>^MODE: 17,17<br>+E_UTRAN Service<br>+CGEV: NW ACT 15,7,0<br>通话挂断，则返回：<br>^MODE: 0,0<br>+NO Service<br>+CGEV: NW DEACT 15, 7, 0<br>通话被挂断，则返回：<br>CGEV: NW MODIFY 7,2,0<br>通话结束或建立失败：<br>NO CARRIER |
| +CME ERROR:<err> |                  |                                                              |

 

参数定义：

| 参数            | 定义     | 取值 | 对取值的说明                                              |
| --------------- | -------- | ---- | --------------------------------------------------------- |
| < dial_string > | 拨号号码 | *99# | 进行数据PPP拨号                                           |
|                 |          | -    | 由以下字符组成：0-9, * , #, +, A, B, C 注：不支持紧急呼叫 |

 

举例：

| 命令（→）/返回（←） | 实例                                                         | 解释和说明                                                   |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ->                  | ATD13165****98                                               | 语音呼叫号码131623\*\*\*98（***是为了保护隐私，将实际数字隐去，实际操作时要如实输入号码） |
| <-                  | OK <br>^MODE: 17,17<br>+E_UTRAN Service<br>+CGEV: NW ACT 15,7,0 | 电话已拨通                                                   |
| ->                  | AT+CHUP                                                      | 模块主动挂断电话                                             |
| <-                  | OK                                                           | 执行完成，返回OK                                             |
