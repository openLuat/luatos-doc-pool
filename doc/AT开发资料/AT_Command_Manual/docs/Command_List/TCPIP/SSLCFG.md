## 配置TCP SSL参数：AT+SSLCFG

**注：本章命令合宙4G CAT1 EC716S系列平台模块(Air780EL系列& Air780ET系列& Air700EC系列)，只有_FS,_MS固件版本支持，其它固件版本不支持**

 

设置命令用来设置SSL版本，SSL加密算法（ciphersuites），安全等级（security level），CA 证书（Certificate Authority Certificate），客户端证书（client certificate）和客户端密钥（client key）。这些参数在SSL协议的握手过程中会用到。

 

语法规则：

| 命令类型 | 语法                                                  | 返回                                                         |
| -------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| 设置命令 | `AT+SSLCFG="sslversion",<n>[,<sslversion>]`           | 如果`<sslversion>`缺失，则查询`<n>`对应的SSL版本：<br>`+SSLCFG: "sslversion",<n>,<sslversion>` <br>OK <br>否则，设置`<n>`对应的SSL版本：<br>如果格式和参数正确，返回：<br>OK  <br>如果命令格式或参数错误，返回：<br>ERROR |
|          | `AT+SSLCFG="ciphersuite",<n>[,<ciphersuites>]`        | 如果`<ciphersuites>`缺失，则查询`<n>`对应的加密算法：`+SSLCFG: ciphersuite",<n>,<ciphersuites>` <br>OK<br>否则，设置`<n>`对应的加密算法：<br>如果格式和参数正确，返回：<br>OK  <br>如果目录格式或参数错误，返回：<br>ERROR |
|          | `AT+SSLCFG="cacert",<n>[,<cacertpath>]`               | 如果`<cacertpath>`参数缺失，则查询<n>对应的CA证书路径：<br>`+SSLCFG:"cacert",<n>,<cacertpath> `<br>OK<br>否则，设置<n>对应的CA证书路径：如果格式和参数正确，返回：<br>OK  <br>如果目录格式或参数错误，返回：<br>ERROR |
|          | `AT+SSLCFG="clientcert",<n>[,<client_cert_path>]`     | 如果<client_cert_path>参数缺失，则是查询`<n>`对应的客户端证书路径：<br>`+SSLCFG:"clientcert",<n>,<client_cert_path>` <br>OK<br>否则，设置`<n>`对应的客户端证书路径：如果格式和参数正确，返回：<br>OK  <br>如果命令格式或参数错误，返回：<br>ERROR |
|          | `AT+SSLCFG="clientkey",<n>[,<client_key_path>]`       | 如果`<client_key_path>`缺失，则是查询`<n>`对应的客户端密钥路径：<br>`+SSLCFG:"clientkey",<n>,<client_key_path>`<br> OK<br>否则，设置`<n>`对应的客户端密钥路径：如果格式和参数正确，返回：<br>OK  <br>如果命令格式或参数错误，返回：<br>ERROR |
|          | `AT+SSLCFG="seclevel",<n>[,<seclevel>]`               | 如果`<seclevel>`参数缺失，则是查询<n>相关的安全等级：<br>`+SSLCFG:"seclevel",<n>,<seclevel>`<br> OK <br>否则，设置`<n>`对应的安全等级：<br>如果格式和参数正确，返回：<br>OK  <br>如果命令格式或参数错误，返回：<br>ERROR |
|          | `AT+SSLCFG="hostname",<n>[,<hostname>]`               | 如果`<hostname>`参数缺失，则是查询`<n>`相关的域名：<br>`+SSLCFG:"hostname",<n>,<hostname><bt>` <br>OK<br>否则，设置`<n>`对应的主机名：<br>如果格式和参数正确，返回：<br>OK  <br>如果命令格式或参数错误，返回：<br>ERROR |
|          | `AT+SSLCFG="ignorelocaltime",<n>[,<ignoreltime>]`     | 如果`<ignorelocaltime>`缺失，则是查询<n>相关的证书过期时间检查这项的设置：<br>`+SSLCFG:"ignorelocaltime",<n>,<ignoreltime> `<br>OK<br>否则，设置`<n>`对应的证书过期时间检查参数：<br>如果格式和参数正确，返回：<br>OK <br> 如果命令格式或参数错误，返回：<br>ERROR |
|          | `AT+SSLCFG="negotiatetimeout",<n>[,<negotiate_time>]` | 如果<negotiate_time>参数缺失，则是查询`<n>`对应的最大SSL协商时间：<br>`+SSLCFG:"negotiatetimeout",<n>,<negotiate_time> `<br>OK<br>否则，设置`<n>`对应的最大SSL写上协商时间：<br>如果格式和参数正确，返回：<br>OK  <br>如果命令格式或参数错误，返回：<br>ERROR |
|          | `AT+SSLCFG="clientrandom",<n>[,<randbytes>]`          | 如果`<randbytes>`缺失，则是查询`<n>`相关的随机数：<br>`+SSLCFG:"clientrandom",<n>,<randbytes> `<br>OK<br>否则，设置`<n>`对应的随机数：<br>如果格式和参数正确，返回：<br>OK<br>如果命令格式或参数错误，返回：<br>ERROR |
|          | `AT+SSLCFG="premaster",<n>[,<premaster>]`             | 如果`<premaster>`缺失，则是查询`<n>`相关的`<premaster>：+SSLCFG:"premaster",<n>,<premaster> `<br>OK<br>否则，设置`<n>`对应的premaster：<br>如果格式和参数正确，返回：<br>OK <br>如果命令格式或参数错误，返回：<br>ERROR |
|          | `AT+SSLCFG="verifymode",<n>[,<verifymode>]`           | 如果`<verifymode>`缺失，则查询`<n>`相关的证书验证模式，此时返回：<br>`+SSLCFG:"verifymode",<n>,<verifymode> `<br>OK<br>否则，设置证书认证模式是根证书认证还是其他证书认证：如果格式和参数正确，返回：<br>OK  <br>如果命令格式或参数错误，返回：<br>ERROR |
|          | `AT+SSLCFG="XXXXX",<n>,`                              | 擦除相应的参数。"XXXXX"是指："sslversion"，"ciphersuite"，"cacert"等关键字。<br>**注意：`<n>`后一定要有逗号，如果`<n>`后面没有逗号，则只是查询。** |
| 测试命令 | AT+SSLCFG=?                                           | OK                                                           |
| 注意事项 | TCP SSL的功能示例，请参考本章后面的例子。             |                                                              |

 

参数定义：

| 参数                 | 定义                                             | 取值             | 对取值的说明                                                 |
| -------------------- | ------------------------------------------------ | ---------------- | ------------------------------------------------------------ |
| `<n>`                | SSL上下文 id                                     | 0~5,34,88,153    | 整数型。<br>TCP功能时与CIPSTART中的`<n>`绑定。<br>例如：当多链接中CIPSTART中设置链接号为1，则SSL上下文id也为1。<br>TCP单链接中SSL上下文id固定为0. <br>FTP功能时`<n>=34`（十进制）<br>MQTT功能时`<n>=88`（十进制）<br>HTTP功能时`<n>=153`（十进制） |
| `<sslversion>`       | SSL 版本                                         | 0                | SSL3.0                                                       |
|                      |                                                  | 1                | TLS1.0                                                       |
|                      |                                                  | 2                | TLS1.1                                                       |
|                      |                                                  | 3                | TLS1.12                                                      |
|                      |                                                  | 4                | ALL above                                                    |
| `<ciphersuites>`     | SSL ciphersuites                                 | 0X0035           | TLS_RSA_WITH_AES_256_CBC_SHA                                 |
|                      |                                                  | 0X002F           | TLS_RSA_WITH_AES_128_CBC_SHA                                 |
|                      |                                                  | 0X0005           | TLS_RSA_WITH_RC4_128_SHA                                     |
|                      |                                                  | 0X0004           | TLS_RSA_WITH_RC4_128_MD5                                     |
|                      |                                                  | 0X000A           | TLS_RSA_WITH_3DES_EDE_CBC_SHA                                |
|                      |                                                  | 0X003D           | TLS_RSA_WITH_AES_256_CBC_SHA256                              |
|                      |                                                  | 0XFFFF           | ALL above                                                    |
| `<cacertpath>`       | 被信任的CA 证书路径                              |                  | 字符串型                                                     |
| `<client_cert_path>` | 客户端证书路径                                   |                  | 字符串型                                                     |
| `<client_key_path>`  | 客户端密钥路径                                   |                  | 字符串型                                                     |
| `<seclevel>`         | 安全等级                                         | 0                | No authentication                                            |
|                      |                                                  | 1                | 服务器鉴权                                                   |
|                      |                                                  | 2                | 服务器鉴权和客户端鉴权（如果服务器要求的话）                 |
| `<hostname>`         | 主机名                                           |                  |                                                              |
| `<ignoreltime>`      | 该参数决定如何对待过期证书                       | 0                | 关心证书的过期时间                                           |
|                      |                                                  | 1                | 忽略证书的过期时间                                           |
| `<negotiate_time>`   | SSL协商阶段的最大时间                            | 10~300           | 单位：秒                                                     |
| `<clientrandom>`     | 随机数，十六进制数组成的字符串，支持56和64个字节 | 数字和字母的组合 | 字符串型，双引号可加可不加，数字的范围：0~9，字母的范围：ABCDEF（大小写不敏感）。例如56个字节的：101B12C3141516171F19202122232425262728293031323334353637 |
| `<premaster>`        | premaster                                        |                  |                                                              |
| `<verifymode>`       | 证书验证模式                                     | 0                | 根证书认证                                                   |
|                      |                                                  | 1                | 其他证书认证                                                 |
