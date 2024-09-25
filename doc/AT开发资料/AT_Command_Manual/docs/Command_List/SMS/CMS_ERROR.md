## 短信业务失败结果码：CMS ERROR：`<err>`

短消息业务失败结果编码描述一个移动设备或网络的错误。其作用与错误结果编码类似。该编码常在一个指令失败时出现。返回的结果码为：`+CMS ERROR: <err>`

| 数字型`<err>`取值 | 冗长方式的`<err>`取值                                        | 解释                             |
| ----------------- | ------------------------------------------------------------ | -------------------------------- |
| 1                 | Unassigned(unallocated) number                               |                                  |
| 3                 | No route to destination                                      |                                  |
| 6                 | Channel unacceptable                                         |                                  |
| 8                 | Operator determined barring                                  |                                  |
| 10                | Call barred                                                  |                                  |
| 11                | Reserved                                                     |                                  |
| 16                | Normal call clearing                                         |                                  |
| 17                | User busy                                                    |                                  |
| 18                | No user reponding                                            |                                  |
| 19                | User alerting,no answer                                      |                                  |
| 21                | Short message transfer rejected                              |                                  |
| 22                | Number changed                                               |                                  |
| 25                | Pre-emption                                                  |                                  |
| 26                | Non-selected user clearing                                   |                                  |
| 27                | Destionation out of service                                  |                                  |
| 28                | Invalid number format (incomplete number)                    |                                  |
| 29                | Facility rejected                                            |                                  |
| 30                | Response to STATUS ENQUIRY                                   |                                  |
| 32                | Normal,unspecified                                           |                                  |
| 34                | No circuit/channel available                                 |                                  |
| 38                | Network out of order                                         |                                  |
| 41                | Temporary failure                                            |                                  |
| 42                | Switching equipment Congestion                               |                                  |
| 43                | Access information discarded                                 |                                  |
| 44                | Requested circuit/channel not available                      |                                  |
| 47                | Resources unavailable, unspecified                           |                                  |
| 49                | Quality of service unavailable                               |                                  |
| 50                | Requested facility not subscribed                            |                                  |
| 55                | Requested facility not subscribed                            |                                  |
| 57                | Bearer capability not authorized                             |                                  |
| 58                | Bearer capability not presently available                    |                                  |
| 63                | Service or option not available, unspecified                 |                                  |
| 65                | Bearer service not implemented                               |                                  |
| 68                | ACM equal or greater than ACM maximum                        |                                  |
| 69                | Requested facility not implemented                           |                                  |
| 70                | Only restricted digital information bearer capability is available |                                  |
| 79                | Service or option not implemented, unspecified               |                                  |
| 81                | Invalid transaction identifier value                         |                                  |
| 87                | User not member of CUG                                       |                                  |
| 88                | Incompatible destination                                     |                                  |
| 91                | Invalid transit network selection                            |                                  |
| 95                | Semantically mandatory information                           |                                  |
| 96                | Invalid mandatory information                                |                                  |
| 97                | Message type non-existent or not implemented                 |                                  |
| 98                | Message type not compatible with protocol state              |                                  |
| 99                | Information element non-existent or not implemented          |                                  |
| 100               | Conditional information element error                        |                                  |
| 101               | Message not compatible with protocol                         |                                  |
| 102               | Recovery on timer expiry                                     |                                  |
| 111               | Protocol error, unspecified                                  |                                  |
| 127               | Interworking, unspecified                                    |                                  |
| 128               | Telematic interworking not supported                         |                                  |
| 129               | Short message Type 0 not supported                           |                                  |
| 130               | Cannot replace short message                                 |                                  |
| 143               | Unspecified TP-PID error                                     |                                  |
| 144               | Data coding scheme (alphabet) not supported                  |                                  |
| 145               | Message class not supported                                  |                                  |
| 159               | Unspecified TP-DCS error                                     |                                  |
| 160               | Command cannot be acted                                      |                                  |
| 161               | Command unsupported                                          |                                  |
| 175               | Unspecified TP-Command error                                 |                                  |
| 176               | TPDU not supported                                           |                                  |
| 192               | SC busy                                                      |                                  |
| 193               | No SC subscription                                           |                                  |
| 194               | SC system failure                                            |                                  |
| 195               | Invalid SME address                                          |                                  |
| 196               | Destination SME barred                                       |                                  |
| 197               | SM Rejected-Duplicate SM                                     |                                  |
| 198               | TP-VPF not supported                                         |                                  |
| 199               | TP-VP not supported                                          |                                  |
| 208               | SIM SMS storage full                                         |                                  |
| 209               | No SMS storage capability in SIM                             |                                  |
| 210               | Error in MS                                                  |                                  |
| 211               | Memory Capacity Exceeded                                     |                                  |
| 212               | SIM Application Toolkit Busy                                 |                                  |
| 213               | SIM data download error                                      |                                  |
| 224               | CP retry exceed                                              |                                  |
| 225               | RP trim timeout                                              |                                  |
| 226               | SMS connection broken                                        |                                  |
| 255               | Unspecified error cause                                      |                                  |
| 300               | ME failure                                                   | ME 错误                          |
| 301               | SMS service of ME reserved                                   | 预留 ME 的 SMS 业务              |
| 302               | operation not allowed                                        | 操作不允                         |
| 303               | operation not supported                                      | 操作不支持                       |
| 304               | invalid PDU mode parameter                                   | PDU 模式下无效的参数             |
| 305               | invalid text mode parameter                                  | TEXT 模式下无效的参数            |
| 310               | (U)SIM not inserted                                          | SIM 卡未插入                     |
| 311               | (U)SIM PIN required                                          | 需要 SIM 卡的 PIN                |
| 312               | PH-(U)SIM PIN required                                       | 需要 PH-SIM 卡的 PIN             |
| 313               | (U)SIM failure                                               | SIM 卡故障                       |
| 314               | (U)SIM busy                                                  | SIM 卡遇忙                       |
| 315               | (U)SIM wrong                                                 | SIM 错误                         |
| 316               | (U)SIM PUK required                                          | 需要 SIM 卡的 PUK                |
| 317               | (U)SIM PIN2 required                                         | 需要 SIM 卡的 PIN2               |
| 318               | (U)SIM PUK2 required                                         | 需要 SIM 卡的 PUK2               |
| 320               | memory failure                                               | 存错错误                         |
| 321               | invalid memory index                                         | 无效的存贮索引                   |
| 322               | memory full                                                  | 存储满                           |
| 330               | SMSC address unknown                                         | 短信中心号码未知                 |
| 331               | no network service                                           | 无网络服务                       |
| 332               | network timeout                                              | 网络超时                         |
| 340               | no +CNMA acknowledgement expected                            | 无预期的+CNMA 确认               |
| 500               | unknown error                                                | 未知错误                         |
| 512               | USER ABORT                                                   | （适用于cat1 模块）              |
| 513               | UNABLE TO STORE                                              | （适用于cat1 模块）              |
| 514               | INVALID STATUS                                               | （适用于cat1 模块）              |
| 515               | INVALID ADDR CHAR                                            | （适用于cat1 模块）              |
| 516               | INVALID LEN                                                  | （适用于cat1 模块）              |
| 517               | INVALID PDU CHAR                                             | （适用于cat1 模块）              |
| 518               | INVALID PARA                                                 | （适用于cat1 模块）              |
| 519               | INVALID LEN OR CHAR                                          | （适用于cat1 模块）              |
| 520               | INVALID TXT CHAR                                             | （适用于cat1 模块）              |
| 521               | TIMER EXPIRED                                                | （适用于cat1 模块）              |
| 528               |                                                              | PDU 中无效（非16 进制）字符      |
| 529               |                                                              | PDU 长度不正确                   |
| 530               | SMS SEND FAIL                                                | （适用于cat1 模块）              |
| 531               |                                                              | 根据制造商不同而变化             |
| 532               |                                                              | 地址中有无效(非16 进制)字符      |
| 533               |                                                              | 无效地址                         |
| 534               |                                                              | PDU 长度（UDL）不正确            |
| 536               |                                                              | SCA 长度不正确                   |
| 537               |                                                              | 无效的第一个8 位字节(应为2 或34) |
| 538               |                                                              | 无效的命令类型                   |
| 539               |                                                              | SRR 位未设置                     |
| 540               |                                                              | SRR 设置                         |
| 604               | unspecified parsing error                                    | 未指定的解析错误                 |
