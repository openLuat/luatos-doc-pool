## IP应用设置：AT+SAPBR

语法规则：

| 命令类型 | 语法                                                         | 返回                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 执行命令 | AT+SAPBR=<cmd_type>,<cid>[,<ConParamTag>,<ConParamValue>]    | 如果<cmd_type> = 2<br>+SAPBR: <cid>,<Status>,<IP_Addr><br> OK |
|          |                                                              | 如果<cmd_type> = 4<br>+SAPBR:<ConParamTag>,<ConParamValue> <br>OK |
|          |                                                              | 其余<br>OK                                                   |
| 测试命令 | AT+SAPBR=?                                                   | +SAPBR: (0-4),(1-3),"ConParamTag","ConParamValue" <br>OK     |
| URC上报  | +SAPBR <cid>: DEACT                                          | 当移动场景去激活时，会有此上报                               |
| 注意事项 | SAPBR设置承载参数APN的时候需要注意以下事项：<br> 模块注册网络后会从网络自动获取<apn>并激活一个PDP上下文，用于RNDIS上网使用（此<apn>可以通过AT+CGDCONT?来查询），所以直接输入AT+SAPBR=3,<cid>,"APN","" 即可，模块内部会按照自动获取的<apn>来设置APN |                                                              |

 

参数定义：

| 参数                    | 定义           | 取值       | 对取值的说明                                                 |
| ----------------------- | -------------- | ---------- | ------------------------------------------------------------ |
| <cmd_type>              | 命令类型       | 0          | 关闭承载                                                     |
|                         |                | 1          | 打开承载                                                     |
|                         |                | 2          | 查询承载状态                                                 |
|                         |                | 3          | 设置承载参数                                                 |
|                         |                | 4          | 获取承载参数                                                 |
| <cid>                   | 承载上下文标识 | 1~3        |                                                              |
| <Status>                | 承载的状态     | 0          | 正在连接                                                     |
|                         |                | 1          | 已经连接                                                     |
|                         |                | 2          | 正在关闭                                                     |
|                         |                | 3          | 已经关闭                                                     |
| <IP_Addr>               | 承载IP地址     |            |                                                              |
| <ConParamTag>           | 承载参数       | "CONTYPE"  | 因特网连接类型。取值请参考参数<ConParamValue_ConType>        |
|                         |                | "APN"      | 接入点名称，最长支持 50 个字符                               |
|                         |                | "USER"     | 用户名称：最长支持 50 个字符                                 |
|                         |                | "PWD"      | 密码：最长支持 50 个字符                                     |
|                         |                | "PHONENUM" | CSD电话号码                                                  |
|                         |                | "RATE"     | CSD连接速率。<br>取值请参考<ConParamValue_Rate>。            |
| <ConParamValue>         |                |            |                                                              |
| <ConParamValue_ConType> | 因特网连接类型 | "CSD"      | CSD，电路交换数据业务                                        |
|                         |                | "GPRS"     | GPRS，通用分组无线业务<br>注：GPRS只是兼容2G模块指令的输入格式，不会强制切换到GPRS网络上，真实的数据承载网络取决于模块当时注册的网络制式 |
| <ConParamValue_Rate>    | CSD连接速率    | 0          | 2400                                                         |
|                         |                | 1          | 4800                                                         |
|                         |                | 2          | 9600                                                         |
|                         |                | 3          | 14400                                                        |
