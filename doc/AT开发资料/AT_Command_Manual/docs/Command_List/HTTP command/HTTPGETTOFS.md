## 下载文件并保存到文件系统中：AT+HTTPGETTOFS

**注：本命令EC618平台系列模块（Air780E系列）软件版本=V1148版本支持**

语法规则：

| 命令类型 | 语法                                                 | 返回                                                       |      |
| -------- | ---------------------------------------------------- | ---------------------------------------------------------- | ---- |
| 设置命令 | AT+HTTPGETTOFS=<loc>,<filename>                      | OK                                                         | 成功 |
|          |                                                      | ERROR                                                      | 失败 |
| 查询命令 | AT+HTTPGETTOFS?                                      | +HTTPGETTOFS: <br><status>,<writelen>,<totalLength> <br>OK |      |
| URC上报  | +HTTPGETTOFS:<响应码>,<writelen>                     | +HTTPGETTOFS:<HTTP响应码>，<writelen>                      |      |
| 测试命令 | AT+HTTPGETTOFS=?                                     | OK                                                         |      |
| 注意事项 | 如果两次下载都用同一个文件名，上次下载的内容会被覆盖 |                                                            |      |

 

参数定义：

| 参数          | 定义                       | 取值 | 对取值的说明                        |
| ------------- | -------------------------- | ---- | ----------------------------------- |
| <status>      | 工作模式                   | 0    | 不在HTTPGETTOFS过程                 |
|               |                            | 1    | 处于HTTPGETTOFS过程                 |
| <loc>         | 文件保存的位置。           | 0    | 保存于ROM，文件夹固定为"/USER/HTTP" |
| <filename>    | 文件名                     |      | 字符串型，最长64个字符              |
| <writelen>    | 当前保存到文件系统多少数据 |      |                                     |
| <totalLength> | 总共保存到文件系统多少数据 |      |                                     |
| <error>       | 错误码                     |      | HTTP错误码                          |
