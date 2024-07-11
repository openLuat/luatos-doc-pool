@[TOC]

# alipay
alipay支持库
## 支付宝消息

支付宝消息

| **消息ID**                            | **消息说明**                 |
| ----------------------------------- | ------------------------ |
| SDK_INIT_OK                         | SDK初始化成功                   |
| NETWORK_INIT_OK                     | 网络初始化成功                   |
| SDK_INIT_ERROR                      | SDK初始化失败               |
| NETWORK_INIT_ERROR                  | 网络初始化失败               |

---



## alipay.setup(sDeviceSupplier,sMerchantUser,sItemId,sProductKey,getTerminalId) 

支付宝配置

**参数**


| **参数**                            | **类型**                 |**释义**|**取值**|
| --------------------------- | ------------------- |-------------------- |--------------------- |
| sDeviceSupplier              | string         | 设备供应商编号|最大长度 32 字节|
| sMerchantUser                | string         |设备运营商的编号 |最大长度 32 字节。|
| sItemId                      | string         |产品身份识别号 | 最大长度 64 字节。|
| sProductKey                  | string         | 备行业和设备形态的精简描述|格式为字符串，最大长度 64 字节|
| getTerminalId                | string         |设备的序列号 SN |最大长度 64 字节，可以为空|

**返回值**

无

---



## alipay.sign(mode,code,amount) 

支付宝数据加签

**参数**


| **参数**                            | **类型**                 |**释义**|**取值**|
| --------------------------- | ------------------- |-------------------- |--------------------- |
| mode              | number         |加签方式|alipay.SIGN_RECV_QRCODE：用户被扫。alipay.SIGN_FACE_TOKEN：用户人脸。alipay.SIGN_QRCODE：用户主扫。alipay.SIGN_DELEGATED：第三方代扣。|
| code              | string         |需要加签的数据|字符串，最大长度为 128 字节
| amount            | string         |需要加签的金额 | 实际单位为元，字符串，最大值为 32 字节。 举例 0.01 表示 1 分钱|

**返回值**


| **返回值**                            | **释义**                 |
| ----------------------------------- | ------------------------ |
| alipay.SIGN_RV_OK                         | 操作成功                   |
| alipay.SIGN_RV_PARAM_ERROR                     | 参数错误                   |
| alipay.SIGN_RV_BUF_NOT_ENOUGHT                      | 传入的内存不足               |
| alipay.SIGN_RV_IO_ERROR                  | IO错误               |
| alipay.SIGN_RV_SEC_INTERNAL_ERROR                     | 安全库内部错误                   |
| alipay.SIGN_RV_SIGN_ERROR                      | 签名接口调用错误               |
| alipay.SIGN_RV_UNKNOWN                  | 未知错误               |

---



## alipay.rep(business_no,qr_code,amount,time_consuming,fail_reason,timestamp) 

支付宝交易信息上报

**参数**


| **参数**                            | **类型**                 |**释义**|**取值**|
| --------------------------- | ------------------- |-------------------- |--------------------- |
| business_no              | string         | 交易产生的流水号|字符串，最长 64 字节，为空表示无。|
| qr_code              | string         |用户付款码字符串|最长 64 字节，为空表示无|
| amount              | number         |交易金额|单位为分|
| time_consuming                  | number         |交易时间耗费|单位为秒，<business_no> 有值的时候不可为空|
| fail_reason                  | number         |交易错误原因,需要自己传入，请传入交易错误原因||
| timestamp                  | number         |交易 UTC 时间戳|单位为秒|

| **交易错误原因**                            | **释义**                 |
| ----------------------------------- | ------------------------ |
| alipay.TRANCTION_UNKNOWN                         | 交易结果无法获取                   |
| alipay.TRANCTION_NONE                     | 交易成功时设置                   |
| alipay.TRANCTION_TIMEOUT                      | 交易超时               |
| alipay.TRANCTION_TRADE_FAIL                  | 交易返回失败               |
| alipay.TRANCTION_PROCESSING                     | 支付处理中                   |
| alipay.TRANCTION_NETWORK_EXCEPTION                      | 网络异常               |
| alipay.TRANCTION_UNKNOW_EXCEPTION                  | 未知异常               |
| alipay.TRANCTION_NOT_SUPPORT                  | 不支持的交易               |

**返回值**


| **返回值**                            | **释义**                 |
| ----------------------------------- | ------------------------ |
| alipay.BIZ_SUCC                         | 操作成功                   |
| alipay.BIZ_PARA_ERR                     | 参数有误                   |
| alipay.BIZ_NOT_INIT                      | 还没初始化               |
| alipay.BIZ_BUFF_ERR                  | 缓存队列访问错误               |
| alipay.BIZ_MEM_ERR                     | 内存分配失败                   |
| alipay.BIZ_BUSY_ERR                      | MDAP繁忙               |
| alipay.BIZ_BUFF_FULL                  | 缓存队列已满               |
| alipay.BIZ_BACKUP_FAIL                  | 数据备份失败，但不影响L1缓存中数据的使用               |

---



## alipay.info(account_flow,iccid,human_verify) 

支付宝产品规格信息上报

**参数**


| **参数**                            | **类型**                 |**释义**|**取值**|
| --------------------------- | ------------------- |-------------------- |--------------------- |
| account_flow              | string         | 交易产生的流水号|字符串，最长 64 字节，为空表示无。|
| iccid              | string         |sim卡iccid|最长 64 字节，为空表示无|
| human_verify              | number         |设备核查消费者身份的方式|0x01：二维码识别<br/>0x02：人脸识别<br/>0x04：手机号码识别(SMS/CALL)<br/>0x08：声纹识别<br/>0x10：NFC识别<br/>0x20：指纹识别<br/>0x40：邮箱识别|

**返回值**


| **返回值**                            | **释义**                 |
| ----------------------------------- | ------------------------ |
| alipay.BIZ_SUCC                         | 操作成功                   |
| alipay.BIZ_PARA_ERR                     | 参数有误                   |
| alipay.BIZ_NOT_INIT                      | 还没初始化               |
| alipay.BIZ_BUFF_ERR                  | 缓存队列访问错误               |
| alipay.BIZ_MEM_ERR                     | 内存分配失败                   |
| alipay.BIZ_BUSY_ERR                      | MDAP繁忙               |
| alipay.BIZ_BUFF_FULL                  | 缓存队列已满               |
| alipay.BIZ_BACKUP_FAIL                  | 数据备份失败，但不影响L1缓存中数据的使用               |

---



## alipay.act(brocast_count,scan_count) 

支付宝行为数据上报

**参数**


| **参数**                            | **类型**                 |**释义**|**取值**|
| --------------------------- | ------------------- |-------------------- |--------------------- |
| brocast_count              | number         | 语音播报增量次数||
| scan_count              | number         |扫码次数增量||

**返回值**


| **返回值** 						   | **释义** 				|
| ----------------------------------- | ------------------------ |
| alipay.BIZ_SUCC						  | 操作成功				   |
| alipay.BIZ_PARA_ERR					  | 参数有误				   |
| alipay.BIZ_NOT_INIT					   | 还没初始化			   |
| alipay.BIZ_BUFF_ERR				   | 缓存队列访问错误				|
| alipay.BIZ_MEM_ERR					 | 内存分配失败					|
| alipay.BIZ_BUSY_ERR					   | MDAP繁忙 			  |
| alipay.BIZ_BUFF_FULL					| 缓存队列已满			   |
| alipay.BIZ_BACKUP_FAIL				  | 数据备份失败，但不影响L1缓存中数据的使用 			  |

---



