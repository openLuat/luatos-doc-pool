## 下载文件：AT+FTPGET

语法规则：

| 命令类型 | 语法                           | 返回                                                         | 说明                                     |
| -------- | ------------------------------ | ------------------------------------------------------------ | ---------------------------------------- |
| 设置命令 | AT+FTPGET=<mode>[,<reqlength>] | OK                                                           | 输入AT+FTPGET=1 的返回                   |
|          |                                | +FTPGET:2,<cnlength>……..数据………..<br> OK                     | 输入：<br>AT+FTPGET=2, <reqlength>的返回 |
| URC上报  | +FTPGET:1,1                    | 输入AT+FTPGET=1后，有此上报，表示有数据了，第一个参数1表示<mode>为1 |                                          |
|          | +FTPGET:1,<error>              | 输入AT+FTPGET=1后，有此上报，表示FTP下载失败，第一个参数1表示<mode>为1 |                                          |
|          | +FTPGET:1,0                    | 表示数据传输结束，第一个参数1表示<mode>为1                   |                                          |
| 测试命令 | AT+FTPGET=?                    | OK                                                           |                                          |

 

参数定义：

| 参数        | 定义               | 取值   | 对取值的说明                                 |
| ----------- | ------------------ | ------ | -------------------------------------------- |
| <mode>      | 工作模式           | 1      | 打开FTP会话                                  |
|             |                    | 2      | 读入FTP下载数据                              |
| <reqlength> | 请求读入的数据长度 | 1~1460 |                                              |
| <cnlength>  | 确认读入的数据长度 | 1~1460 | 可能小于<reqlength>。0表示没有数据可以读入。 |
| <error>     | 错误码             | 61     | 网络错误 net error                           |
|             |                    | 62     | DNS错误 DNS error                            |
|             |                    | 63     | 连接错误 connect error                       |
|             |                    | 64     | 超时 timeout                                 |
|             |                    | 65     | 服务器错误 server error                      |
|             |                    | 66     | 操作禁止 operation not allowed               |
|             |                    | 70     | 应答错误 reply error                         |
|             |                    | 71     | 用户错误 user error                          |
|             |                    | 72     | 口令错误 password error                      |
|             |                    | 73     | 类型错误 type error                          |
|             |                    | 74     | 保持错误 rest error                          |
|             |                    | 75     | 被动错误 passive error                       |
|             |                    | 76     | 主动错误 active error                        |
|             |                    | 77     | 操作错误 operate error                       |
|             |                    | 78     | 上传错误 upload error                        |
|             |                    | 79     | 下载错误 download error                      |
|             |                    | 80~84  | FTP SSL 连接错误                             |
|             |                    | 85     | 文件错误                                     |
|             |                    | 86     | 主动退出                                     |
