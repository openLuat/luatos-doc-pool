## 域名解析：AT+CDNSGIP

语法规则：

| 命令类型 | 语法                     | 返回和说明                                                   |
| -------- | ------------------------ | ------------------------------------------------------------ |
| 设置命令 | AT+CDNSGIP=<domain name> | 如果命令正确，而且域名解析成功，响应：<br>OK<br> +CDNSGIP: 1, <domain name>,<IPaddress> <br>如果命令正确，但域名解析失败，响应：<br>OK <br>+CDNSGIP:0,<dns error code><br> 如果命令语法错误，响应：<br>ERROR |
| 测试命令 | AT+CDNSGIP=?             | 返回：<br>OK                                                 |

 

参数定义：

| 参数             | 定义                  | 取值 | 对取值的说明                                  |
| ---------------- | --------------------- | ---- | --------------------------------------------- |
| <domain name>    | Internet 上注册的域名 | -    | 字符串参数(字符串需要加引号)，不超过128个字节 |
| <IPaddress>      | 域名对应的IP地址      | -    | 字符串参数(字符串需要加引号)                  |
| <dns error code> | DNS相关的错误码       | 10   | GENERAL ERROR                                 |
|                  |                       | 11   | MAX RETRIES                                   |
|                  |                       | 12   | NO SERVER ADDR                                |
|                  |                       | 13   | NO MEMORY                                     |
|                  |                       | 14   | INVALID NAME                                  |
|                  |                       | 15   | INVALID RESP                                  |
|                  |                       | 其他 | 一些其他的错误代码                            |
