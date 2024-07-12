
@[TOC]

# socketCh395

模块功能：数据链路激活、socketCh395管理(创建、连接、数据收发、状态维护)

## socketCh395.open(para)

初始化CH395模块

* 参数

|名称|传入值类型|释义|
|-|-|-|
|para|table|取值如下：<br>para为table类型，表示以太网的配置参数，参数结构如下：<br>{<br>mode = 1,                            --1表示客户端；2表示服务器；默认为1<br>intPin = pio.P0_22,                  --以太网芯片中断通知引脚<br>rstPin = pio.P0_23,                  --复位以太网芯片引脚<br>clientNum = 6,                       --server可连路数<br>spiCs = pio.P0_23,                   --SPI片选<br>CH395MAC = "84C2E4A82950",           --MAC地址<br>localAddr = "192.168.1.112",         --本机的地址<br>localSubnetMas = "255.255.255.0",    --子网掩码<br>localPort = 1888,                    --server本机的端口<br>spiCs=pio.P0_7,                      --spi片选<br>localGateway = "192.168.1.1",        --本机的网关地址<br>func=function(id, msg, dat)end,      --中断处理函数，处理server中断事件<br>powerFunc=function(state) end        --控制以太网模块的供电开关函数，ret为true开启供电，false关闭供电<br>spi = {spi.SPI_1,0,0,8,800000},      --SPI通道参数，id,cpha,cpol,dataBits,clock，默认spi.SPI_1,0,0,8,800000<br>}|

* 返回值

result 数据接收结果<br>true表示成功<br>false表示失败

* 例子

```lua
socketCh395.open(para)
```

---

## socketCh395.tcp(ssl, cert, tCoreExtPara)

创建基于TCP的socket对象

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ssl|bool|**可选参数，默认为`nil`** 是否为ssl连接，true表示是，其余表示否|
|cert|table|**可选参数，默认为`nil`** 保留参数，ssl功能还未实现。|
|tCoreExtPara|table|**可选参数，默认为`nil`** 建立链接扩展参数<br>{<br>id =0, --server socket索引ID<br>ip ="192.168.1.1", --server socket client ip<br>port ="8000", --server socket client port<br>type ="TCPSERVER", --server socket type<br>localport ="8000", -- socket client port<br>}|

* 返回值

client，创建成功返回socket客户端对象；创建失败返回nil<br>

* 例子

无

---

## socketCh395.udp(localPort)

创建基于UDP的socket对象

* 参数

无

* 返回值

client，创建成功返回socket客户端对象；创建失败返回nil

* 例子

```lua
c = socketCh395.udp()
```

---

## mt:connect(address, port, timeout)

连接服务器

* 参数

|名称|传入值类型|释义|
|-|-|-|
|address|string|服务器地址，支持ip和域名|
|port|param|string或者number类型，服务器端口|
|timeout|number|**可选参数，默认为`120`** 可选参数，连接超时时间，单位秒|

* 返回值

bool result true - 成功，false - 失败
string ,id '0' -- '8' ,返回通道ID编号

* 例子

```lua
socketClient = socketCh395.tcp()
socketClient:connect("www.baidu.com","80")
```

---

## mt:serverSelect(keepAlive, pingreq)

server发送数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|keepAlive|number|**可选参数，默认为`nil`** 服务器和客户端最大通信间隔时间,也叫心跳包最大时间,单位秒|
|pingreq|string|**可选参数，默认为`nil`** 心跳包的字符串|

* 返回值

boole,false 失败，true 表示成功

* 例子

```lua
socketClient = socketCh395.tcp()
socketClient:connect("www.baidu.com","80")
while socketClient:serverSelect() do end
```

---

## mt:asyncSelect(keepAlive, pingreq)

异步发送数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|keepAlive|number|**可选参数，默认为`nil`** 服务器和客户端最大通信间隔时间,也叫心跳包最大时间,单位秒|
|pingreq|string|**可选参数，默认为`nil`** 心跳包的字符串|

* 返回值

boole,false 失败，true 表示成功

* 例子

```lua
socketClient = socketCh395.tcp()
socketClient:connect("www.baidu.com","80")
while socketClient:asyncSelect() do end
```

---

## mt:serverSend(data, timeout)

server缓存待发送的数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|data|string|数据|
|timeout|number|**可选参数，默认为`nil`** 可选参数，发送超时时间，单位秒；为nil时表示不支持timeout|

* 返回值

result true - 成功，false - 失败

* 例子

```lua
socketClient = socketCh395.tcp()
socketClient:connect("www.baidu.com","80")
socketClient:serverSend("12345678")
```

---

## mt:serverRecv()

server接收数据

* 参数

无

* 返回值

data 表示接收到的数据(如果是UDP，返回最新的一包数据；如果是TCP,返回所有收到的数据)<br>""表示未收到数据

* 例子

```lua
socketClient = socketCh395.tcp()
socketClient:connect("www.baidu.com","80")
data = socketClient:serverRecv()
```

---

## mt:asyncSend(data, timeout)

异步缓存待发送的数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|data|string|数据|
|timeout|number|**可选参数，默认为`nil`** 可选参数，发送超时时间，单位秒；为nil时表示不支持timeout|

* 返回值

result true - 成功，false - 失败

* 例子

```lua
socketClient = socketCh395.tcp()
socketClient:connect("www.baidu.com","80")
socketClient:asyncSend("12345678")
```

---

## mt:asyncRecv()

异步接收数据

* 参数

无

* 返回值

data 表示接收到的数据(如果是UDP，返回最新的一包数据；如果是TCP,返回所有收到的数据)<br>""表示未收到数据

* 例子

```lua
socketClient = socketCh395.tcp()
socketClient:connect("www.baidu.com","80")
data = socketClient:asyncRecv()
```

---

## mt:send(data, timeout)

同步发送数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|data|string|数据<br>此处传入的数据长度和剩余可用内存有关，只要内存够用，可以随便传入数据<br>虽然说此处的数据长度没有特别限制，但是调用core中的socket发送接口时，每次最多发送11200字节的数据<br>例如此处传入的data长度是112000字节，则在这个send接口中，会循环10次，每次发送11200字节的数据|
|timeout|number|**可选参数，默认为`120`** 可选参数，发送超时时间，单位秒|

* 返回值

result true - 成功，false - 失败

* 例子

```lua
socketClient = socketCh395.tcp()
socketClient:connect("www.baidu.com","80")
socketClient:send("12345678")
```

---

## mt:recv(timeout, msg, msgNoResume)

同步接收数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|timeout|number|**可选参数，默认为`0`** 可选参数，接收超时时间，单位毫秒|
|msg|string|**可选参数，默认为`nil`** 可选参数，控制socket所在的线程退出recv阻塞状态|
|msgNoResume|bool|**可选参数，默认为`nil`** 可选参数，控制socket所在的线程退出recv阻塞状态<br>false或者nil表示“在recv阻塞状态，收到msg消息，可以退出阻塞状态”，true表示不退出<br>此参数仅lib内部使用，应用脚本不要使用此参数|

* 返回值

result 数据接收结果<br>true表示成功（接收到了数据）<br>false表示失败（没有接收到数据）
data <br>如果result为true，data表示接收到的数据(如果是UDP，返回最新的一包数据；如果是TCP,返回所有收到的数据)<br>如果result为false，超时失败，data为"timeout"<br>如果result为false，msg控制退出，data为msg的字符串<br>如果result为false，socket连接被动断开控制退出，data为"CLOSED"<br>如果result为false，PDP断开连接控制退出，data为"IP_ERROR_IND"
param 如果是msg控制退出，param的值是msg的参数

* 例子

```lua
socketClient = socketCh395.tcp()
socketClient:connect("www.baidu.com","80")
result,data = socketClient:recv(60000,"APP_SOCKET_SEND_DATA")
```

---

## mt:close()

主动关闭并且销毁一个socket

* 参数

无

* 返回值

nil

* 例子

```lua
socketClient = socketCh395.tcp()
socketClient:connect("www.baidu.com","80")
socketClient:close()
```

---

## socketCh395.printStatus()

打印所有socket的状态

* 参数

无

* 返回值

无

* 例子

```lua
socketCh395.printStatus()
```

---
