## E-UTRAN EPS 网络注册状态：AT+CEREG

设置命令打开或关闭+CEREG的URC上报，URC上报内容如下：

 

设置<n>=1，当在E-UTRAN网的EPS注册状态发生变化时，主动上报+CEREG: <stat>

设置<n>=2，当在E-UTRAN网的EPS注册状态或驻网小区发生变化时，主动上报+CEREG: <stat>[,<tac>,<ci>,<act>]

设置<n>=3，当在E-UTRAN网的EPS注册状态或驻网小区发生变化时，主动上报+CEREG: <stat>[,<tac>,<ci>,<act>[,<cause_type>,<reject_cause>]]

 

语法规则：

| 命令类型 | 语法                                                         | 返回                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 设置命令 | AT+CEREG=<n>                                                 | OK                                                           |
| 查询命令 | AT+CEREG?                                                    | +CEREG: <n>,<stat>[,[<tac>],[<ci>],[<AcT>[,<cause_type>,<reject_cause>]]] <br>OK |
| 测试命令 | AT+CEREG=?                                                   | +CEREG: (list of supported <n>s) <br>OK                      |
| URC上报  | +CEREG: <stat>                                               | <n>=1，当在E-UTRAN网的EPS注册状态发生变化时                  |
|          | +CEREG: <stat>[,[<tac>],[<ci>],[<AcT>]]                      | <n>=2，当在E-UTRAN网的EPS注册状态或驻网小区发生变化时        |
|          | +CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,,]]                  | <n>=3，当在E-UTRAN网的EPS注册状态或驻网小区发生变化时        |
|          | +CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,,[,[<ActiveTime>],[<Periodic-TAU>]]]] | <n>=4，对于请求PSM的UE，使能网络注册状态主动上报、位置信息和网络定时器配置主动上报 |
|          | +CEREG:<stat>[,[<tac>],[<ci>],[<AcT>][,[<cause_type>],[<reject_cause>][,[<Active-Time>],[<Periodic-TAU>]]]] | <n>=5，对于请求PSM的UE，使能网络注册状态主动上报、位置信息、注册失败原因和 网络定时器配置主动上报，上报内容为 |

 

参数定义:

| 参数           | 定义                           | 取值 | 对取值的说明                                                 |
| -------------- | ------------------------------ | ---- | ------------------------------------------------------------ |
| <n>            | URC上报状态                    | 0    | 禁止上报网络注册状态URC +CEREG                               |
|                |                                | 1    | 允许主动上报+CEREG: <stat>                                   |
|                |                                | 2    | 允许主动上报+CREG:<stat>[,<lac>,<ci>]                        |
|                |                                | 3    | 允许主动上报+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,,]]      |
|                |                                | 4    | +CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,,[,[],[<Periodic-TAU>]]]] |
|                |                                | 5    | +CEREG:<stat>[,[<tac>],[<ci>],[<AcT>][,[],[<reject_cause>][,[],[<Periodic-TAU>]]]] |
| <stat>         | 当前网络注册状态               | 0    | 未注册；ME 当前没有搜索要注册业务的新运营商                  |
|                |                                | 1    | 已注册，本地网                                               |
|                |                                | 2    | 未注册，但 ME 正在搜索要注册业务的新运营商                   |
|                |                                | 3    | 注册被拒绝                                                   |
|                |                                | 4    | 未知(超出E-UTRAN网覆盖范围)                                  |
|                |                                | 5    | 注册漫游网                                                   |
|                |                                | 6    | 注册归属地"SMS only"业务                                     |
|                |                                | 7    | 注册漫游地"SMS only"业务                                     |
|                |                                | 8    | 仅附着紧急承载业务                                           |
|                |                                | 9    | 注册归属地"CSFB not preferred"业务                           |
|                |                                | 10   | 注册漫游地"CSFB not preferred"业务                           |
|                |                                | 11   | 仅紧急业务可用                                               |
| <tac>          | 跟踪区号                       | -    | 字符串型，16进制数                                           |
| <ci>           | 小区id                         | -    | 字符串型，16进制数                                           |
| <act>          | 接入模式                       | 0    | GSM                                                          |
|                |                                | 1    | GSM Compact                                                  |
|                |                                | 2    | UTRAN                                                        |
|                |                                | 3    | GSM w/EGPRS                                                  |
|                |                                | 4    | UTRAN w/HSDPA                                                |
|                |                                | 5    | UTRAN w/HSUPA                                                |
|                |                                | 6    | UTRAN w/HSDPA and HSUPA                                      |
|                |                                | 7    | E-UTRAN                                                      |
|                |                                | 8    | UTRAN HSPA+(CAT1 模块)EC-GSM-IoT(CAT4模块)                   |
| <cause_type>   | 整数型，定义<reject_cause>类型 | 0    | 显示<reject_cause>包括一个EMM 原因值（请参考3GPP TS 24.301 Annex A） |
|                |                                | 1    | 显示<reject_cause>值由厂家定义                               |
| <reject_cause> | 整数型，定义注册失败原因       |      | 此值的类型由<cause_type>定义                                 |

 
