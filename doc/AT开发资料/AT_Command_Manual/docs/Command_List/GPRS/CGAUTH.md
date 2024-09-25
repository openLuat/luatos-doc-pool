## PDP上下文鉴权参数：AT+CGAUTH

本命令是AT+CGDCONT命令的扩展，设置相关PDP上下文的鉴权方式。

查询命令查询所有PDP上下文鉴权信息。

语法规则：

| 命令类型 | 语法                                                    | 返回                                                         |
| -------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| 设置命令 | `AT+CGAUTH=<cid>[,<auth_prot>[,<userid>[,<password>]]]` | OK                                                           |
| 查询命令 | AT+CGAUTH?                                              | `[+CGAUTH: <cid>,<auth_prot>,<userid>,<password>] [<CR><LF>+CGAUTH: <cid>,<auth_prot>,<userid>,<password> [. . . ]]` |
| 测试命令 | AT+CGAUTH=?                                             | `+CGAUTH: (range of supported <cid>s), (list of supported <auth_prot>s), (range of supported <userid>s), (range of supported <password>s)` |

 

参数定义：

| 参数         | 定义                                     | 取值 | 对取值的说明                                                 |
| ------------ | ---------------------------------------- | ---- | ------------------------------------------------------------ |
| `<cid>`      | PDP上下文标识，用于标识一个PDP上下文定义 |      | 整数型。该参数对TE-MT接口而言是本地参数，并且可用于其他PDP上下文相关指令 |
| <auth_prot>  | 鉴权类型                                 | 0    | None                                                         |
|              |                                          | 1    | PAP                                                          |
|              |                                          | 2    | CHAP                                                         |
| `<userid>`   | 用户名                                   |      |                                                              |
| `<password>` | 密码                                     |      |                                                              |
