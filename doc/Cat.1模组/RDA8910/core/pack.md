@[TOC]

# pack
数据转换
## pack库说明

pack

pack 库支持将一系列数据按照格式字符转化为 lua 字符串或者将 lua 字符串按照格式字符转化成
一系列值

格式字符串格式如下:

[endianness]< format specifier >[count]

endianness：字节序

- ‘<’ 小字节序，最低有效字节优先，更低的字节有效位占据着更低地址的内存空间。
- ‘>’ 大字节序，最高有效字节优先，更高的字节有效位占据着更低地址的内存空间。
- ‘=’ 自然字节序，默认。

format specifier：参照下面格式化符号

count：取字节个数

| 格式化符号 | 变量类型                                   |
| ---------- | ------------------------------------------ |
| ‘z’        | 以’\0’结尾的字符串                         |
| ‘p’        | 在string数据前面加一个字节的string长度数据 |
| ‘P’        | 在string数据前面加2个字节的string长度数据  |
| ‘a’        | 在string数据前面加4个字节的string长度数据  |
| ‘A’        | 字符串(string)                             |
| ‘f’        | 浮点数(float)                              |
| ‘d’        | 双精度浮点数(double)                       |
| ‘n’        | Lua数字(Lua number)                        |
| ‘c’        | 字符(char)                                 |
| ‘b’        | 字节(byte = unsigned char)                 |
| ‘h’        | 短整型(short，两字节)                      |
| ‘H’        | 无符号短整型(unsigned short，两字节)       |
| ‘i’        | 整型(int，四字节)                          |
| ‘I’        | 无符号整型(unsigned int，四字节)           |
| ‘l’        | 长整型(long，八字节)                       |
| ‘L’        | 无符号长整型(unsigned long，八字节)        |

---



## pack.unpack( string, format,[ init ] )

解包字符串

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|string|string|需解包的字符串|  |
|format|string|格式化符号|  |
|init[opt=1]|number|默认值为1，标记解包开始的位置|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|nextpos|number|字符串标记的位置|   |
|val1|number|第一个解包的值|  |

---



## pack.pack( format, val1, val2, ...valn )

打包字符串的值,在pack的时候有符号 无符号的输出结果都是一样的 unpack时有符号跟无符号才有区别

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|format|string|格式化符号|  |
|val1|number|第一个需打包的值|  |
|val2|number|第二个需打包的值|   |
|valn|number|第n个需打包的值|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|一个包含所有格式化变量的字符串|   |

**例子**

```lua
--print("pcak.pack test：")
--print(pack.pack("A",10))--当"10"以字符串形式包装时，会打印出“10”
--print(common.binstohexs(pack.pack("b",0x10)))--将0x01以十六进制打包为字符串，然后用十六进制输出0x10
--print(pack.pack("A","LUAT"))

```

---



