## 查询cid相关的上下文定义：AT+CGCONTRDP

设置命令返回`<cid>`相关的<bearer_id>, `<apn>`, <local_addr and subnet_mask>, <gw_addr>, <DNS_prim_addr>, <DNS_sec_addr>, <P-CSCF_prim_addr>, <P-CSCF_sec_addr>, <IM_CN_Signalling_Flag>和<LIPA_indication>。

 

语法规则：

| 命令类型 | 语法                   | 返回                                                         |
| -------- | ---------------------- | ------------------------------------------------------------ |
| 设置命令 | `AT+CGCONTRDP[=<cid>]` | `[+CGCONTRDP: <cid>,<bearer_id>,<apn>[,<local_addr>,<subnet_mask>[,<gw_addr>[,<DNS_prim_addr>[,<DNS_sec_addr>[,<P-CSCF_prim_addr>[,<P-CSCF_sec_addr>[,<IM_CN_Signalling_Flag>[,<LIPA_indication>]]]]]]]]] [<CR><LF>+CGCONTRDP: <cid>,<bearer_id>,<apn>[,<local_addr>,<subnet_mask>[,<gw_addr>[,<DNS_prim_addr>[,<DNS_sec_addr>[,<P-CSCF_prim_addr>[,<P-CSCF_sec_addr>[,<IM_CN_Signalling_Flag>[,<LIPA_indication>]]]]]]]] […]]` <br>OK |
| 测试命令 | AT+CGCONTRDP=?         | `+CGCONTRDP: (list of <cid>s associated with active contexts)` <br>OK |

 

参数定义:

| 参数                    | 定义                                                         | 取值 | 对取值的说明 |
| ----------------------- | ------------------------------------------------------------ | ---- | ------------ |
| `<cid>`                 | 定义了一个特定的PDP上下文。                                  |      | 整数型       |
| <bearer_id>             | 指定了一个承载，例如：EPS网中的EPS承载，UMTS/GPRS中的NSAPI承载。 |      | 整数型       |
| `<apn>`                 | Access Point Name，接入点名称，用来选择GGSN或外部分组数据网  |      | 字符串型     |
| <local_addr>            | 模块本地IP地址                                               |      | 字符串型     |
| <subnet_mask>           | 子网掩码                                                     |      | 字符串型     |
| <gw_addr>               | 网关IP地址                                                   |      | 字符串型     |
| <DNS_prim_addr>         | 主DNS服务器IP地址                                            |      | 字符串型     |
| <DNS_sec_addr>          | 辅DNS服务器IP地址                                            |      | 字符串型     |
| <P-CSCF_prim_addr>      | 主P-CSCF服务器IP地址                                         |      | 字符串型     |
| <P-CSCF_sec_addr>       | 辅P-CSCF服务器IP地址                                         |      | 字符串型     |
| <IM_CN_Signalling_Flag> | 整数型，定义PDP上下文是否仅与IM CN子系统最大值相关           | 0    | 否           |
|                         |                                                              | 1    | 是           |
| <LIPA_indication>       | 整数型，显示PDP上下文是否与LIPA PDN相关。本参数无法设置      | 0    | 否           |
|                         |                                                              | 1    | 是           |

 

 

举例：

| 命令(→)/返回(←) | 实例                                                         |
| --------------- | ------------------------------------------------------------ |
| →               | AT+CGCONTRDP=1                                               |
| ←               | +CGCONTRDP: 1,5,"cmiot","10.174.8.137","",,"211.138.180.4","211.138.180.5" <br>OK |
