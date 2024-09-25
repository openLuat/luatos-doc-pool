## 读短信：AT+CMGR

使用设置指令，可将消息存储器`<mem1>`中，索引为`<index>`的消息返回到TE。若该消息处于"已接收未读"状态，则将其状态变为"已接收已读"。

语法规则：

| 命令类型 | 语法              | 返回和说明                                                   |
| -------- | ----------------- | ------------------------------------------------------------ |
| 设置命令 | `AT+CMGR=<index>` | PDU模式下（AT+CMGF=0），返回：<br>`+CMGR:<stat>,[<alpha>],<length><CR><LF><pdu>`<br> OK |
|          |                   | 如果是TEXT模式（AT+CMGF=1）：<br>对于SMS-DELIVER：<br>`+CMGR:<stat>,<oa>,[<alpha>],<scts>[,*<tooa>,<fo>,<pid>,<dcs>,<sca>,<tosca>,<length>*]<CR><LF><data>`<br> OK <br>对于SMS-SUBMIT：<br>`+CMGR:<stat>,<da>,[<alpha>][*,,,,,[],<sca>,<tosca>,<length>*]<CR><LF><data>`<br> OK <br>对于SMS-STATUS-REPORT：<br>`+CMGR:<stat>,<fo>,<mr>,[<ra>],[<tora>],<scts>,<dt>,<st>` <br>OK <br>对于SMS-COMMAND：<br>`+CMGR:<stat>,<fo>,<ct>[,*<pid>,[<m**n**>],[<da>],[<toda>],<length><CR><LF><cdata>] `<br>OK<br> 注:以上斜体字是否显示由+CSDH的设置决定 |
| 测试命令 | AT+CMGR=?         | OK                                                           |

 

参数定义：

| 参数             | 定义                                              | 取值 | 对取值的说明                                               |
| ---------------- | ------------------------------------------------- | ---- | ---------------------------------------------------------- |
| `<da>，<oa>`     |                                                   |      | 请参考AT+CMGW条目                                          |
| `<toda>，<tooa>` |                                                   |      |                                                            |
| `<length>`       |                                                   |      |                                                            |
| `<stat>`         |                                                   |      |                                                            |
| `<alpha>`        | MT 电话簿记录对应`<da>`或`<oa>`的显示             |      | 字符型                                                     |
| `<pid>`          | Protocol Identification                           |      | 请参考AT+CSMP条目                                          |
| `<fo>`           | PDU短信首字节                                     |      |                                                            |
| `<vp>`           | Valid Period                                      |      |                                                            |
| `<dcs>`          | Data Coding System                                |      |                                                            |
| `<scts>`         | 短信中心时间戳（Short Message Center Time Stamp） |      | 时间-字符串型GSM 03.40 TP-Service-Centre-Time-Stamp        |
| `<dt>`           | Discharge time                                    |      | 时间-字符串型GSM 03.40 TP-Discharge-Time，与`<st>`成对出现 |
| `<st>`           | Status                                            |      | 整数型GSM 03.40 TP-Status描述上一个已经发送的MO短信的状态  |
| `<ct>`           | Command Type                                      |      | 整数型GSM 03.40 TP-Command-Type，缺省为0                   |
| `<ra>`           | 接收地址                                          |      | 字符串型的GSM 03.40 TP-Recipient-Address 地址-取值字段     |
| `<cdata>`        | TEXT模式下SMS-COMMAND的返回                       |      | TP-Command-Data(GSM 03.40)                                 |
| `<mr>`           | 消息参考（MessageReference）                      |      | TP-Message-Reference(GSM 03.40), 整数型                    |
| `<mn>`           | 消息序号                                          |      | TP-Message-Number(GSM 03.40), 整数型                       |

 

举例：

| 命令（→）/  返回（←） | 实例                                                         | 解释和说明                                                   |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|                       | 用TEXT模式读取短信：                                         |                                                              |
| →                     | AT+CMGF=1                                                    | 设置为TEXT模式                                               |
| ←                     | OK                                                           |                                                              |
| →                     | AT+CSCS="GSM"                                                | +CSCS命令决定了读取的短信内容的编码方式                      |
| ←                     | OK                                                           |                                                              |
| →                     | AT+CMGR=6                                                    | 读取index=6的英文短信                                        |
| ←                     | +CMGR: "REC READ","+86139*******9","12/03/30,20:40:31+32"<br> HI! <br>OK | 这个英文短信的内容为"HI"                                     |
| →                     | AT+CMGR=1                                                    | Air720S系列模块读一个内容有中文的短信                        |
| ←                     | +CMGR: "REC READ","002B0038003600310033003100360032003300310030003200360033",,"13/01/06,10:11:47+32"<br>611F8C2200310032<br> OK | 注：TEXT模式下Air720S系列模块收到带有中文的短信，显示的是短信内容的UCS2码的可见字符形式例如本例是"感谢12"的UCS2码的可见字符形式 TEXT模式下如果Air720S系列模块收到的是不含中文的短信，则直接显示内容 |
| →                     | AT+CMGR=2                                                    | Air720U系列模块读一个内容有中文的短信                        |
| ←                     | +CMGR: "REC READ","002B0038003600310033003100360032003300310030003200360033",,"13/01/06,10:11:47+32"<br>感谢34<br> OK | 注：Air720U系列模块一个内容有中文的短信，是用的GB2312编码    |
|                       | 用PDU模式读取一个短信：                                      |                                                              |
| →                     | AT+CMGF=0                                                    | 设置为PDU模式                                                |
| ←                     | OK                                                           |                                                              |
| →                     | AT+CMGR=9                                                    | 读取index=9的短信                                            |
| ←                     | +CMGR: 0,,240891683108200105F0240D91683161450179F900082180904121102304611F8C22 <br>OK |                                                              |
