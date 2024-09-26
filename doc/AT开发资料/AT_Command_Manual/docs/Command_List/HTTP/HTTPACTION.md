## HTTP方式激活：AT+HTTPACTION

语法规则：

| 命令类型 | 语法                     | 返回                                                         |
| -------- | ------------------------ | ------------------------------------------------------------ |
| 设置命令 | `AT+HTTPACTION=<method>` | OK<br>后面紧跟Unsolicited Result Code:<br>`+HTTPACTION: <Method>,<StatusCode>,<DataLen>` |
|          |                          | 或如果错误与 ME 功能相关，则返回：<br>`+CME ERROR: <err>`<br>后面紧跟Unsolicited Result Code:<br>`+HTTPACTION: <Method>,<StatusCode>,<DataLen>` |
| 测试命令 | AT+HTTPACTION=?          | +HTTPACTION: (0-2) <br>OK                                    |

 

参数定义：

| 参数           | 定义                                               | 取值 | 对取值的说明                                                 |
| -------------- | -------------------------------------------------- | ---- | ------------------------------------------------------------ |
| `<Method>`     | HTTP 方法说明                                      | 0    | GET                                                          |
|                |                                                    | 1    | POST                                                         |
|                |                                                    | 2    | HEAD                                                         |
| `<DataLen>`    | 得到的数据长度                                     | -    | 整数型                                                       |
| `<StatusCode>` | HTTP状态码，由远端服务器响应， 参考TTP1.1(RFC2616) | 100  | 继续（Continue）                                             |
|                |                                                    | 101  | 交换协议(Switching Protocols)                                |
|                |                                                    | 200  | 确定(OK)                                                     |
|                |                                                    | 201  | 已创建(Created)                                              |
|                |                                                    | 202  | 已接受(Accepted)                                             |
|                |                                                    | 203  | 非权威消息(Non-Authoritative Information)                    |
|                |                                                    | 204  | 无内容(No Content)                                           |
|                |                                                    | 205  | 重置内容(Reset Content)                                      |
|                |                                                    | 206  | 部分内容(Partial Content)                                    |
|                |                                                    | 300  | 多重选择(Multiple Choices)                                   |
|                |                                                    | 301  | 永久删除(Moved Permanently)                                  |
|                |                                                    | 302  | 找到(Found )                                                 |
|                |                                                    | 303  | 参考其他(See Other)                                          |
|                |                                                    | 304  | 未修改(Not Modified)                                         |
|                |                                                    | 305  | 使用代理服务器(Use Proxy)                                    |
|                |                                                    | 307  | 临时重定向(Temporary Redirect )                              |
|                |                                                    | 400  | 错误请求(Bad Request)                                        |
|                |                                                    | 401  | 未授权(Unauthorized)                                         |
|                |                                                    | 402  | 付费请求(Payment Required)                                   |
|                |                                                    | 403  | 禁止(Forbidden)                                              |
|                |                                                    | 404  | 找不到(Not Found)                                            |
|                |                                                    | 405  | 方法不被允许(Method not Allowed)                             |
|                |                                                    | 406  | 不可接受(Not Acceptable)                                     |
|                |                                                    | 407  | 要 求 进 行 代 理 身 份 认 证 (Proxy AuthenticationRequired) |
|                |                                                    | 408  | 请求超时 (Request Time-out)                                  |
|                |                                                    | 409  | 冲突(Conflict)                                               |
|                |                                                    | 410  | 所请求资源不在服务器上有效，且不知道转发地址(Gone)           |
|                |                                                    | 411  | 需要输入长度(Length Required)                                |
|                |                                                    | 412  | 前提条件失败 (Precondition Failed)                           |
|                |                                                    | 413  | 请求实体太大(Request Entity Too Large)                       |
|                |                                                    | 414  | 请求URI太长(Request-URI Too Large)                           |
|                |                                                    | 415  | 媒体类型不支持(Unsupported Media Type)                       |
|                |                                                    | 416  | 所 请 求 的 范 围 无 法 满 足(Requested range notsatisfiable) |
|                |                                                    | 417  | 执行失败(Expectation Failed)                                 |
|                |                                                    | 500  | 内部服务器错误(Internal Server Error)                        |
|                |                                                    | 501  | 未执行 (Not Implemented)                                     |
|                |                                                    | 502  | 网关错误(Bad Gateway)                                        |
|                |                                                    | 503  | 服务不可用(Service Unavailable)                              |
|                |                                                    | 504  | 网关超时(Gateway Time-out)                                   |
|                |                                                    | 505  | HTTP 版本不支持(HTTP Version not supported)                  |
|                |                                                    | 600  | 非 HTTP PDU 格式(Not HTTP PDU)                               |
|                |                                                    | 601  | 网络错误(Network Error)                                      |
|                |                                                    | 602  | 内存不足(No memory)                                          |
|                |                                                    | 603  | DNS 错误(DNS Error)                                          |
|                |                                                    | 604  | 栈忙(Stack Busy)                                             |
|                |                                                    | 605  | SSL建立通道失败                                              |
|                |                                                    | 606  | SSL通讯警告错误                                              |
