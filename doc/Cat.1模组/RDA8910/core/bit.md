@[TOC]

# bit
位操作支持库
## bit.bnot( value )

取反，等价于C语言中的~

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|需要取反的值|0x0000 0000~0xFFFF FFFF      |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|取反之后的值|0x0000 0000~0xFFFF FFFF   |

**例子**

```lua
--支持32位比特数按位取反
print(bit.bnot(5))--按位取反，输出-6

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2338#API_8 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2171 "示例")

---



## bit.band( val1, val2, ... valn )

与运算，等价于Ｃ语言中的val1 & val2 & … & valn

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|val1|number|第一个参数|       |
|val2|number|第二个参数|   |
|valn|number|第n个参数|    |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|与运算之后的结果|    |

**例子**

```lua
print(bit.band(1,1))--与,--输出1

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2338#API_8 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2171 "示例")

---



## bit.bor( val1, val2, ... valn )

或运算，等价于C里面的val1 | val2 | … | valn

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|val1|number|第一个参数|       |
|val2|number|第二个参数|   |
|valn|number|第n个参数|    |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|或运算之后的结果|    |

**例子**

```lua
print(bit.bor(1,2))--或，--输出3

```

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2338#API_8 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2171 "示例")

---



## bit.bxor( val1, val2, ... valn )

异或运算，等价于C语言中的val1 ^ val2 ^ … ^ valn

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|val1|number|第一个参数|       |
|val2|number|第二个参数|   |
|valn|number|第n个参数|     |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|异或运算之后的结果, 此处为位异或||

**例子**

```lua
print(bit.bxor(2,3,5))--异或结果为4

```

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2338#API_8 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2171 "示例")

---



## bit.lshift( value, shift )

逻辑左移，等价于C语言中的value << shift

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|移位的值|       |
|shift|number|移位的位置|    |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|逻辑左移之后的结果|    |

**例子**

```lua
print(bit.lshift(1,2))--逻辑左移，“100”，输出为4

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2338#API_8 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2171 "示例")

---



## bit.rshift( value, shift )

逻辑右移，等价于C语言中的value >> shift

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|移位的值|       |
|shift|number|移位的位置|    |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|逻辑右移之后的结果|      |

**例子**

```lua
print(bit.rshift(4,2))--逻辑右移，“001”，输出为1

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2338#API_8 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2171 "示例")

---



## bit.arshift( value, shift )

算数右移

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|移位的值|       |
|shift|number|移位的位置|    |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|逻辑右移之后的结果|   |

**例子**

```lua
print(bit.arshift(2,2))--算数右移，左边添加的数与符号有关，输出为0

```

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2338#API_8 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2171 "示例")

---



## bit.bit( position )

左移运算，等价于C语言中的1 << position

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|position|number|移位的位置|    |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|需要移位的位置|    |

**例子**

```lua
print(bit.bit(2))--参数是位数，作用是1向左移动两位，打印出4

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2338#API_8 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2171 "示例")

---



## bit.isset(value, position)

测试位数是否被置1

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|被测试的值|     |
|position|number|被测试的位置|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|true:该位被置1，false:其他|0/其它 |

**例子**

```lua
-- 例子1
print(bit.isset(5,0))--第一个参数是是测试数字，第二个是测试位置。从右向左数0到7。是1返回true，否则返回false，该返回true
-- 例子2
print(bit.isset(5,1))--打印false
-- 例子3
print(bit.isset(5,2))--打印true
-- 例子4
print(bit.isset(5,3))--返回返回false

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2338#API_8 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2171 "示例")

---



## bit.isclear(value, position)

测试位数是否被置0

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|被测试的值|     |
|position|number|被测试的位置|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|true:该位被置0，false:其他|0/其它  |

**例子**

```lua
print(bit.isclear(5,0))--与上面的相反
print(bit.isclear(5,1))
print(bit.isclear(5,2))
print(bit.isclear(5,3))

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2338#API_8 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2171 "示例")

---



## bit.set(value, pos1, pos2, ...posn)

置1

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|基数(需要改变的值)|  |
|pos1|number|第一位置|   |
|pos2|number|第二位置|  |
|posn|number|第n位置|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|置1之后的值|   |

**例子**

```lua
-- 把0的第0，1，2，3位值为1
print(bit.set(0,0,1,2,3))--在相应的位数置1，打印15

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2338#API_8 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2171 "示例")

---



## number=bit.clear(value, pos1, pos2, ...posn)

置0

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|基数（需要改变的值）|  |
|pos1|number|第一位置|   |
|pos2|number|第二位置|  |
|posn|number|第n位置|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|置0之后的值|   |

**例子**

```lua
-- 把5的第0，2位置为0
print(bit.clear(5,0,2)) --在相应的位置置0，打印0

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2338#API_8 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2171 "示例")

---



