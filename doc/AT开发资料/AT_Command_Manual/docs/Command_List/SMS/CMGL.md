## 列举短消息：AT+CMGL

使用设置指令，可将查询优选消息存储器`<mem1>`中，状态值为`<stat>`的消息显示在 TE中。若该消息处于"已接收未读"状态，则将其状态变为"已接收已读"。

语法规则：

| 命令类型 | 语法             | 返回和说明                                                   |
| -------- | ---------------- | ------------------------------------------------------------ |
| 设置命令 | `AT+CMGL=<stat>` | 如果是PDU模式（AT+CMGF=0），则`<stat>`取值如下：<br>0已接收的未读消息<br>1  已接收的已读消息<br>2  已存储的未发送短信<br>3  已存储的已发送短信<br>4  所有短信<br>且返回如下：<br>`+CMGL:<index>,<stat>,[<alpha>],<length><CR><LF>< pdu><CR><LF>+CMGL:<index>,<stat>,[<alpha>],<length><CR><LF><pdu>[...]] `<br>OK |
|          |                  | 如果是TEXT模式（AT+CMGF=1），则`<stat>`取值如下：<br>"REC UNREAD"  已接收的未读消息<br>"REC READ"    已接收的已读消息<br>"STO UNSENT"已存储的未发送短信<br>"STO SENT"已存储的已发送短信<br>"ALL"所有短信<br>**注意：对于以上取值，所有字母要大写。双引号可加可不加**。<br>对于SMS-DELIVER或SMS-SUBMIT，则返回（注：斜体字是否显示由+CSDH的设置决定）：<br>`+CMGL:<index>,<stat>,<oa/da>,[<alpha>],[<scts>][,*,*]<CR><LF><data>[<CR><LF>+CMGL:<index>,<stat>,<da/oa>,[<alpha>],[<scts>][,*,*]<CR><LF><data>[...]] ` <br>OK <br>对于SMS-STATUS-REPORT，则返回：<br>`+CMGL:<index>,<stat>,<fo>,<mr>,[<ra>],[<tora>],<scts>,<dt>,<st>[<CR><LF>+CMGL:<index>,<stat>,<fo>,<mr>,[<ra>],[<tora>],<scts>,<dt>,<st>[...]] `<br>OK<br> 对于SMS-COMMAND，则返回：<br>`+CMGL:<index>,<stat>,<fo>,<ct>[<CR><LF>+CMGL:<index>,<stat>,<fo>,<ct>[...]]` <br>OK |
| 测试命令 | AT+CMGL=?        | `+CMGL: (<stat>取值列表)` <br>OK                             |

 

参数定义：

| 参数 | 定义 | 取值 | 对取值的说明                                             |
| ---- | ---- | ---- | -------------------------------------------------------- |
|      |      |      | 本词条的所有参数在以前的命令中都有详细叙述，这里不再赘述 |

 

举例：

| 命令（→）/返回（←） | 实例                                                         | 解释和说明                            |
| ------------------- | ------------------------------------------------------------ | ------------------------------------- |
|                     | 在TEXT模式下列举短信：                                       |                                       |
| →                   | AT+CMGF=1                                                    | 设置为TEXT模式                        |
| ←                   | OK                                                           |                                       |
| →                   | AT+CMGL=?                                                    | 查询<stat>取值列表                    |
| ←                   | +CMGL: "REC UNREAD","REC READ","STO UNSENT","STO SENT","ALL" <br>OK |                                       |
| →                   | AT+CMGL="ALL"                                                | 查询所有的短信（注意：ALL必须为大写） |
|                     | +CMGL: 8,"REC READ","+8613162310263",,"12/08/08,10:43:04+32"hi+CMGL: 9,"REC READ","+8613162310263",,"12/08/09,14:12:01+32"aŒ" <br>OK | 所有短信 Index=1~7被删掉了而已。      |
|                     | 在PDU模式下列举短信：                                        |                                       |
| →                   | AT+CMGF=0                                                    | 设置为PDU模式                         |
| ←                   | OK                                                           |                                       |
| →                   | AT+CMGL=?                                                    |                                       |
| ←                   | +CMGL: (0-4) <br>OK                                          |                                       |
| →                   | AT+CMGL=4                                                    | 查询所有的短信                        |
| ←                   | +CMGL: 8,1,,24<br>0891683108200105F0240D91683161320162F300002180800134402304D7A2930A<br>+CMGL: 9,1,,24<br>0891683108200105F0240D91683161320162F300082180904121102304611F8C22 <br>OK | 显示查询结果                          |

 
