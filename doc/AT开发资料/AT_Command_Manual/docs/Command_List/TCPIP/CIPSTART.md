## 建立TCP连接或注册UDP端口号：AT+CIPSTART

语法规则：

| 命令类型 | 语法                                                         | 返回和说明                                                   |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 设置命令 | 单 路 连 接 (+CIPMUX=0)时： AT+CIPSTART=<mode>,<sever>,<port> | 如果格式正确且处于IP INITIAL 或者 IP STATUS或TCP/UDP CLOSE状态，返回：<br>OK<br>否则返回：<br>+CME ERROR <err> <br>紧接着会有URC上报，上报内容如下： <br>如果连接已经存在，返回：ALREADY CONNECT 如果连接成功(非透传)，返回：CONNECT OK如果连接成功(透传)，返回：CONNECT 否则返回:<br>STATE: <sl_state><br>CONNECT FAIL |
|          | 多路连接(+CIPMUX=1)时： AT+CIPSTART=<n>,<mode>,<server>,<port> | 如果格式正确且处于 IP STATUS或IP PROCESSING时，返回：<br>OK<br>否则返回：<br>+CME ERROR <err><br>紧接着会有URC上报，上报内容如下： <br>如果连接已经存在, 返回：<br><n>,ALREADY CONNECT 如果连接成功，返回：<n>,CONNECT OK<br>否则返回:<br><n>,CONNECT FAIL |
| 测试命令 | AT+CIPSTART=?                                                | 单路连接(+CIPMUX=0)时返回：<br>+CIPSTART: (<mode>取值列表),(IP address range),(port range)<br>+CIPSTART: (<mode>取值列表),(domain name),(port range)<br> OK |
|          |                                                              | 多路连接(+CIPMUX=1)时返回：<br>+CIPSTART: (<n> 取 值 列 表 ),( <mode> 取 值 列 表 ),(IP addressrange),(port range)<br>+CIPSTART: (<n>取值列表),(<mode>取值列表),(domain name),(portrange) <br>OK |
| 注意事项 | **1.** 此命令应用于建立 TCP/UDP 连接；<br>**2.** 当前状态可用AT+CIPSTATUS查询；<br>**3.** 单路连接时只当前状态为IP INITIAL 或者 IP STATUS或TCP/UDP CLOSE 时可执行，多路连接时当前状态为 IP STATUS或IP PROCESSING时可执行；<br>**4.** 在当前状态不是上述可执行状态时，需执行 AT+CIPSHUT后再开始建立连接；<br>**5.** 多路连接时，设置此命令前，必须先执行AT+CSTT, AT+CIICR,AT+CIFSR这三个命令。 |                                                              |

 

参数定义：

| 参数       | 定义                                   | 取值                                           | 对取值的说明                           |
| ---------- | -------------------------------------- | ---------------------------------------------- | -------------------------------------- |
| <n>        | Link No.                               | 0~5                                            | 整数型，表示连接序号                   |
| <mode>     | 连接类型，字符串型（双引号可加可不加） | "TCP"                                          | 建立TCP连接                            |
|            |                                        | "UDP"                                          | 建立UDP连接                            |
| <server>   | 远端服务器 IP 地址或域名皆可           | 最大128个字节                                  | 字符串参数（双引号可加可不加）         |
| <port>     | 远端服务端口                           | 1~65535                                        | 整数型                                 |
| <sl_state> | 单连接状态                             | IP INITIAL                                     | 初始化                                 |
|            |                                        | IP START                                       | 启动任务                               |
|            |                                        | IP CONFIG                                      | 配置场景                               |
|            |                                        | IP GPRSACT                                     | 场景已激活                             |
|            |                                        | IP STATUS                                      | 获得本地 IP 状态                       |
|            |                                        | TCP CONNECTING/UDP CONNECTING/SERVER LISTENING | TCP 连接中/UDP 端口注册中/服务器侦听中 |
|            |                                        | CONNECT OK                                     | 连接建立成功                           |
|            |                                        | TCP CLOSING/UDP CLOSING                        | 正在关闭 TCP 连接，正在注销 UDP 端口   |
|            |                                        | TCP CLOSED/UDP CLOSED                          | 连接断开 /UDP 端口被注销               |
|            |                                        | PDP DEACT                                      | 场景被释放                             |
