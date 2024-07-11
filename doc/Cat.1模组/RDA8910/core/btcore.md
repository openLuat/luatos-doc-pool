@[TOC]

# btcore
BLE 蓝牙功能
## 蓝牙消息

蓝牙消息

| **消息ID**                           | **消息说明**                 |
| ------------------------------------ | ---------------------------- |
| MSG_OPEN_CNF                         | 蓝牙打开成功                 |
| MSG_CLOSE_CNF                        | 蓝牙关闭成功                 |
| MSG_BLE_CONNECT_CNF                  | BLE蓝牙主模式连接               |
| MSG_BLE_CONNECT_IND                  | BLE蓝牙从模式连接               |
| MSG_BLE_DISCONNECT_CNF               | BLE蓝牙主模式断开连接           |
| MSG_BLE_DISCONNECT_IND               | BLE蓝牙从模式断开连接           |
| MSG_BLE_DATA_IND                     | BLE蓝牙数据接收                     |
| MSG_BLE_SCAN_CNF                     | BLE蓝牙扫描打开成功                 |
| MSG_BLE_SCAN_IND                     | BLE蓝牙扫描数据上报                 |
| MSG_BLE_FIND_CHARACTERISTIC_IND      | BLE蓝牙发现服务中包含的特征成功     |
| MSG_BLE_FIND_CHARACTERISTIC_UUID_IND | BLE蓝牙发现服务中包含的特征uuid成功 |
| MSG_BLE_FIND_SERVICE_IND             | BLE蓝牙发现服务成功                 |
| MSG_BLE_READ_VALUE_IND               | BLE蓝牙读value值                    |
| MSG_BLE_MTU_EXCHANGE_IND             | BLE蓝牙设置MTU                    |
| MSG_BT_HFP_CONNECT_IND               | 经典蓝牙HFP连接                    |
| MSG_BT_HFP_DISCONNECT_IND            | 经典蓝牙HFP断开连接                    |
| MSG_BT_HFP_CALLSETUP_OUTGOING        | 经典蓝牙HFP建立呼出电话                    |
| MSG_BT_HFP_CALLSETUP_INCOMING        | 经典蓝牙HFP呼叫传入                    |
| MSG_BT_HFP_RING_INDICATION           | 经典蓝牙HFP呼叫传入铃声               |
| MSG_BT_AVRCP_CONNECT_IND             | 经典蓝牙AVRCP连接                    |
| MSG_BT_AVRCP_DISCONNECT_IND          | 经典蓝牙AVRCP断开连接                 |

---



## btcore.open(mode)

打开蓝牙模式

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|mode|number|区分模式|经典蓝牙：mode=2<br/>主模式：mode=1<br/>从模式：mode=0|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1，成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.close()

关闭蓝牙

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1，成功/失败|0/-1|

---



## btcore.send(data,uuid_c,handle[,mode])

写BLE蓝牙

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|string|写入数据内容|最大244字节|
|uuid_c|number|特征uuid|16bit uuid int型/128bit uuid 字符串|
|handle|number|连接句柄|   |
|mode|number|主模式发送方式|默认0(write without rsp),1(write)|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1，成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.recv(len)

读BLE蓝牙

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|len|number|想要读到的数据长度|最大244字节|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|recvuuid|number|数据来源uuid|  |
|recvdata|string|实际读到的数据内容|  |
|recvlen|number|实际读到的数据长度|  |

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.setname(name)

设置蓝牙名称

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|name|string|蓝牙名称|最大26字节|

**返回值**

无

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.setadvparam(advmin,advmax,advtype,ownaddrtype,advchannmap,advfilter[,directaddrtype,directaddr])

设置广播参数

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|advmin|number|最小广播间隔|最小广播间隔,单位0.625ms，范围20ms~10.24s (必选)|
|advmax|number|最大广播间隔|最大广播间隔,单位0.625ms，范围20ms~10.24s (必选)|
|advtype|number|广播类型|广播类型 (必选)：0: Connectable undirected advertising (ADV_IND)<br/>1: Connectable high duty cycle directed advertising<br/>2: Scannable undirected advertising (ADV_SCAN_IND)<br/>3: Non connectable undirected advertising (ADV_NONCONN_IND)<br/>4: Connectable low duty cycle directed advertising|
|ownaddrtype|number|广播本地地址类型|广播本地地址类型(必选)：0：Public Device Address<br/>1：Random Device Address<br/>2：Controller generates Resolvable Private Address based on the local IRK from the resolving list. If the resolving list contains no matching entry, use the public address<br/>3：Controller generates Resolvable Private Address based on the local IRK from the resolving list. If the resolving list contains no matching entry, use the random address from LE_Set_Random_Address|
|advchannmap|number|广播channel map|广播channel map,3个bit，分别对应37，38，39信道 (必选)|
|advfilter|number|广播过滤策略|广播过滤策略(必选)：<br/>0: Process scan and connection requests from all devices.<br/>1: Process connection requests from all devices and only scan requests from devices that are in the White List.<br/>2: Process scan requests from all devices and only connection requests from devices that are in the White List.<br/>3: Process scan and connection requests only from devices in the White List|
|directaddrtype|number|定向地址类型|定向地址类型(可选)：0: Public Device Address<br/>1: Random Device Address|
|directaddr|string|定向地址|定向地址(可选)|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

**例子**

```lua
--具体设置要求见1321页：https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=457080)

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.setscanparam(scanType,scanInterval,scanWindow,filterPolicy,own_addr_type)

设置扫描参数

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|scanType|number|扫描类型|0 passive/1 active|
|scanInterval|number|扫描间隔|单位0.625ms，范围2.5ms~10.24s|
|scanWindow|number|扫描窗口|单位0.625ms，范围2.5ms~10.24s|
|filterPolicy|number|扫描过滤策略|0: Accept all advertising and scan response PDUs except directed advertising PDUs not addressed to this device (default)/1: Accept only advertising and scan response PDUs from devices where the advertiser’s address is in the White List. Directed advertising PDUs which are not addressed to this device shall be ignored|
|own_addr_type|number|本地地址类型|0：Public Device Address<br/>1：Random Device Address<br/>2：Controller generates Resolvable Private Address based on the local IRK from the resolving list. If the resolving list contains no matching entry, use the public address<br/>3：Controller generates Resolvable Private Address based on the local IRK from the resolving list. If the resolving list contains no matching entry, use the random address from LE_Set_Random_Address|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

**例子**

```lua
--(具体设置要求见1331页：https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=457080)
btcore.setscanparam(scanType,scanInterval,scanWindow,filterPolicy,own_addr_type)

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.setadvdata(data)

设置蓝牙广播包数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|string|广播包数据|最大31字节|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.setscanrspdata(data)

设置蓝牙响应包数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|string|响应包数据|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|	number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.advertising(enable)

蓝牙广播开关

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|enable|number|广播开关|1 打开广播/0 关闭广播|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.state()

查询蓝牙状态

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.scan(enable)

蓝牙扫描开关

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|enable|number|扫描开关|1 打开扫描/0 关闭扫描|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.disconnect(handle)

蓝牙主动断开连接

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|handle|number|连接句柄|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.connect(addr,addr_type)

蓝牙连接

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|addr|string|蓝牙地址|   |
|addr_type|number|地址类型|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.addservice(uuid_s)

蓝牙添加服务

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|uuid_s|number|服务uuid|16bit uuid int型/128bit uuid 字符串|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.addcharacteristic(uuid_c,type,permission)

蓝牙添加特征

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|uuid_c|number|特征uuid|16bit uuid int型/128bit uuid 字符串|
|type|number|特征属性|   |
|permission|string|特征权限|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

**例子**

```lua
--特征属性配置：
#define ATT_CHARA_PROP_BROADCAST    0x01
#define ATT_CHARA_PROP_READ         0x02
#define ATT_CHARA_PROP_WWP          0x04   // WWP short for "write without response"
#define ATT_CHARA_PROP_WRITE        0x08
#define ATT_CHARA_PROP_NOTIFY     0x10
#define ATT_CHARA_PROP_INDICATE 0x20
#define ATT_CHARA_PROP_ASW     0x40   // ASW short for "Authenticated signed write"
#define ATT_CHARA_PROP_EX_PROP  0x80
--特征权限配置：
#define ATT_PM_READABLE                    0x0001
#define ATT_PM_WRITEABLE                   0x0002
#define ATT_PM_R_AUTHENT_REQUIRED          0x0004
#define ATT_PM_R_AUTHORIZE_REQUIRED        0x0008
#define ATT_PM_R_ENCRYPTION_REQUIRED       0x0010
#define ATT_PM_R_AUTHENT_MITM_REQUERED     0x0020
#define ATT_PM_W_AUTHENT_REQUIRED          0x0040
#define ATT_PM_W_AUTHORIZE_REQUIRED        0x0080
#define ATT_PM_W_ENCRYPTION_REQUIRED       0x0100
#define ATT_PM_W_AUTHENT_MITM_REQUERED     0x0200
#define ATT_PM_BR_ACCESS_ONLY              0x0400


```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.adddescriptor(uuid_d,value)

蓝牙添加描述

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|uuid_d|number|描述uuid|16bit uuid int型|
|value|string|描述属性|int型/字符串|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2166 "示例")

---



## btcore.findcharacteristic(uuid_s,handle)

蓝牙发现服务内包含的特征

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|uuid_s|number|服务uuid|16bit uuid int型/128bit uuid 字符串|
|handle|number|连接句柄|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.findservice(handle)

蓝牙发现服务

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|handle|number|连接句柄|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.opennotification(uuid_c,handle)

蓝牙打开通知

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|uuid_c|number|特征uuid|16bit uuid int型/128bit uuid 字符串|
|handle|number|连接句柄|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.closenotification(uuid_c,handle)

蓝牙关闭通知

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|uuid_c|number|特征uuid|16bit uuid int型/128bit uuid 字符串|
|handle|number|连接句柄|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.getaddr()

读蓝牙MAC地址

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|本机蓝牙MAC地址|   |

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.setbeacondata(uuid,major,minor)

设置蓝牙beacon数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|uuid|string|字符串|128位|
|major|number|编号|0~65535|
|minor|number|标号|0~65535|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

**例子**

```lua
 --[[
     UUID ：这是将你所有的beacon与其他人的beacon设备区别开的id！例如，目前在商店里某个区域分布着多个beacon形成一条“链带”，用于为顾客提供特定的服务，那么归属于同一条“链带”的beacon将分配到相同的proximity UUID。为这条“链带”设计的专用应用程序将会在后台使用这个UUID扫描到这条“链带”中的beacon设备。

    major 编号：用于将相关的beacon标识为一组。例如，一个商店中的所有beacon将会分配到相同的major编号。通过这种方式，应用程序就能够知道顾客位于哪一家商店。

    minor 标号：用于标识特定的beacon设备。例如一个商店中的每一个beacon设备都拥有唯一的minor编号，这样你才能够知道顾客位于商店中的哪个位置。
 ]]

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.addwhitelist(addr,addr_type)

添加蓝牙白名单

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|addr|string|蓝牙地址|   |
|addr_type|number|地址类型|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.removewhitelist(addr,addr_type)

移除蓝牙白名单

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|addr|string|蓝牙地址|   |
|addr_type|number|地址类型|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.clearwhitelist()

清空蓝牙白名单

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.readvalue(uuid_c,handle)

读蓝牙特征value

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|uuid_c|number|特征uuid|16bit uuid int型/128bit uuid 字符串 |
|handle|number|连接句柄| |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1 |

**例子**

```lua
--注：适用于主模式，通过MSG_BLE_READ_VALUE_IND消息上报获取value

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.setvalue(data,uuid_c[,att_len])

设置蓝牙特征value

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|string|写入数据内容|最大244字节|
|uuid_c|number|特征uuid|16bit uuid int型/128bit uuid 字符串 |
|att_len|number|特征value长度|最大244字节|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

**例子**

```lua
--注：适用于从模式

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.setmtu(size)

设置蓝牙最大传输单元

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|size|number|最大传输单元|23~247,单位字节|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.setvisibility(visible)

设置经典蓝牙可见性

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|visible|number|可见性|NO_VISIABLE = 0x00<br>CONNECTABLE = 0x01<br>DISCOVERABLE = 0x10<br>ALL_VISIABLE = 0x11  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.getvisibility()

获取经典蓝牙可见性

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|	number|visible, 可见性|NO_VISIABLE = 0x00<br>CONNECTABLE = 0x01<br>DISCOVERABLE = 0x10<br>ALL_VISIABLE = 0x11   |

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.sethfpvol(vol)

经典蓝牙设置HFP音量

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|vol|number|音量|0~15|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.hfpcallanswer()

经典蓝牙接听电话

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.hfpcallreject()

经典蓝牙拒接电话

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.hfpcallhangup()

经典蓝牙挂断电话

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.hfpcallredial()

经典蓝牙重拨电话

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.hfpcalldial(number)

经典蓝牙拨打电话

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|number|number|电话号码|字符串|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.setavrcpvol(vol)

经典蓝牙设置AVRCP音量

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|vol|number|音量|0~127|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.getavrcpvol()

经典蓝牙获取AVRCP音量

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|vol,音量|0~127|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.setavrcpsongs(state)

经典蓝牙设置AVRCP音乐播放的状态

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|state|number|状态|0：暂停/1：播放/2：上一曲/3：下一曲|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1, 成功/失败|0/-1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



## btcore.getavrcpstate()

经典蓝牙获取AVRCP状态

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|state状态|0:停止,1:播放,2:暂停,255:错误|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2455#API_18 "指南")  [示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/bluetooth)

---



