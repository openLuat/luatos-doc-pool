## 设置HTTP参数值：AT+HTTPPARA

语法规则：

| 命令类型 | 语法                                          | 返回                                                         |
| -------- | --------------------------------------------- | ------------------------------------------------------------ |
| 设置命令 | `AT+HTTPPARA=<HTTPParamTag>,<HTTPParamValue>` | OK                                                           |
| 查询命令 | AT+HTTPPARA?                                  | `+HTTPPARA: list of <HTTPParamTag>:<HTTPParamValue>)` <br>OK |
| 测试命令 | AT+HTTPPARA=?                                 | +HTTPPARA: "HTTPParamTag"," HTTPParamValue" <br>OK           |

 

参数定义：

| 参数                                                         | 定义                                                         | 取值                                                         | 对取值的说明                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `<HTTPParamTag> `:HTTP参数，包括：                           |                                                              |                                                              |                                                              |
| "CID"                                                        | 承载上下文号码(必选参数)                                     | 1~3                                                          |                                                              |
| "URL"                                                        | HTTP 或HTTPS URL(必选参数) <br>**注：同时支持HTTPS 和HTTP URL** | "http://server/path:tcpPort <br>"或：<br>"https://server/path:tcpPort "<br>最大长度500个字节 | Server: FQDN or IP-address<br>Path: path of file or directory<br>tcpPort: 如果参数省略，将服务连接到<br> HTTP默认端口 80。<br>参考"IETF-RFC 261 |
| "UA"                                                         | 应用程序必须设置用户代理来识别移动终端。通常操作系统和软件版本信息在设置时都会携带浏览器标识符。 | -                                                            | 默认值为:AM_MODULE                                           |
| "PROIP"                                                      | HTTP 代理服务器的 IP 地址                                    | -                                                            |                                                              |
| "PROPORT"                                                    | HTTP 代理服务器的PORT                                        | -                                                            |                                                              |
| "REDIR"                                                      | 作为 HTTP 客户端时用此标志控制重定向机制。如果此标记设置为 1，当服务器发送重定向码(范围 30x)时，客户端自动发送新的 HTTP 请求 | -                                                            | 默认值为 0(无定向)                                           |
| "BREAK"                                                      | HTTP 方法"GET"的参数，整数型                                 | -                                                            | 获取从断点到结束点的部分数据，注意不是所有的 HTTP 服务器都支持`<BREAK>`参数。BREAK最小值是0。 |
| "BREAKEND"                                                   | 和"BREAK"一起使用，用于断点续传功能。整数型。                | -                                                            | 如果"BREAKEND"大于"BREAK"，续传的范围从"BREAKEND"到"BREAK"。<br>如果"BREAKEND"小于"BREAK"，续传的范围从"BREAK"到文件结尾。<br>如果"BREAKEND"和"BREAK"均为 0，将不会续传。 |
| "TIMEOUT"                                                    | 设置http请求的超时时间                                       | -                                                            | 单位是秒，默认120秒                                          |
| "CONTENT"                                                    | 设置发送的请求实体数据数据类型                               | -                                                            | 即Content-Type                                               |
| "USER_DEFINED"                                               | 用户自定义参数，为了兼容合宙2G模块                           |                                                              | 用户自定义参数的取值。例如：AT+HTTPPARA="USER_DEFINED","Content-type: json-user-define"<br>**注**：如果需要设置多条用户自定义参数，则一条一条地输入。后面输入的不会覆盖以前的。 |
| "USERDATA"                                                   | 用户自定义参数，作用同"USER_DEFINED"，为了兼容SIMCOM模块     |                                                              | 用户自定义参数的取值。例如：AT+HTTPPARA="USERDATA","Content-type: json-user-define"<br>**注**:如果想设置多条用户定义参数，则多条参数之间可以用\r\n连接。例如：<br>AT+HTTPPARA="USERDATA","Content-Type:application/json\r\nAPPKEY:FW"<br>在MCU程序中需要将\r\n写成[\\r\\n](file:///\\r\\n) 值得一提的是有些PC串口工具，例如SSCOM，会将\r和\n当做控制字符处理，所以也需要将\r\n写成[\\r\\n](file:///\\r\\n)而另外一些工具，例如XCOM，不会将\r和\n当做控制字符处理，所以直接输入\r\n |
| `<HTTPParamValue>` : 即`<HTTPParamTag>`的取值。<br> 注："USER_DEFINED" 和"USERDATA"中内嵌的双引号，用\22表达。 |                                                              |                                                              |                                                              |

 

举例：

| 命令（→）/返回（←） | 实例                                                         | 解释和说明 |
| ------------------- | ------------------------------------------------------------ | ---------- |
| →                   | AT+HTTPPARA?                                                 |            |
| ←                   | +HTTPPARA:  <br>CID: 1<br>URL: <br>UA: AM_MODULE<br>PROIP: 0.0.0.0<br>PROPORT: 0<br>REDIR: 0<br>BREAK: 0<br>BREAKEND: 0<br>TIMEOUT: 120<br>CONTENT:<br> USERDATA: <br>OK |            |

 
