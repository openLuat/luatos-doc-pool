@[TOC]

# crypto
lua.crypto库
## crypto.base64_encode(originstr,len)

base64加密

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|originstr|string|需要加密的字符串|   |
|len|number|字符串长度|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|加密后的数据|   |

**例子**

```lua
local originstr = "123456"
local encodestr = crypto.base64_encode(originstr,slen(originstr))
print("base64_encode",encodestr)
--base64_encode	MTIzNDU2

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.base64_decode(originstr,len)

base64解密

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|originstr|string|需要解密的字符串|   |
|len|number|字符串长度|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|解密后的数据|   |

**例子**

```lua
print("base64_decode",crypto.base64_decode(encodestr,slen(encodestr)))
-- base64_decode	123456

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.hmac_md5(originstr,len_str,signkey,len_key)

hmac_md5算法

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|originstr|string|需要加密的字符串|   |
|len_str|number|字符串长度|   |
|signkey|string|密钥|   |
|len_key|number|密钥长度|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|加密后的数据|   |

**例子**

```lua
local originstr = "asdasdsadas"
local signkey = "123456"
print("hmac_md5",crypto.hmac_md5(originstr,slen(originstr),signkey,slen(signkey)))
-- hmac_md5	38A7B18DC5F6543849DC49F06FADE3CC

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.flow_md5()

流式md5算法

**参数**

无

**返回值**

无

**例子**

```lua
local fmd5Obj=crypto.flow_md5()
local testTable={"lqlq666lqlq946","07946lq94607946","lq54075407540707946"}
for i=1, #(testTable) do
    fmd5Obj:update(testTable[i])
end
print("testCrypto.flowMd5Test",fmd5Obj:hexdigest())

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.md5(originstr,len_str)

md5算法，支持计算文件的md5值

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|originstr|string|需要加密的字符串/要计算的文件路径|   |
|len_str|number|字符串长度/传入文件路径时为"file"|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|加密后的数据|   |

**例子**

```lua
   --计算字符串md5
   local originstr = "sdfdsfdsfdsffdsfdsfsdfs1234"  
   print("md5",crypto.md5(originstr,slen(originstr)))
   --计算文件md5
   log.info("testCrypto.sys.lua md5",crypto.md5("/lua/test.txt","file"))  
   --md5    235B69FBC9E75C4FD5E8C59F9CB16500 

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## hmac_sha1(originstr,len_str,signkey,len_key)

hmac_sha1算法

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|originstr|string|需要加密的字符串|   |
|len_str|number|字符串长度|   |
|signkey|string|密钥|   |
|len_key|number|密钥长度|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|加密后的数据|   |

**例子**

```lua
local originstr = "asdasdsadasweqcdsjghjvcb"
local signkey = "12345689012345"
print("hmac_sha1",crypto.hmac_sha1(originstr,slen(originstr),signkey,slen(signkey)))
--hmac_sha1	E3BB109BA59AF6A1F677157E8EC6B21349B9220F

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.sha1(originstr,len)

sha1算法

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|originstr|string|需要加密的字符串|   |
|len|number|字符串长度|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|加密后的数据|   |

**例子**

```lua
local originstr = "sdfdsfdsfdsffdsfdsfsdfs1234"
print("sha1",crypto.sha1(originstr,slen(originstr)))
-- sha1	16EBE919119B9B54C8AF6B4F2A09C18B6B6D8218

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.crc16(crcMethod,originstr,poly,initial,finally,inReverse,outReverse)

CRC16校验算法

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|crcMethod|string|校验方法|   |
|originstr|string|需要校验的字符串|   |
|poly|string|可选，默认0| |
|initial|string|可选，默认0| |
|finally|string|可选，默认0| |
|inReverse|string|可选，默认0| |
|outReverse|string|可选，默认0| |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|number|校验计算结果|   |

**例子**

```lua
local originStr = "sdfdsfdsfdsffdsfdsfsdfs1234"
print("testCrypto.crc16_MODBUS",string.format("%04X",crypto.crc16("MODBUS",originStr)))
print("testCrypto.crc16_IBM",string.format("%04X",crypto.crc16("IBM",originStr)))
print("testCrypto.crc16_X25",string.format("%04X",crypto.crc16("X25",originStr)))
print("testCrypto.crc16_MAXIM",string.format("%04X",crypto.crc16("MAXIM",originStr)))
print("testCrypto.crc16_USB",string.format("%04X",crypto.crc16("USB",originStr)))
print("testCrypto.crc16_CCITT",string.format("%04X",crypto.crc16("CCITT",originStr)))
print("testCrypto.crc16_CCITT-FALSE",string.format("%04X",crypto.crc16("CCITT-FALSE",originStr)))
print("testCrypto.crc16_XMODEM",string.format("%04X",crypto.crc16("XMODEM",originStr)))
print("testCrypto.crc16_DNP",string.format("%04X",crypto.crc16("DNP",originStr)))

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.crc32(originstr,len)

CRC32校验算法

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|originstr|string|需要校验的字符串|   |
|len|number|字符串长度|     |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|校验计算结果|   |

**例子**

```lua
--local originstr = "sdfdsfdsfdsffdsfdsfsdfs1234"  
print("crc32",string.format("%08X",crypto.crc32(originstr,slen(originstr))))  
--crc32    2FC153F9  

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---

## crypto.crc8(originstr,len)

CRC8校验算法

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|originstr|string|需要校验的字符串|   |
|len|number|字符串长度|     |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|校验计算结果|   |

**例子**

```lua
--local originstr = "sdfdsfdsfdsffdsfdsfsdfs1234"  
print("crc8",string.format("%02X",crypto.crc8(originstr,slen(originstr))))  
--crc8    C5  

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---

## crypto.aes_encrypt(mode,padding,originStr,password)

aes算法（参考http://tool.chacuo.net/cryptaes）

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|mode|string|加密模式|  |
|padding|string|填充方式|  |
|originStr|string|加密字符串|   |
|password|string|密钥|     |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|已加密的字符串|   |

**例子**

```lua
--下面示例为LuaTask的，如果需要LuaScript的，请参考LuaScript crypto demo
local originStr = "AES128 ECB ZeroPadding test"
--加密模式：ECB；填充方式：ZeroPadding；密钥：1234567890123456；密钥长度：128 bit
local encodeStr = crypto.aes_encrypt("ECB","ZERO",originStr,"1234567890123456")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("ECB","ZERO",encodeStr,"1234567890123456"))
originStr = "AES128 ECB Pkcs5Padding test"
--加密模式：ECB；填充方式：Pkcs5Padding；密钥：1234567890123456；密钥长度：128 bit
encodeStr = crypto.aes_encrypt("ECB","PKCS5",originStr,"1234567890123456")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("ECB","PKCS5",encodeStr,"1234567890123456"))
originStr = "AES128 ECB Pkcs7Padding test"
--加密模式：ECB；填充方式：Pkcs7Padding；密钥：1234567890123456；密钥长度：128 bit
encodeStr = crypto.aes_encrypt("ECB","PKCS7",originStr,"1234567890123456")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("ECB","PKCS7",encodeStr,"1234567890123456"))
originStr = "AES192 ECB ZeroPadding test"
--加密模式：ECB；填充方式：ZeroPadding；密钥：123456789012345678901234；密钥长度：192 bit
local encodeStr = crypto.aes_encrypt("ECB","ZERO",originStr,"123456789012345678901234")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("ECB","ZERO",encodeStr,"123456789012345678901234"))
originStr = "AES192 ECB Pkcs5Padding test"
--加密模式：ECB；填充方式：Pkcs5Padding；密钥：123456789012345678901234；密钥长度：192 bit
encodeStr = crypto.aes_encrypt("ECB","PKCS5",originStr,"123456789012345678901234")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("ECB","PKCS5",encodeStr,"123456789012345678901234"))
originStr = "AES192 ECB Pkcs7Padding test"
--加密模式：ECB；填充方式：Pkcs7Padding；密钥：123456789012345678901234；密钥长度：192 bit
encodeStr = crypto.aes_encrypt("ECB","PKCS7",originStr,"123456789012345678901234")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("ECB","PKCS7",encodeStr,"123456789012345678901234"))
originStr = "AES256 ECB ZeroPadding test"
--加密模式：ECB；填充方式：ZeroPadding；密钥：12345678901234567890123456789012；密钥长度：256 bit
local encodeStr = crypto.aes_encrypt("ECB","ZERO",originStr,"12345678901234567890123456789012")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("ECB","ZERO",encodeStr,"12345678901234567890123456789012"))
originStr = "AES256 ECB Pkcs5Padding test"
--加密模式：ECB；填充方式：Pkcs5Padding；密钥：12345678901234567890123456789012；密钥长度：256 bit
encodeStr = crypto.aes_encrypt("ECB","PKCS5",originStr,"12345678901234567890123456789012")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("ECB","PKCS5",encodeStr,"12345678901234567890123456789012"))
originStr = "AES256 ECB Pkcs7Padding test"
--加密模式：ECB；填充方式：Pkcs7Padding；密钥：12345678901234567890123456789012；密钥长度：256 bit
encodeStr = crypto.aes_encrypt("ECB","PKCS7",originStr,"12345678901234567890123456789012")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("ECB","PKCS7",encodeStr,"12345678901234567890123456789012"))
originStr = "AES128 CBC ZeroPadding test"
--加密模式：CBC；填充方式：ZeroPadding；密钥：1234567890123456；密钥长度：128 bit；偏移量：1234567890666666
local encodeStr = crypto.aes_encrypt("CBC","ZERO",originStr,"1234567890123456","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CBC","ZERO",encodeStr,"1234567890123456","1234567890666666"))
originStr = "AES128 CBC Pkcs5Padding test"
--加密模式：CBC；填充方式：Pkcs5Padding；密钥：1234567890123456；密钥长度：128 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CBC","PKCS5",originStr,"1234567890123456","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CBC","PKCS5",encodeStr,"1234567890123456","1234567890666666"))
originStr = "AES128 CBC Pkcs7Padding test"
--加密模式：CBC；填充方式：Pkcs7Padding；密钥：1234567890123456；密钥长度：128 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CBC","PKCS7",originStr,"1234567890123456","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CBC","PKCS7",encodeStr,"1234567890123456","1234567890666666"))
originStr = "AES192 CBC ZeroPadding test"
--加密模式：CBC；填充方式：ZeroPadding；密钥：123456789012345678901234；密钥长度：192 bit；偏移量：1234567890666666
local encodeStr = crypto.aes_encrypt("CBC","ZERO",originStr,"123456789012345678901234","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CBC","ZERO",encodeStr,"123456789012345678901234","1234567890666666"))
originStr = "AES192 CBC Pkcs5Padding test"
--加密模式：CBC；填充方式：Pkcs5Padding；密钥：123456789012345678901234；密钥长度：192 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CBC","PKCS5",originStr,"123456789012345678901234","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CBC","PKCS5",encodeStr,"123456789012345678901234","1234567890666666"))
originStr = "AES192 CBC Pkcs7Padding test"
--加密模式：CBC；填充方式：Pkcs7Padding；密钥：123456789012345678901234；密钥长度：192 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CBC","PKCS7",originStr,"123456789012345678901234","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CBC","PKCS7",encodeStr,"123456789012345678901234","1234567890666666"))
originStr = "AES256 CBC ZeroPadding test"
--加密模式：CBC；填充方式：ZeroPadding；密钥：12345678901234567890123456789012；密钥长度：256 bit；偏移量：1234567890666666
local encodeStr = crypto.aes_encrypt("CBC","ZERO",originStr,"12345678901234567890123456789012","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CBC","ZERO",encodeStr,"12345678901234567890123456789012","1234567890666666"))
originStr = "AES256 CBC Pkcs5Padding test"
--加密模式：CBC；填充方式：Pkcs5Padding；密钥：12345678901234567890123456789012；密钥长度：256 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CBC","PKCS5",originStr,"12345678901234567890123456789012","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CBC","PKCS5",encodeStr,"12345678901234567890123456789012","1234567890666666"))
originStr = "AES256 CBC Pkcs7Padding test"
--加密模式：CBC；填充方式：Pkcs7Padding；密钥：12345678901234567890123456789012；密钥长度：256 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CBC","PKCS7",originStr,"12345678901234567890123456789012","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CBC","PKCS7",encodeStr,"12345678901234567890123456789012","1234567890666666"))
originStr = "AES128 CTR ZeroPadding test"
--加密模式：CTR；填充方式：ZeroPadding；密钥：1234567890123456；密钥长度：128 bit；偏移量：1234567890666666
local encodeStr = crypto.aes_encrypt("CTR","ZERO",originStr,"1234567890123456","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CTR","ZERO",encodeStr,"1234567890123456","1234567890666666"))
originStr = "AES128 CTR Pkcs5Padding test"
--加密模式：CTR；填充方式：Pkcs5Padding；密钥：1234567890123456；密钥长度：128 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CTR","PKCS5",originStr,"1234567890123456","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CTR","PKCS5",encodeStr,"1234567890123456","1234567890666666"))
originStr = "AES128 CTR Pkcs7Padding test"
--加密模式：CTR；填充方式：Pkcs7Padding；密钥：1234567890123456；密钥长度：128 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CTR","PKCS7",originStr,"1234567890123456","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CTR","PKCS7",encodeStr,"1234567890123456","1234567890666666"))
originStr = "AES128 CTR NonePadding test"
--加密模式：CTR；填充方式：NonePadding；密钥：1234567890123456；密钥长度：128 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CTR","NONE",originStr,"1234567890123456","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CTR","NONE",encodeStr,"1234567890123456","1234567890666666"))
originStr = "AES192 CTR ZeroPadding test"
--加密模式：CTR；填充方式：ZeroPadding；密钥：123456789012345678901234；密钥长度：192 bit；偏移量：1234567890666666
local encodeStr = crypto.aes_encrypt("CTR","ZERO",originStr,"123456789012345678901234","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CTR","ZERO",encodeStr,"123456789012345678901234","1234567890666666"))
originStr = "AES192 CTR Pkcs5Padding test"
--加密模式：CTR；填充方式：Pkcs5Padding；密钥：123456789012345678901234；密钥长度：192 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CTR","PKCS5",originStr,"123456789012345678901234","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CTR","PKCS5",encodeStr,"123456789012345678901234","1234567890666666"))
originStr = "AES192 CTR Pkcs7Padding test"
--加密模式：CTR；填充方式：Pkcs7Padding；密钥：123456789012345678901234；密钥长度：192 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CTR","PKCS7",originStr,"123456789012345678901234","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CTR","PKCS7",encodeStr,"123456789012345678901234","1234567890666666"))
originStr = "AES192 CTR NonePadding test"
--加密模式：CTR；填充方式：NonePadding；密钥：123456789012345678901234；密钥长度：192 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CTR","NONE",originStr,"123456789012345678901234","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CTR","NONE",encodeStr,"123456789012345678901234","1234567890666666"))
originStr = "AES256 CTR ZeroPadding test"
--加密模式：CTR；填充方式：ZeroPadding；密钥：12345678901234567890123456789012；密钥长度：256 bit；偏移量：1234567890666666
local encodeStr = crypto.aes_encrypt("CTR","ZERO",originStr,"12345678901234567890123456789012","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CTR","ZERO",encodeStr,"12345678901234567890123456789012","1234567890666666"))
originStr = "AES256 CTR Pkcs5Padding test"
--加密模式：CTR；填充方式：Pkcs5Padding；密钥：12345678901234567890123456789012；密钥长度：256 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CTR","PKCS5",originStr,"12345678901234567890123456789012","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CTR","PKCS5",encodeStr,"12345678901234567890123456789012","1234567890666666"))

originStr = "AES256 CTR Pkcs7Padding test"
--加密模式：CTR；填充方式：Pkcs7Padding；密钥：12345678901234567890123456789012；密钥长度：256 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CTR","PKCS7",originStr,"12345678901234567890123456789012","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CTR","PKCS7",encodeStr,"12345678901234567890123456789012","1234567890666666"))

originStr = "AES256 CTR NonePadding test"
--加密模式：CTR；填充方式：NonePadding；密钥：12345678901234567890123456789012；密钥长度：256 bit；偏移量：1234567890666666
encodeStr = crypto.aes_encrypt("CTR","NONE",originStr,"12345678901234567890123456789012","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.aes_decrypt("CTR","NONE",encodeStr,"12345678901234567890123456789012","1234567890666666"))

```

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.sm4_encrypt(mode,padding,originStr,password)

SM4加密算法

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|mode|number|加密模式|   |
|padding|number|填充方式|   |
|originstr|string|加密的字符串|   |
|password|string|密钥|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|已加密的字符串|   |

**例子**

```lua
local originStr = "AES128 ECB ZeroPadding test"
--加密模式：ECB；填充方式：ZeroPadding；密钥：1234567890123456；密钥长度：128 bit
local encodeStr = crypto.sm4_encrypt("ECB","ZERO",originStr,"1234567890123456")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.sm4_decrypt("ECB","ZERO",encodeStr,"1234567890123456"))

originStr = "AES128 ECB Pkcs5Padding test"
--加密模式：ECB；填充方式：Pkcs5Padding；密钥：1234567890123456；密钥长度：128 bit
encodeStr = crypto.sm4_encrypt("ECB","PKCS5",originStr,"1234567890123456")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.sm4_decrypt("ECB","PKCS5",encodeStr,"1234567890123456"))

originStr = "AES256 CBC Pkcs5Padding test"
--加密模式：CBC；填充方式：Pkcs5Padding；密钥：1234567890123456；密钥长度：256 bit；偏移量：1234567890666666
encodeStr = crypto.sm4_encrypt("CBC","PKCS5",originStr,"1234567890123456","1234567890666666")
print(originStr,"encrypt",string.toHex(encodeStr))
log.info("testCrypto.decrypt",crypto.sm4_decrypt("CBC","PKCS5",encodeStr,"1234567890123456","1234567890666666"))

```

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.sm4_decrypt(mode,padding,encodeStr,password)

SM4解密算法

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|mode|number|加密模式|   |
|padding|number|填充方式|   |
|originstr|string|已加密的字符串|   |
|password|string|密钥||

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|解密的字符串|   |

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.des_encrypt(mode,padding,originStr,password)

des加密算法（参考http://tool.chacuo.net/cryptdes）

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|mode|number|加密模式|   |
|padding|number|填充方式|   |
|originstr|string|加密的字符串|   |
|password|string|密钥|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|已加密的字符串|   |

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.des_decrypt(mode,padding,encodeStr,password)

des解密算法（参考http://tool.chacuo.net/cryptdes）

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|mode|number|加密模式|   |
|padding|number|填充方式|   |
|originstr|string|已加密的字符串|   |
|password|string|密钥|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|解密的字符串|   |

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.rsa_encrypt("PUBLIC_KEY",publicKey,keylen,"PUBLIC_CRYPT",text)

RSA算法

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|"PUBLIC_KEY"|string|公钥|     |
|publicKey|string|密钥|  |
|keylen|number|密钥长度|   |
|"PUBLIC_CRYPT"|string|加密方式|    |
|text|string|待加密字符串|    |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|	string|加密数据|     |

**例子**

```lua
  --公钥加密
  local plainStr = "firmId=10015&model=zw-sp300&sn=W01201910300000108&version=1.0.0"
  local encryptStr = crypto.rsa_encrypt("PUBLIC_KEY",io.readFile("/lua/public.key"),2048,"PUBLIC_CRYPT",plainStr)
  log.info("rsaTest.encrypt",encryptStr:toHex())

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.rsa_decrypt("PRIVATE_KEY",privateKey,keylen,"PRIVATE_CRYPT",text)

rsa解密

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|"PUBLIC_KEY"|string|公钥|     |
|publicKey|string|密钥|  |
|keylen|number|密钥长度|   |
|"PUBLIC_CRYPT"|string|加密方式|    |
|text|string|待加密字符串|    |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|	string|解密的数据|         |

**例子**

```lua
  --私钥解密(2048bit，这个bit与实际私钥的bit要保持一致)
  local decryptStr = crypto.rsa_decrypt("PRIVATE_KEY",io.readFile("/lua/private.key"),2048,"PRIVATE_CRYPT",encryptStr)
  log.info("rsaTest.decrypt",decryptStr) --此处的decryptStr应该与plainStr相同

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2358 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2170 "示例")

---



## crypto.sha256(originStr)

sha256算法

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|originStr|string|string类型， 需要加密的字符串|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|加密后的数据|   |

**例子**

```lua
local originStr = "sdfdsfdsfdsffdsfdsfsdfs1234"
print("testCrypto.sha256",crypto.sha256(originStr))

```

---



## crypto.rsa_sha1_sign("PRIVATE_KEY",privateKey,keylen,"PRIVATE_CRYPT",text)

rsa私钥签名

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|"PRIVATE_KEY"|string|私钥|     |
|privateKey|string|密钥|  |
|keylen|number|密钥长度|1024或2048   |
|"PRIVATE_CRYPT"|string|加密方式|    |
|text|string|待加密字符串|    |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|	string|签名的数据|         |

**例子**

```lua
  --私钥签名(1024bit或2048bit，这个bit与实际私钥的bit要保持一致)
  local signStr = crypto.rsa_sha1_sign("PRIVATE_KEY",io.readFile("/lua/private.key"),2048,"PRIVATE_CRYPT",plainStr)
  log.info("rsaTest.signature",crypto.base64_encode(signStr,slen(signStr))) --此处使用base64_encode转化为可见字符便于对比

```

---



## crypto.rsa_sha1_verify("PUBLIC_KEY",publicKey,keylen,"PUBLIC_CRYPT",text,plainStr)

rsa公钥验签

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|"PUBLIC_KEY"|string|公钥|     |
|publicKey|string|密钥|  |
|keylen|number|密钥长度|1024或2048   |
|"PUBLIC_CRYPT"|string|加密方式|    |
|text|string|待验签的字符串||
|plainStr|string|原始数据|    |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|	bool|验签结果|true         |

**例子**

```lua
  --公钥验签(1024bit或2048bit，这个bit与实际公钥的bit要保持一致)
  local verifyResult = crypto.rsa_sha1_verify("PUBLIC_KEY",io.readFile("/lua/public.key"),2048,"PUBLIC_CRYPT",text,plainStr)
  log.info("rsaTest.verify",verifyResult) --结果为true表示验签通过

```

---



## crypto.xxtea_encrypt(text,key)

xxtea加密算法

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|text|string|待加密字符串|   |
|key|string|密钥|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|	strring|加密/解密数据|   |

**例子**

```lua
local text = "Hello World!";
local key = "07946";
local encrypt_data = crypto.xxtea_encrypt(text, key);
print("testCrypto.xxteaTest","xxtea_encrypt:"..encrypt_data)
local decrypt_data = crypto.xxtea_decrypt(encrypt_data, key);
print("testCrypto.xxteaTest","decrypt_data:"..decrypt_data)

```

---



## crypto.sm3start()

流式sm3算法

**参数**

无

**返回值**

无

**例子**

```lua
local fSm3Obj=crypto.sm3start()
local testTable={"lqlq666lqlq946","07946lq94607946","lq54075407540707946"}
for i=1, #(testTable) do
    fSm3Obj:sm3update(testTable[i])
end
log.info("testCrypto.flowSm3Test",fSm3Obj:sm3finish())

```

---



