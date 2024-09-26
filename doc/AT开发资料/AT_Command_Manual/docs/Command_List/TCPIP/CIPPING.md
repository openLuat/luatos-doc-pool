## Ping回声请求命令:AT+CIPPING

语法规则：

| 命令类型 | 语法                                                         | 返回和说明                                                   |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 设置命令 | `AT+CIPPING=<IPaddr>[,<retryNum>[,<dataLen>[,<timeout>[,<ttl>]]]]` | `+CIPPING: <replyId>,<Ip Address>,<replyTime>,<ttl>[<CR><LF> +CIPPING: <replyId>,<Ip Address>,<replyTime>,<ttl> [...]]`  <br>OK |
| 查询命令 | AT+CIPPING?                                                  | `+CIPPING: <retryNum>,<dataLen>,<timeout>,<ttl>` <br>OK      |
| 测试命令 | AT+CIPPING=?                                                 | `+CIPPING: (list of supported <retryNum>s),(list of supported <dataLen>s),(list of supported <timeout>s),(list of supported <ttl>s)  `<br>OK |
| 注意事项 | **1.** 发送PING命令之前，需激活GPRS PDP上下文。<br>**2.** 当发送PING到时无回应，那么返回的信息则显示`<replyTime>`=600 并且`<ttl>`=255。<br>**3.** 执行本命令时，如果GPRS PDP上下文由于某种原因被去激活了，例如掉网，那么本命令立即终止执行。 |                                                              |

 

参数定义：

| 参数           | 定义                                        | 取值       | 对取值的说明                                                 |
| -------------- | ------------------------------------------- | ---------- | ------------------------------------------------------------ |
| `<IPaddr>`     | PING的目标服务器地址。IP地址或域名都支持    | ip address |                                                              |
| Domain name    |                                             |            |                                                              |
| `<retryNum>`   | 需要发送的PING的数量                        | 1-100      | 缺省值:4                                                     |
|                |                                             | 0          | 可以不停的进行ping，并且最大的ping数量可以达到0xffffffff个>=V1120版本支持 |
| `<dataLen>`    | PING请求的长度                              | 0-1024     | 缺省值:32                                                    |
| `<timeout>`    | The timeout waiting for a single Echo Reply | 1-600      | 单位：100 ms                                                 |
| `<ttl>`        | time to live                                | 1-255      | 缺省值:64                                                    |
| `<replyId>`    | Echo Reply serial number                    |            |                                                              |
| `<Ip Address>` | IP Address of the remote host               |            |                                                              |
| `<replyTime>`  | time to receive the response                |            | 单位：1ms                                                    |

 

举例：

| 命令（→）/  返回（←） | 实例                                                         | 解释和说明                                                   |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| →                     | AT+CSTT                                                      |                                                              |
| ←                     | OK                                                           |                                                              |
| →                     | AT+CIICR                                                     |                                                              |
| ←                     | OK                                                           |                                                              |
| →                     | AT+CIFSR                                                     |                                                              |
| ←                     | 10.207.9.213                                                 |                                                              |
| →                     | AT+CIPPING="www.baidu.com"                                   |                                                              |
| ←                     | +CIPPING: 1,"36.152.44.96",35,54<br>+CIPPING: 2,"36.152.44.96",20,54<br>+CIPPING: 3,"36.152.44.96",20,54<br>+CIPPING: 4,"36.152.44.96",35,54 <br>OK |                                                              |
| →                     | AT+CIPPING="www.baidu.com",0                                 | 可以不停的进行ping，并且最大的ping数量可以达到0xffffffff个<br>>=V1120版本支持 |
| ←                     | +CIPPING: 1,"112.80.248.76",40,54<br>+CIPPING: 2,"112.80.248.76",45,54<br>+CIPPING: 3,"112.80.248.76",35,54<br>+CIPPING: 4,"112.80.248.76",35,54<br>+CIPPING: 5,"112.80.248.76",40,54<br>+CIPPING: 6,"112.80.248.76",35,54<br>... |                                                              |
