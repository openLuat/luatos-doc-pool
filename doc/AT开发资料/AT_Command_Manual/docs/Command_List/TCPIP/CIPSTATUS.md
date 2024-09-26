## 查询当前连接状态：AT+CIPSTATUS

语法规则：

| 命令类型 | 语法                                 | 返回和说明                                                   |
| -------- | ------------------------------------ | ------------------------------------------------------------ |
| 执行命令 | AT+CIPSTATUS                         | 如果是单路连接(AT+CIPMUX=0)，返回：<br>OK <br>STATE: <sl_state> |
|          |                                      | 如果是多路连接 (AT+CIPMUX=1)，返回：<br>OK <br>STATE:<ml_state> <br>`C:<n>,<bearer>, <TCP/UDP>, <IP address>, <port>, <client state>` |
| 查询指令 | `AT+CIPSTATUS=<n>`（多路连接时支持） | 多路连接 (AT+CIPMUX=1)，返回：<br>`<n>,<bearer>, <TCP/UDP>, <IP address>, <port>, <client state>` |
| 测试命令 | AT+CIPSTATUS=?                       | 返回：<br>OK                                                 |

 

参数定义：

| 参数             | 定义          | 取值                                                   | 对取值的说明                                 |
| ---------------- | ------------- | ------------------------------------------------------ | -------------------------------------------- |
| `<n>`            | Link No.      | 0~5                                                    | 整数型，表示连接序号与+CIPSTRAT中<n>定义一致 |
| `<bearer>`       | GPRS 承载方式 | 0~1                                                    | 缺省是0                                      |
| `<IP address>`   | IP 地址       | -                                                      | 字符串参数(字符串需要加引号)                 |
| `<port>`         | 端口号        | -                                                      | 整数型                                       |
| <sl_state>       | 单连接状态    | IP INITIAL                                             | 初始化                                       |
|                  |               | IP START                                               | 启动任务                                     |
|                  |               | IP CONFIG                                              | 配置场景                                     |
|                  |               | IP GPRSACT                                             | 场景已激活                                   |
|                  |               | IP STATUS                                              | 获得本地 IP 状态                             |
|                  |               | TCP CONNECTING/UDP <br>CONNECTING/SERVER <br>LISTENING | TCP 连接中/UDP 端口注册中/服务器侦听中       |
|                  |               | CONNECT OK                                             | 连接建立成功                                 |
|                  |               | TCP CLOSING/UDP <br>CLOSING                            | 正在关闭 TCP 连接，正在注销 UDP 端口         |
|                  |               | TCP CLOSED/UDP <br>CLOSED                              | 连接断开 /UDP 端口被注销                     |
|                  |               | PDP DEACT                                              | 场景被释放                                   |
| <ml_state>       | 多链接状态    | IP INITIAL                                             | 初始化                                       |
|                  |               | IP START                                               | 启动任务                                     |
|                  |               | IP CONFIG                                              | 配置场景                                     |
|                  |               | IP GPRSACT                                             | 场景已激活                                   |
|                  |               | IP STATUS                                              | 获得本地 IP 状态                             |
|                  |               | IP PROCESSING                                          | IP 数据阶段                                  |
|                  |               | PDP DEACT                                              | 场景被释放                                   |
| `<client state>` | 客户端状态    | INITIAL                                                | 初始化                                       |
|                  |               | CONNECTING                                             | 正在连接                                     |
|                  |               | CONNECTED                                              | 已连接                                       |
|                  |               | REMOTE CLOSING                                         | 对端关闭                                     |
|                  |               | CLOSING                                                | 正在关闭                                     |
|                  |               | CLOSED                                                 | 已关闭                                       |
