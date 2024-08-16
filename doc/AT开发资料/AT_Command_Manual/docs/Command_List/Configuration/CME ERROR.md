## 错误码描述：+CME ERROR:<err>

| 数字型<err>取值 | 冗长方式的<err>取值                           | 解释                              |
| --------------- | --------------------------------------------- | --------------------------------- |
| 常见错误        |                                               |                                   |
| 0               | phone failure                                 | 手机故障                          |
| 1               | no connection to phone                        | 未连接到手机                      |
| 2               | phone-adaptor link reserved                   | 预留手机适配器链路                |
| 3               | operation not allowed                         | 不允许操作                        |
| 4               | operation not supported                       | 不支持操作                        |
| 5               | PH-SIM PIN required                           | 需要PH-SIM卡的PIN                 |
| 6               | PH-FSIM PIN required                          | 需要PH-FSIM的PIN                  |
| 7               | PH-FSIM PUK required                          | 需要PH-FSIM的PUK                  |
| 10              | SIM not inserted                              | 没有插入SIM卡                     |
| 11              | SIM PIN required                              | 需要SIM卡的PIN                    |
| 12              | SIM PUK required                              | 需要SIM卡的PUK                    |
| 13              | SIM failure                                   | SIM卡故障                         |
| 14              | SIM busy                                      | SIM卡遇忙                         |
| 15              | SIM wrong                                     | SIM错误                           |
| 16              | incorrect password                            | 密码无效                          |
| 17              | SIM PIN2 required                             | 需要SIM卡的PIN2                   |
| 18              | SIM PUK2 required                             | 需要SIM卡的PUK2                   |
| 20              | memory full                                   | 存储已满                          |
| 21              | invalid index                                 | 索引无效                          |
| 22              | not found                                     | 未发现                            |
| 23              | memory failure                                | 存储故障                          |
| 24              | text string too long                          | 文本字符串过长                    |
| 25              | invalid characters in text string             | 文本字符串中的字符无效            |
| 26              | dial string too long                          | 拨号字符串过长                    |
| 27              | invalid characters in dial string             | 拨号字符串中的字符无效            |
| 30              | no network service                            | 无网络业务                        |
| 31              | network timeout                               | 网络超时                          |
| 32              | network not allowed - emergency calls only    | 网络不允许－只适用于紧急呼叫      |
| 40              | network personalization PIN required          | 需要网络个性化PIN                 |
| 41              | network personalization PUK required          | 需要网络个性化PUK                 |
| 42              | network subset personalization PIN required   | 需要网络子集个性化PIN             |
| 43              | network subset personalization PUK required   | 需要网络子集个性化PUK             |
| 44              | service provider personalization PIN required | 需要服务供应商个性化PIN           |
| 45              | service provider personalization PUK required | 需要服务供应商个性化PUK           |
| 46              | corporate personalization PIN required        | 需要公司个性化PIN                 |
| 47              | corporate personalization PUK required        | 需要公司个性化PUK                 |
| 48              | hidden key required                           | 需要输入隐藏的密码                |
| 49              | EXE_NOT_SURPORT                               |                                   |
| 50              | EXE_FAIL                                      | （适用于cat1 模块）               |
| 50              | Invalid Param                                 | 无效参数（适用于cat4 模块）       |
| 51              | NO MEMORY                                     | 内存不足（适用于cat1 模块）       |
| 52              | OPTION NOT SURPORT                            | 选项不支持（适用于cat1 模块）     |
| 53              | parameters are invalid                        | 无效参数（适用于cat1 模块）       |
| 54              | EXT_REG_NOT_EXIT                              | （适用于cat1 模块）               |
| 55              | EXT_SMS_NOT_EXIT                              | （适用于cat1 模块）               |
| 56              | EXT_PBK_NOT_EXIT                              | （适用于cat1 模块）               |
| 57              | EXT_FFS_NOT_EXIT                              | （适用于cat1 模块）               |
| 58              | INVALID_COMMAND_LINE                          | （适用于cat1 模块）               |
| 59              | ITF_DIFFERENT                                 | （适用于cat1 模块）               |
| 60              | BURN_FLASH_FAIL                               | （适用于cat1 模块）               |
| 61              | TFLASH NOT EXIST                              | TF卡不存在（适用于cat1 模块）     |
| 62              | FILE NOT EXIST                                | 文件不存在（适用于cat1 模块）     |
| 63              | FILE TOO LARGE                                | 文件太大（适用于cat1 模块）       |
| 96              | INVALID DATE OR TIME                          | 无效日期或时间（适用于cat1 模块） |
| 97              | DIR CREATE FAIL                               | 创建文件夹失败（适用于cat1 模块） |
| 98              | DIR NOT EXIST                                 | 文件夹不存在（适用于cat1 模块）   |
| 99              | NOT IMPLEMENTED                               | 不可执行（适用于cat1 模块）       |
| 100             | unknown                                       | 未知                              |
| 103             | Illegal MS                                    | 非法MS                            |
| 106             | Illegal ME                                    | 非法ME                            |
| 107             | GPRS services not allowed                     | 不允许GPRS业务                    |
| 111             | PLMN not allowed                              | 不允许PLMN                        |
| 112             | Location area not allowed                     | 不允许位置区                      |
| 113             | Roaming not allowed in this location area     | 该位置区不允许漫游                |
| 132             | service option not supported                  | 不支持业务选择                    |
| 133             | requested service option not subscribed       | 未描述业务选择请求                |
| 134             | service option temporarily out of order       | 业务选择暂时无连接                |
| 148             | unspecified GPRS error                        | GPRS错误未指明                    |
| 149             | PDP authentication failure                    | PDP 鉴权失败                      |
| 150             | invalid mobile class                          | 移动类别无效                      |
| 151             | AT command timeout                            | AT命令超时                        |
| 181             | UNSUPPORTED QCI VALUE                         | 不支持CQI                         |
| 214             | SS_UNKNOWN_SUBSCRIBER                         |                                   |
| 222             | SS_ILLEGAL_SUBSCRIBER                         |                                   |
| 223             | SS_BRERSERV_NOT_PROV                          |                                   |
| 224             | SS_TELESERV_NOT_PROV                          |                                   |
| 225             | SS_ILLEGAL_EQUIPMENT                          |                                   |
| 226             | SS_CALL_BARRED                                |                                   |
| 229             | SS_ILLEGAL_OPERATION                          |                                   |
| 230             | SS_ERROR_STATUS                               |                                   |
| 231             | SS_NOT_AVAILABLE                              |                                   |
| 232             | SS_SUBS_VIOLATION                             |                                   |
| 233             | SS_INCOMPATIBILITY                            |                                   |
| 234             | SS_FACILITY_NOT_SUPPORTED                     |                                   |
| 240             | SS_ABSENT_SUBSCRIBER                          |                                   |
| 247             | SS_SYSTEM_FAILURE                             |                                   |
| 248             | SS_DATA_MISSING                               |                                   |
| 249             | SS_UNEXPECTED_DATA_VALUE                      |                                   |
| 250             | SS_PWD_REGISTRATION_FAILURE                   |                                   |
| 251             | SS_NEGATIVE_PWD_CHECK                         |                                   |
| 256             | SS_NUMOF_PWD_ATTEMPT_VIOL                     |                                   |
| 264             | SIM VERIFY FAIL                               | （适用于cat1 模块）               |
| 265             | SIM UNBLOCK FAIL                              | （适用于cat1 模块）               |
| 266             | SIM CONDITION NO FULLFILLED                   | （适用于cat1 模块）               |
| 267             | SS_POSITION_METHOD_FAILURE                    | （适用于cat4 模块）               |
| 267             | SIM UNBLOCK FAIL NO LEFT                      | （适用于cat1 模块）               |
| 268             | SIM VERIFY FAIL NO LEFT                       | （适用于cat1 模块）               |
| 269             | SIM INVALID PARAMETER                         | （适用于cat1 模块）               |
| 270             | SIM UNKNOW COMMAND                            | （适用于cat1 模块）               |
| 271             | SIM WRONG CLASS                               | （适用于cat1 模块）               |
| 272             | SIM TECHNICAL PROBLEM                         | （适用于cat1 模块）               |
| 273             | SIM CHV NEED UNBLOCK                          | （适用于cat1 模块）               |
| 274             | SIM NOEF SELECTED                             | （适用于cat1 模块）               |
| 275             | SIM FILE UNMATCH COMMAND                      | （适用于cat1 模块）               |
| 276             | SIM CONTRADICTION CHV                         | （适用于cat1 模块）               |
| 277             | SIM CONTRADICTION INVALIDATION                | （适用于cat1 模块）               |
| 278             | SIM MAXVALUE REACHED                          | （适用于cat1 模块）               |
| 279             | SIM PATTERN NOT FOUND                         | （适用于cat1 模块）               |
| 280             | SIM FILEID NOT FOUND                          | （适用于cat1 模块）               |
| 281             | SIM STK BUSY                                  | （适用于cat1 模块）               |
| 282             | SIM UNKNOW                                    | （适用于cat1 模块）               |
| 283             | SIM PROFILE ERROR                             | （适用于cat1 模块）               |
| 284             | SS_UNKNOWN_ALPHABET                           |                                   |
| 285             | SS_USSD_BUSY                                  |                                   |
| 323             |                                               | Cat1模块                          |
| 339             | SS_MAXMPTY_CALLS_EXCEEDED                     |                                   |
| 340             | SS_RESOURCES_NOT_AVAILABLE                    |                                   |
| 501             | WIFI labtool reture error                     |                                   |
| 502             | BT labtool reture error                       |                                   |
| 503             | FM labtool reture error                       |                                   |
| 504             | MRD file already exist                        |                                   |
| 505             | MRD file with same version already exist      |                                   |
| 506             | MRD file with newer version already exist     |                                   |
| 507             | MRD authorization failure                     |                                   |
| 508             | (U)SIM PUK blocked                            |                                   |
| 509             | Vendor not supported                          |                                   |
| 510             | NVM path not exist                            |                                   |
| 511             | NVM file comcfg error                         |                                   |
| 535             | PROTOCOL stack busy                           |                                   |
| 600             | BTSAP card not accessible                     |                                   |
| 601             | BTSAP card powered off                        |                                   |
| 602             | BTSAP card removed                            |                                   |
| 603             | BTSAP card powered on                         |                                   |
| 604             | BTSAP data not available                      |                                   |
| 605             | BTSAP not supported                           |                                   |
| 606             | Non-Production mode                           |                                   |
| 753             | missing required cmd parameter                | CRSM 缺少参数                     |
| 754             | Invalid SIM command                           | CRSM 无效命令                     |
| 755             | Invalid file id                               | CRSM 无效的文件                   |
| 756             | Missing required P1/2/3 parameter             | CRSM 缺少P 参数                   |
| 757             | Invalid P1/2/3 parameter                      | CRSM 无效的P 参数                 |
| 758             | Missing required command data                 | CRSM 缺少命令数据                 |
| 759             | invalid characters in command data            | CRSM 命令行中有无效字符           |
| 765             | Invalid input value                           | 无效输入值                        |
| 766             | Unsupported mode                              | 不支持的模式                      |
| 767             | Operation failed                              | 操作失败                          |
| 768             | Mux already running                           | 多路复用已经在运行                |
| 769             | Unable to get control                         | 不能获得控制权                    |
| 770             | SIM network reject                            | SIM 网络拒绝                      |
| 771             | Call setup in progress                        | 正在建立呼叫                      |
| 772             | SIM powered down                              | SIM 关闭了                        |
| 773             | SIM file not present                          | SIM 文件不在                      |
| 774             | RAC refresh net time failure                  |                                   |
| 791             | Param count not enough                        |                                   |
| 792             | Param count beyond                            |                                   |
| 793             | Param value range beyond                      |                                   |
| 794             | Param type not match                          |                                   |
| 795             | Param format invalid                          |                                   |
| 796             | Get a null param                              |                                   |
| 797             | CFUN state is 0 or 4                          |                                   |
| 810             | No Error                                      |                                   |
| 811             | Unrecognized Command                          |                                   |
| 812             | Return Value Error                            |                                   |
| 813             | Syntax Error                                  |                                   |
| 814             | Unspecified Error                             |                                   |
| 815             | Data Transfer Already                         |                                   |
| 816             | Action Already                                |                                   |
| 817             | Not At Cmd                                    |                                   |
| 818             | Multi Cmd too long                            |                                   |
| 819             | Abort Cops                                    |                                   |
| 820             | No Call Disc                                  |                                   |
| 821             | BT SAP Undefined                              |                                   |
| 822             | BT SAP Not Accessible                         |                                   |
| 823             | BT SAP Card Removed                           |                                   |
| 824             | AT Not Allowed By Customer                    |                                   |
| 890             | GPS_NOT_RUNNING                               |                                   |
| 891             | GPS_IS_RUNNING                                |                                   |
| 892             | GPS_IS_FIXING                                 |                                   |
| 893             | GPS_IS_SLEEPING                               |                                   |
| 894             | GPS_NOT_SLEEPING                              |                                   |
| 900             | DIAED_REJECT                                  |                                   |
| 901             | PDP_NO_ACTIVE                                 |                                   |
| 902             | PDP_ACTIVE                                    |                                   |
| 910             | TCP_CONNECTION_REJECT                         |                                   |
| 911             | TCP_CONNECT_OVERTIME                          |                                   |
| 912             | SOCKET_CONNECTION_EXIST                       |                                   |
| 913             | SOCKET_CONNECTION_NOT_EXIST                   |                                   |
| 914             | BUFFER_OVER_SIZE                              |                                   |
| 915             | SENDING_OVERTIME                              |                                   |
| 916             | DNS_EXIST                                     |                                   |
| 917             | DNS_PARSE_OVERTIME                            |                                   |
| 918             | DNS_PARSE_ERROR                               |                                   |
| 980             | INPUT_VALUE_ERROR                             |                                   |
| 981             | OTHER_ERROR                                   |                                   |
| 982             | ERROR                                         |                                   |
| 983             | NOT_ALLOWED                                   |                                   |
| 1000            | UPGRADE_INVALID_URL                           |                                   |
| 1001            | UPGRADE_NET_ERROR                             |                                   |
| 1002            | UPGRADE_SERVER_CONNECT_ERROR                  |                                   |
| 1003            | UPGRADE_INVALID_FILE                          |                                   |
| 1004            | UPGRADE_SERVER_RESPONSE_ERROR                 |                                   |
| 1005            | UPGRADE_WRITE_FLASH_ERROR                     |                                   |
| 1006            | UPGRADE_ERROR                                 |                                   |
| 65535           | Other Error                                   |                                   |
