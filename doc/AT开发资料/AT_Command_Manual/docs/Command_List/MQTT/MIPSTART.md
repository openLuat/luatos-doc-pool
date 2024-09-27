## 建立TCP连接：AT+MIPSTART

语法规则：

| 命令类型     | 语法                                                         | 返回                                                         | 说明         |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------ |
| 设置命令     | 普通链接：<br>`AT+MIPSTART=<svraddr>,<port>` <br>SSL链接：`AT+SSLMIPSTART=<svraddr>,<port>` | OK                                                           | 正常返回     |
|              |                                                              | ERROR                                                        | 输入格式有误 |
|              |                                                              | 输入这条设置命令以后，后续会有URC上报。<br> 1) 单链接（AT+CIPMUX=0） <br>如果链接成功地建立，则上报：<br>CONNECT OK<br> 如果链接已经存在，则上报：<br>ALREADY CONNECT <br>如果链接失败，则上报：<br>`STATE:<state>`<br>CONNECT FAIL <br>2) 多链接（AT+CIPMUX=1）<br>如果链接成功地建立，则上报：<br>7,CONNECT OK <br>如果链接已经存在，则上报：<br>ALREADY CONNECT <br>如果链接失败，则上报：<br>7,CONNECT FAIL |              |
| 测试命令     | AT+MIPSTART=?                                                | +MIPSTART:"(0,255).(0,255).(0,255).(0,255)",(1-65535)<br>+MIPSTART:"DOMAIN NAME",(1-65535) <br>OK |              |
|              | AT+SSLMIPSTART=?                                             | +SSLMIPSTART:"(0,255).(0,255).(0,255).(0,255)",(1-65535)<br>+SSLMIPSTART:"DOMAIN NAME",(1-65535) <br>OK |              |
| **注意事项** | **当使用SSL链接进行数据传输时，链接命令为: `AT+SSLMIPSTART=<svraddr>,<port>`其余跟普通链接一样。这点请知悉！** |                                                              |              |

 

参数定义：

| 参数        | 定义                  | 取值                         | 对取值的说明                                      |
| ----------- | --------------------- | ---------------------------- | ------------------------------------------------- |
| `<svraddr>` | 服务器IP地址或DNS地址 | domain name或XXX.XXX.XXX.XXX | XXX 取值范围：0~255<br>可以用""括住，也可以不用"" |
| `<port>`    | server port           | 1-65535                      | 可以用""括住，也可以不用""                        |
