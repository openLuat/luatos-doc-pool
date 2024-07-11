@[TOC]

# zip
zip解压缩（LuatOSVer>=3104）
## zip.open(filename)

打开zip文件，成功时返回一个zfile对象

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|filename|string|zip文件路径|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|zfile|table|zip文件对象|失败时为nil|
|error|string|错误信息|   |

**例子**

```lua
 zfile, err = zip.open("/test.zip")
 zfile:close()

```
参考示例：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/zip "示例")

---



## zfile:close()

关闭用zip.open打开的zfile

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|是否成功|1为成功，0为失败|

**例子**

```lua
 zfile, err = zip.open("/test.zip")
 zfile:close()

```
参考示例：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/zip "示例")

---



## zfile:open(filename)

打开一个存储在zip.open打开的zip文件中的文件。

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|filename|string|文件路径|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|file|table|zip文件中的file对象|失败时为nil|
|error|string|错误信息|   |

**例子**

```lua
 zfile, err = zip.open("/test.zip")
 -- a.txt 是test.zip中的一个文件
 file, err = zfile:open("a.txt")
 file:close()
 zfile:close()

```
参考示例：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/zip "示例")

---



## zip.openfile(filename [, extensions])

递归地遍历所有的路径分隔符，查找zip文件。如果找到了一个zip文件，这个函数将使用剩下的路径来打开请求的文件。

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|filename|string|文件路径|   |
|extensions|string|zip文件后缀后缀名，可以不是.zip（可选）|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|zfile|table|zip文件对象|失败时为nil|
|error|string|错误信息|   |

**例子**

```lua
 file, err = zip.openfile("/test/a.txt")
 file:close()

```
参考示例：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/zip "示例")

---



## zfile:files()

返回一个迭代器函数，每次调用都返回zfile中的一个文件的信息

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|files|iterator|zfile中的文件信息|   |

**例子**

```lua
 -- 文件信息的格式为
 -- {
 --   filename, --压缩文件的路径
 --   compressed_size, --压缩后的字节数
 --   uncompressed_size, --压缩前的字节数
 -- }
 zfile, err = zip.open("/test.zip")
 for file in zfile:files() do
   print(file.filename)
 end
 zfile:close()

```
参考示例：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/zip "示例")

---



## file:close()

关闭一个由zfile:open打开的文件。

**参数**

无

**返回值**

无

**例子**

```lua
 zfile, err = zip.open("/test.zip")
 file, err = zfile:open("a.txt")
 file:close()
 zfile:close()

```
参考示例：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/zip "示例")

---



## file:read(format [, number])

根据指定格式去读取文件

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|format|string|读取格式|"*a"为读取整个文件，"*l"为按行读取|
|number|number|读取的最大字节数（可选）|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|读到的内容|读不到时为nil|

**例子**

```lua
 zfile, err = zip.open("/test.zip")
 file, err = zfile:open("a.txt")
 -- 读取全部内容
 print(file:read("*a"))
 file:close()
 zfile:close()

```
参考示例：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/zip "示例")

---



## file:lines()

返回一个迭代器函数，该函数在每次调用时从文件中返回一个新行。

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|iterator|文件中的每一行|   |

**例子**

```lua
 for line in file:lines() do
   print(line)
 end

```
参考示例：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/zip "示例")

---



## file:seek([whence] [, offset])

设置并获取文件位置

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|whence|string|位置|"set"文件开头, "cur"当前位置, "end"文件结尾, 默认为"cur"|
|offset|number|偏移值|默认为0|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|文件位置|   |

**例子**

```lua
 zfile, err = zip.open("/test.zip")
 file, err = zfile:open("a.txt")
 -- 读取全部内容
 print(file:read("*a"))
 file:seek("set")
 print(file:read("*a"))
 file:close()
 zfile:close()

```
参考示例：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/zip "示例")

---



