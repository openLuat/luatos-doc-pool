@[TOC]

# i2c
i2c操作接口
## i2c.setup( id, speed [,slaveaddr] [,isbaud] [,reg16bit])

打开i2c接口

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|i2c接口id|core 0025版本之前，0、1、2都表示i2c2core 0025以及之后的版本，1、2、3分别表示i2c 1、2、3|
|speed|number|时钟频率|0~3500000|
|[,slaveaddr]|number|可选，i2c 外设地址|0x00-0x7f|
|[,isbaud]|number|可选自定义波特率开关 0/1-关闭/开启 |0/1|
|[,reg16bit]|number|双字节寄存器配置开关 0/1-关闭/开启 |0/1|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|可以根据返回的频率值判断是否成功打开i2c|0~3500000|

**例子**

```lua
--使用i2c.send和i2c.recv的setup
if i2c.setup(i2cid,100000) ~= 100000 then
  print("init fail")
  return
end
--自定义i2c波特率(不想指定地址可以将第三个参数置为-1)，波特率自定义开关 第四个参数：1 打开 0 关闭
if i2c.setup(i2cid,2400,-1,1) ~= 2400 then
  print("init fail")
  return
end

--使用i2c.write和i2c.read的setup
if i2c.setup(i2cid,100000,i2cslaveaddr) ~= 100000 then
  print("init1 fail")
  return
end

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1943 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2177 "示例")

---



## i2c.write( id, reg, data )

往指定的寄存器地址 reg 传输数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|i2c接口id|core 0025版本之前，0、1、2都表示i2c2core 0025以及之后的版本，1、2、3分别表示i2c 1、2、3|
|reg|number|写入 i2c 从设备的寄存器起始地址|      |
|data|number|number / string / table，自动根据参数类型写数据，num 只写 1 个字节，string/table|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|传输成功的字节数|   |

**例子**

```lua
local cmd,i = {0x1B,0x00,0x6A,0x01,0x1E,0x20,0x21,0x04,0x1B,0x00,0x1B,0xDA,0x1B,0xDA}
for i=1,#cmd,2 do
  --向从设备的寄存器地址cmd[i]中写1字节的数据cmd[i+1]
  i2c.write(i2cid,cmd[i],cmd[i+1])
end

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/i2c "示例")

---



## i2c.read( id, reg, num )

读取指定寄存器地址 reg 的数据内容

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|i2c接口id|core 0025版本之前，0、1、2都表示i2c2core 0025以及之后的版本，1、2、3分别表示i2c 1、2、3|
|reg|number|读取 i2c 从设备的寄存器起始地址|   |
|num|number|读取数据字节数|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|返回读取的数据|string|二进制数据会包含非可见字符，请使用 string.byte 打印数据流|  |

**例子**

```lua
--从从设备的寄存器地址cmd[i]中读1字节的数据，并且打印出来
    local cmd,i = {0x1B,0x00,0x6A,0x01,0x1E,0x20,0x21,0x04,0x1B,0x00,0x1B,0xDA,0x1B,0xDA}
    for i=1,#cmd,2 do
        --向从设备的寄存器地址cmd[i]中写1字节的数据cmd[i+1]
        i2c.write(i2cid,cmd[i],cmd[i+1])
        --从从设备的寄存器地址cmd[i]中读1字节的数据，并且打印出来
        print("testI2c.init1",string.format("%02X",cmd[i]),string.toHex(i2c.read(i2cid,cmd[i],1)))
    end

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/i2c "示例")

---



## i2c.send( id,slave, data )

向从设备写数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|i2c接口id|core 0025版本之前，0、1、2都表示i2c2core 0025以及之后的版本，1、2、3分别表示i2c 1、2、3|
|slave|number|i2c 外设地址|0x00-0x7f|
|data|number/string/table|自动根据参数类型写数据，num 只写 1 个字节，string/table自动|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|返回读取的数据，二进制数据会包含非可见字符，请使用 string.byte 打印数据流|   |

**例子**

```lua
--从从设备的寄存器地址cmd[i]中读1字节的数据，并且打印出来
    local cmd,i = {0x1B,0x00,0x6A,0x01,0x1E,0x20,0x21,0x04,0x1B,0x00,0x1B,0xDA,0x1B,0xDA}
    for i=1,#cmd,2 do
        --向从设备的寄存器地址cmd[i]中写1字节的数据cmd[i+1]
        i2c.write(i2cid,cmd[i],cmd[i+1])
        --从从设备的寄存器地址cmd[i]中读1字节的数据，并且打印出来
        print("testI2c.init1",string.format("%02X",cmd[i]),string.toHex(i2c.read(i2cid,cmd[i],1)))
    end

```

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1943 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2177 "示例")

---



## i2c.recv( id, slave,size )

向从设备读取数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|i2c接口id,core 0025版本之前，0、1、2都表示i2c2core 0025以及之后的版本，1、2、3分别表示i2c 1、2、3|   |
|slave|number|i2c 外设地址|0x00-0x7f|
|size|number|读取数据字节数|    |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|返回读取的数据，二进制数据会包含非可见字符，请使用 string.byte 打印数据流|   |

**例子**

```lua
--向从设备i2cslaveaddr发送寄存器地址cmd[i]
i2c.send(i2cid,i2cslaveaddr,cmd[i])
--读取从设备i2cslaveaddr寄存器内的1个字节的数据，并且打印出来
print("testI2c.init",string.format("%02X",cmd[i]),string.toHex(i2c.recv(i2cid,i2cslaveaddr,1)))

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1943 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2177 "示例")

---



## i2c.close( id )

关闭 I2C 接口

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|i2c接口id|core 0025版本之前，0、1、2都表示i2c2core 0025以及之后的版本，1、2、3分别表示i2c 1、2、3|

**返回值**

无

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1943 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2177 "示例")

---



