## 下载文件(扩展)：AT+FTPEXTGET

语法规则：

| 命令类型 | 语法                                                         | 返回                                                         | 说明                                              |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------- |
| 设置命令 | AT+FTPEXTGET=<mode>                                          | OK                                                           | 当<mode>=0或1                                     |
|          | AT+FTPEXTGET=<mode>,<filename>                               | +FTPEXTGET:2,<totalLength> <br>OK                            | 当<mode>=2                                        |
|          | AT+FTPEXTGET=<mode>,<readpos>,<readlen>                      | +FTPEXTGET:3,<outputLength>…… //这里是输出到串口的数据 <br>OK | 当<mode>=3                                        |
|          | AT+FTPEXTGET=<mode>                                          | OK+FTPEXTGET: 4,<outputLength>//outputLength数据长度         | 当<mode>=4<br>AT+FTPEXTGET=4,outputLength//读数据 |
| 查询命令 | AT+FTPEXTGET?                                                | +FTPEXTGET: <status>[,<receivedLength>] <br>OK               |                                                   |
| 测试命令 | AT+FTPEXTGET=?                                               | OK                                                           |                                                   |
| URC上报  | +FTPEXTGET:1,0                                               | <mode>=1且FTPEXTGET结束，会有如此上报                        |                                                   |
|          | +FTPEXTGET:1,<error>                                         | <mode>=1且FTPEXTGET出错，会有如此上报。错误码<error>定义请参考AT+FTPGET 错误码<error>定义 |                                                   |
|          | +FTPEXTGET:2,<totalLength>                                   | <mode>=2                                                     |                                                   |
|          | +FTPEXTGET:3,<outputLength>                                  | <mode>=3                                                     |                                                   |
|          | +FTPEXTGET:4,<outputLength>                                  | <mode>=4                                                     |                                                   |
| 注意事项 | 1） 当FTPEXTPUT<mode>=1时，不可使用本命令<br>2） 如果文件大小(<receivedLength>)<300KB，可以使用这个命令；如果文件大小(<receivedLength>)>=300KB，请使用缺省的FTPGET method (AT+FTPEXTGET=0)<br>3） 本命令的使用方法请参考本章最后一部分：使用方法举例<br>4） <mode>=4仅适用于合宙 4G CAT1 模块（Air780E /Air600E系列）>=V1106版本支持 |                                                              |                                                   |

 

参数定义：

| 参数             | 定义                                 | 取值    | 对取值的说明                                                 |
| ---------------- | ------------------------------------ | ------- | ------------------------------------------------------------ |
| <mode>           | 工作模式                             | 0       | 使用缺省的FTPGET方法                                         |
|                  |                                      | 1       | 使用扩展的FTPGET方法                                         |
|                  |                                      | 2       | 保存下载的数据到文件中                                       |
|                  |                                      | 3       | 输出下载的数据到串口                                         |
|                  |                                      | 4       | 流式获取数据                                                 |
| <filename>       | 文件名                               |         | 字符串型，最长64个字符。注:只需指定文件名，不要指定路径，因为保存的路径是确定的C:/USER/FTP |
| <totalLength>    | 保存到文件的所有数据长度，用于mode 2 | <302512 | 单位：字节                                                   |
| <outputLength>   | 输出到串口的数据长度，用于mode 3或4  | <302512 | 单位：字节                                                   |
| <readpos>        | 读取文件数据的起始位置，用于mode 3   |         | 0                                                            |
| <readlen>        | 读取长度，用于mode 3                 |         | 单位：字节                                                   |
| <status>         | FTPEXTGET的状态                      | 0       | 不在FTPEXTGET过程中                                          |
|                  |                                      | 1       | 处于FTPEXTGET过程                                            |
| <receivedLength> | 下载的数据的长度                     |         | 单位：字节                                                   |
| <error>          | 错误码                               |         | 与AT+FTPGET命令的<error>定义相同                             |
