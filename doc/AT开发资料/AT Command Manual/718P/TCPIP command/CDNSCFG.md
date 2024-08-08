## 配置域名服务器DNS：AT+CDNSCFG

语法规则：

| 命令类型 | 语法                                      | 返回                                                |
| -------- | ----------------------------------------- | --------------------------------------------------- |
| 设置命令 | AT+CDNSCFG=<pri_dns>[,<sec_ dns>[,<cid>]] | OK                                                  |
| 查询命令 | AT+CDNSCFG?                               | PrimaryDns: <pri_dns>SecondaryDns: <sec_dns> <br>OK |
| 测试命令 | AT+CDNSCFG=?                              | +CDNSCFG: ("Primary DNS"),("Secondary DNS") <br>OK  |

 

参数定义：

| 参数       | 定义                  | 取值 | 对取值的说明                                                 |
| ---------- | --------------------- | ---- | ------------------------------------------------------------ |
| <pri_dns>  | 主域名服务器的 IP地址 |      | 字符串参数(字符串需要加引号)                                 |
| <sec_ dns> | 备域名服务器的 IP地址 |      | 字符串参数(字符串需要加引号)                                 |
| <cid>      | 定义同+SAPBR中<cid>   | 1~3  | 当使用SAPBR激活pdp承载后，如有需要，再使用带<cid>的命令设置DNS服务器 |

举例：

| 命令(→)返回(←) | 实例                                                         | 解释和说明                                                   |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|                | **+CDNSCFG命令查询和修改域名服务器的场景应用1（TCPIP,MQTT应用）：** |                                                              |
| →              | AT+CREG?                                                     | 查询当前GPRS注册状态                                         |
| ←              | +CREG: 0,1 <br>OK                                            | <n>=0，表示禁用URC上报<br><stat>=1，标识已经注册GPRS网络，而且是本地网 |
| →              | AT+CSTT                                                      |                                                              |
| ←              | OK                                                           |                                                              |
| →              | AT+CIICR                                                     |                                                              |
| ←              | OK                                                           |                                                              |
| →              | AT+CIFSR                                                     |                                                              |
| ←              | 10.113.72.66                                                 |                                                              |
| →              | AT+CDNSCFG?                                                  | 查询默认DNS服务器                                            |
| ←              | PrimaryDns: 211.136.112.50<br>SecondaryDns: 211.136.150.66 <br>OK |                                                              |
| →              | AT+CDNSCFG=ip1,ip2                                           | 如果有需要，客户可以修改DNS服务器<br>ip1和ip2请按照实际的dns服务器地址输入，ip1和ip2可以加双括号，也可以不加 |
| ←              | OK                                                           |                                                              |
| →              | AT+CIPSTART=TCP,<server domain>,<port>                       | 连接一个域名地址。所有参数可加双括号，也可不加 <br>本例是TCPIP的应用举例。如果是MQTT应用，此时可依次输入: <br>AT+MCONFIG,AT+MIPSTART,AT+MCONNECT等命令，具体请参考[MQTT使用方法举例](#_使用方法举例) |
| ←              | OK <br>CONNECT OK                                            |                                                              |
|                | **+CDNSCFG查询和修改域名服务器的场景应用2（HTTP,FTP应用）:** |                                                              |
| →              | AT+SAPBR=3,1,"CONTYPE","GPRS"                                |                                                              |
| ←              | OK                                                           |                                                              |
| →              | AT+SAPBR=3,1,"APN",""                                        |                                                              |
| ←              | OK                                                           |                                                              |
| →              | AT+SAPBR=1,1                                                 | 激活cid=1的PDP上下文                                         |
| ←              | OK                                                           |                                                              |
| →              | AT+SAPBR=2,1                                                 |                                                              |
| ←              | +SAPBR: 1,1,010.169.179.213 <br>OK                           |                                                              |
| →              | AT+CDNSCFG=ip1,ip2,1                                         |                                                              |
| ←              | OK                                                           |                                                              |
| →              | AT+CDNSCFG?                                                  | 查询DNS服务器。这种应用场景，必须要先执行+CDNSCFG设置命令才能查询 |
| ←              | PrimaryDns: ip1<br>SecondaryDns: ip2 OK                      | 以上ip1,ip2都是实际的DNS域名服务器的ip地址，可加双括号，也可不加 |
| →              | HTTP应用，依次输入：AT+HTTPINIT，AT+HTTPPARA，AT+HTTPACTION等命令，具体请参考：[HTTP使用方法举例](#_使用方法举例_1) <br>FTP应用，依次输入：AT+FTPCID，AT+FTPSERV，AT+FTPUN，AT+FTPPW等命令，具体请参考：[FTP使用方法举例](#_使用方法举例_2) |                                                              |
