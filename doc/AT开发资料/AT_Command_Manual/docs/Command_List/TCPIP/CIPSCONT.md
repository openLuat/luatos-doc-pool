## 保存TCPIP应用上下文：AT+CIPSCONT

该命令的执行命令保存包含相应的TCPIP AT 命令参数，即TCPIP 应用上下文，当系统重启时，参数将自动载入。

查询命令查询当前的TCPIP应用上下文的设置。

 

语法规则：

| 命令类型 | 语法         | 返回和说明                                                   |
| -------- | ------------ | ------------------------------------------------------------ |
| 查询命令 | AT+CIPSCONT? | `+CIPSCONT:<value>`<br>`+CIPCSGP:<mode>`<br>`Gprs Config APN:<apn>`<br>`Gprs Config UserId:<user name>`<br>`Gprs Config Password:<password>`<br>`+CIPHEAD:<mode>`<br>`+CIPSHOWTP:<mode>`<br>`+CIPSRIP:<mode>`<br>`+CIPATS:<mode>,<time>`<br>`+CIPSPRT:<send prompt>`<br>`+CIPQSEND:<n>`<br>`+CIPMODE:<mode>`<br>`+CIPCCFG:<NmRetry>,<WaitTm>,<SendSz>,<esc>,<Rxmode>,<RxSize>,<Rxtimer>`<br>`+CIPMUX:<n>`<br>`+CIPDPDP:<mode>, <interval>, <timer>`<br>`+CIPRXGET:<mode>`<br>`+CIPRDTIMER: 2000,3500 `<br>OK |
| 执行命令 | AT+CIPSCONT  | OK                                                           |

 

参数定义：

| 参数      | 定义           | 取值 | 对取值的说明                       |
| --------- | -------------- | ---- | ---------------------------------- |
| `<value>` | 是否保存上下文 | 0    | 保存TCPIP 应用上下文               |
|           |                | 1    | 默认值，表示不保存TCPIP 应用上下文 |
