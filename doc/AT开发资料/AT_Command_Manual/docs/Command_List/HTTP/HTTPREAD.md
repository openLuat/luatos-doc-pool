## 查询HTTP服务响应：AT+HTTPREAD

语法规则：

| 命令类型 | 语法                                    | 返回                                                         |
| -------- | --------------------------------------- | ------------------------------------------------------------ |
| 设置命令 | AT+HTTPREAD=<start_address>,<byte_size> | `+HTTPREAD:<date_len>`<br>`<data>`<br>OK                     |
| 执行命令 | AT+HTTPREAD                             | `+HTTPREAD:<date_len>`<br>`<data> `<br>OK  <br>读取 AT+HTTPACTION=0	或 AT+HTTPDATA 命令的所有响应数据。<br>执行命令用来将HTTP服务器的响应输出到UART或者输出准备好POST 到服务器的数据。 |
| 测试命令 | AT+HTTPREAD=?                           | `+HTTPREAD: (list of supported <start_address>s),(list of supported<byte_size>s) `<br>OK |

 

参数定义：

| 参数              | 定义                                       | 取值   | 对取值的说明 |
| ----------------- | ------------------------------------------ | ------ | ------------ |
| `<date_len>`      | 实际输出数据长度                           |        |              |
| `<data>`          | HTTP 服务器对AT+HTTPACTION=0命令的响应数据 |        |              |
| `<start_address>` | 输出数据的起点                             | 0~3356 | 单位:字节    |
| `<byte_size>`     | 输出数据的长度                             | 1~3356 | 单位:字节    |
