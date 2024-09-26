## 设置TCP保活（keep-alive）参数:AT+CIPTKA

语法规则：

| 命令类型 | 语法                                                         | 返回和说明                                                   |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 设置命令 | `AT+CIPTKA=<mode>[,<keepIdle>[,<keepInterval>[,<keepCount>]]]` | OK                                                           |
| 查询命令 | AT+CIPTKA?                                                   | `+CIPTKA:<mode>,<keepIdle>,<keepInterval>,<keepCount>` <br>OK |
| 测试命令 | AT+CIPTKA=?                                                  | `+CIPTKA:(listofsupported<mode>s),(listofsupported<keepIdle>s),(listofsupported<keepInterval>s),(listofsupported<keepCount>s)` <br>OK |

 

参数定义：

| 参数             | 定义                                                         | 取值    | 对取值的说明           |
| ---------------- | ------------------------------------------------------------ | ------- | ---------------------- |
| `<mode>`         | 是否开启TCP保活（keep-alive）                                | 0       | 关闭                   |
|                  |                                                              | 1       | 开启                   |
| `<keepIdle>`     | 在`<keepIdle>`时间内链接上无任何数据交互，则发送初始保活探针（initial keep-alive probe） | 30~7200 | 单位为秒，缺省值为7200 |
| `<keepInterval>` | 保活探针重传的间隔时间                                       | 30~600  | 单位为秒，缺省值为75   |
| `<keepCount>`    | 发送保活探针的最大数量                                       | 1~9     | 单位为次，缺省值为9    |
