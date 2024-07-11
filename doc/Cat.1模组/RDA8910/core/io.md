@[TOC]

# io
文件操作接口
## io.exists(path)

判断文件是否存在

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|path|string|文件全名|例如：“/ldata/call.mp3”   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|bool|bool,存在为true,不存在为false|1/0  |

**例子**

```lua
local ex = io.exists("/ldata/call.mp3")

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1956 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2172 "示例")

---



## io.readFile(path)

读取文件并返回文件的内容

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|path|string|文件全名|例如：“/ldata/call.txt”   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|string,文件的内容|文件不存在返回nil  |

**例子**

```lua
local ex = io.readFile("/ldata/call.mp3")

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1956 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2172 "示例")

---



## io.writeFile(path, content, mode)

写入文件指定的内容,默认为覆盖二进制模式

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|path|string|文件全名|例如：“/ldata/call.txt”   |
|path|string|content,文件内容|    |
|path|string|mode,文件写入模式|默认"w+b",支持：<br/>"w"或者"w+b"：空文件写入模式，<br/>如果文件不存在，则新建文件，然后从起始位置开始写入；<br/>如果文件存在，则删除已有内容，然后从起始位置开始写入<br/><br/>         "a"或者"a+b"：追加写入模式，<br/>如果文件不存在，则新建文件，然后从起始位置开始写入；<br/>如果文件存在，则从文件末尾开始追加写入  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|boolean|文件写入结果,true写入成功；false写入失败|1/0  |

**例子**

```lua
local c = io.writeFile("/ldata/call.txt","test")

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1956 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2172 "示例")

---



## io.pathInfo(path)

将文件路径分解为table信息

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|path|string|文件全名|例如：“/ldata/call.txt”   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|table|{dirname=“/ldata/”,filename=“call.txt”,basename=“call”,extname=“.txt”}| |

**例子**

```lua
local p = io.pathInfo("/ldata/call.txt")

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1956 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2172 "示例")

---



## io.fileSize(path)

返回文件大小

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|path|string|文件全名|例如：“/ldata/call.txt”   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|number|文件大小|  |

**例子**

```lua
local cnt = io.fileSize("/ldata/call.txt")

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1956 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2172 "示例")

---



## io.readStream(path, offset, len)

返回指定位置读取的字符串

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|path|string|文件全名|例如：“/ldata/call.txt”  |
|offset|number|要读取的指定位置，相对于文件开头的偏移位置| |
|len|number|要读取的字节数| |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|返回要读取的数据|读取失败返回nil |

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1956 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2172 "示例")

---



## io.opendir(path)

打开文件系统目录

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|path|string|文件系统目录路径|字符串|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|number|  1：表示成功，0：表示失败|1/0|

**例子**

```lua
--[[
  --当需要打开SD 卡 目录时
  io.opendir(“/sdcard0”)
]]

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1936 "指南")  [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2192 "示例")

---



## io.readdir()

读取目录信息

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|number|文件类型|  |
|res|string|文件名称|  |
|res|number|文件大小|  |

**例子**

```lua
--[[
  --如果成功会返回三个参数，分别是文件类型，文件名称，文件大小（如果还是目录则为-1，无实际意义；如果是文件，则是文件实际大小）,如果失败或者读取完成返回空（nil）
  E_FS_ATTR_DEFAULT     = 0,
  // read-only 
  E_FS_ATTR_RO          = 1,
  // hidden 
  E_FS_ATTR_HIDDEN      = 2,
  // system 
  E_FS_ATTR_SYSTEM      = 4, 
  // volume label 
  E_FS_ATTR_VOLUME      = 8,
  // directory 
  E_FS_ATTR_DIR         = 16,
  // archived 
  E_FS_ATTR_ARCHIVE     = 32,
]]

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1936 "指南")  [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2192 "示例")

---



## io.closedir()

关闭文件系统目录

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|number| 1：表示成功，0：表示失败|1/0 |

**例子**

```lua
--[[
  --必须关闭才能再次打开目录
]]

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1936 "指南")  [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2192 "示例")

---



## io.mount(flashType[,path][,size][,offset][,clock],[isfu],[fatclock])

挂载文件系统分区

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|flashType|number|//SD卡<br/>//内部flash<br/>//外挂flash, LCD复用管脚，V_LCD供电<br/>//外挂flash, 使用GPIO pin脚复用，V_PAD_1V8供电|//io.SDCARD<br/>//io.INTERNAL<br/>//io.EXTERN_PINLCD<br/>//io.EXTERN_PINGPIO	 |
|path|string|字符串长度>=5第一个字节为'/'|mount的文件系统根目录|
|size|string|要考虑字节对齐|分区的大小|
|offset|string|flash 地址偏移量|  |
|clock|string|spi传输速率|clock=166M/clkDiv，2<clkDiv<255,默认40000000|
|isfu|boole|lcd外挂flash选择文件系统|fals：fs文件系统<br/>true：fat文件系统(注：速率不高)<br/>|
|fatclock|number|fatspi速率调整|分频系数范围：(clock>=1 && clock < 255)，可选参数默认为1分频，可能不稳定建议实测<br/>|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|number| 1：表示成功，0：表示失败|1/0 |

**例子**

```lua
--
 local fg=io.mount(io.SDCARD)
 local fg=io.mount(io.EXTERN_PINGPIO,"/ext1",0x400000,0x400000,50000000)
--[[
  参数：当flashType为io.SDCARD时，有效参数为flashType。
  当flashType为io.INTERNAL或io.EXTERN_PINLCD或io.EXTERN_PINGPIO时
  有效参数为flashType,path,size,offset,clock。其中path,size为必选参数，
  必须传入有效值，并且size不能为0。

  注意：
  分区path必须大于5字节，并且前面第一个字节为’/‘。多个分区的前五个字节不能相同。
  分区操作的时候size必须考虑字节对齐。
  挂载不上就调用io.format()格式化，就可以读写外挂flash。
]]

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1936 "指南")  [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2192 "示例")

---



## io.unmount(flashType[,path][,size][,offset][,clock])`

卸载文件系统分区

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|flashType|number|//SD卡<br/>//内部flash<br/>//外挂flash, LCD复用管脚，V_LCD供电<br/>//外挂flash, 使用GPIO pin脚复用，V_PAD_1V8供电|//io.SDCARD<br/>//io.INTERNAL<br/>//io.EXTERN_PINLCD<br/>//io.EXTERN_PINGPIO	 |
|path|string|字符串长度>=5第一个字节为'/'|mount的文件系统根目录|
|size|string|要考虑字节对齐|分区的大小|
|offset|string|flash 地址偏移量|  |
|clock|string|spi传输速率|clock=166M/clkDiv，2<clkDiv<255,默认40000000|
|isfu|boole|lcd外挂flash选择文件系统|fals：fs文件系统<br/>true：fat文件系统(注：速率不高)<br/>|
|fatclock|number|fatspi速率调整|分频系数范围：(clock>=1 && clock < 255)，可选参数默认为1分频，可能不稳定建议实测<br/>|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|number| 1：表示成功，0：表示失败|1/0 |

**例子**

```lua
--[[
  参数：
  当flashType为io.SDCARD时，有效参数flashType
  否则有效参数flashType,path,size,offset,clock
  注意：
  分区path必须大于5字节，并且前面第一个字节为’/‘。多个分区的前五个字节不能相同。
  分区操作的时候size必须考虑字节对齐
]]

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1936 "指南")  [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2192 "示例")

---



## io.format(flashType[,path][,size][,offset][,clock])

格式化文件系统分区

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|flashType|number|//SD卡<br/>//内部flash<br/>//外挂flash, LCD复用管脚，V_LCD供电<br/>//外挂flash, 使用GPIO pin脚复用，V_PAD_1V8供电|//io.SDCARD<br/>//io.INTERNAL<br/>//io.EXTERN_PINLCD<br/>//io.EXTERN_PINGPIO	|
|path|string|字符串长度>=5第一个字节为'/'|mount的文件系统根目录|
|size|string|要考虑字节对齐|分区的大小|
|offset|string|flash 地址偏移量|  |
|clock|string|spi传输速率|clock=166M/clkDiv，2<clkDiv<255,默认40000000|
|isfu|boole|lcd外挂flash选择文件系统|fals：fs文件系统<br/>true：fat文件系统(注：速率不高)<br/>|
|fatclock|number|fatspi速率调整|分频系数范围：(clock>=1 && clock < 255)，可选参数默认为1分频，可能不稳定建议实测<br/>|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|number| 1：表示成功，0：表示失败|1/0 |

**例子**

```lua
--
 local fg=io.format(io.EXTERN_PINGPIO,"/ext1",0x400000,0x400000,50000000)
--[[
  参数：
  当flashType为io.SDCARD时，有效参数flashType
  否则有效参数flashType,path,size,offset,clock
  注意：
  分区path必须大于5字节，并且前面第一个字节为’/‘。多个分区的前五个字节不能相同。
  分区操作的时候size必须考虑字节对齐
]]

```
详细指南：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2579 "指南")

---



## io.otp_write(address, buf)

写OTP数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|address|number|地址|0~2048 |
|buf|string|写数据的内容| |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|ret|number| 1：表示成功，0：表示失败|1/0 |

**例子**

```lua
 otp的总大小为2个block，1个block大小为1024
 address+bufsize<=2048
 io.otp_write(0,"1234567890")

```

---



## io.otp_read(address, size)

读OTP数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|address|number|地址|0~2048  |
|size|number|读数据的大小| |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|ret|string|上报数据的内容| |

**例子**

```lua
 otp的总大小为2个block，1个block大小为1024
 address+size<=2048
 io.otp_read(0, 256)

```

---



## io.otp_erase(address, size)

擦OTP数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|address|number|地址|0~2048  |
|size|number|数据的大小| |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|ret|number| 1：表示成功，0：表示失败|1/0 |

**例子**

```lua
 otp的总大小为2个block，1个block大小为1024
 擦的大小以block大小对齐即1024
 擦的数据在一个block内时擦当前block，在两个block内时擦两个block
 io.otp_erase(0, 1024)

```

---



## io.otp_lock(address, size)

锁OTP数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|address|number|地址|0~2048  |
|size|number|数据的大小| |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|ret|number| 1：表示成功，0：表示失败|1/0 |

**例子**

```lua
 otp的总大小为2个block，1个block大小为1024
 锁的大小以block大小对齐即1024
 锁的数据在一个block内时锁当前block，在两个block内时锁两个block
 address+size<=2048
 io.otp_lock(0, 1024)

```

---



## io.write_sfile(path, buf)

写入文件指定的内容(掉电保护)

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|path|string|文件全名|例如：“/ldata/call.txt”  |
|buf|string|写数据的内容| |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|ret|number|数据长度|写入成功返回数据长度，失败返回0|

---





