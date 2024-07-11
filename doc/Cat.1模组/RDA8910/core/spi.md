@[TOC]

# spi
spi操作接口
## spi.setup(id,chpa,cpol,dataBits,clock,duplexMode)

spi开启接口

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|SPI的ID，spi.SPI_1表示SPI1，Air720U系列只有SPI1作为普通SPI接口使用，固定传spi.SPI_1即可通道选择|0：普通spi<br/>1:lcdspi|
|chpa|number|0:第一个clk的跳变沿传输数据，1:第二个clk跳变沿传输数据|0/1|
|cpol|number|clock 管脚的默认状态，0表示低电平，1表示高电平|0/1|
|dataBits|number|数据位|8|
|clock|number|spi时钟频率，number数值|110000-100000000|
|duplex|number|只支持全双工|1|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|失败|0|
|result|number|成功|1|

---



## spi.send(id,data[,cscontrol])

spi写数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|SPI的ID，spi.SPI_1表示SPI1，Air720U系列只有SPI1作为普通SPI接口使用，固定传spi.SPI_1即可|0：普通spi<br/>1:lcdspi 复用为普通spi|
|data|string|string类型，要发送的数据|  |
|cscontrol|number|cs是否自动控制,可选参数默认0，1代表CS随数据自动变化，0代表cs先拉低数据结束再恢复|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|写数据的长度|  |

---



## spi.recv(id,length[,cscontrol])

读数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|SPI的ID，spi.SPI_1表示SPI1，Air720U系列只有SPI1作为普通SPI接口使用，固定传spi.SPI_1即可|0：普通spi<br/>1:lcdspi 复用为普通spi|
|length|number|要读取的数据的长度|   |
|cscontrol|number|cs是否自动控制,可选参数默认0，1代表CS随数据自动变化，0代表cs先拉低数据结束再恢复|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|读取的数据内容|  |

---



## spi.send_recv(id,data[,cscontrol])

读写数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|SPI的ID，spi.SPI_1表示SPI1，Air720U系列只有SPI1作为普通SPI接口使用，固定传spi.SPI_1即可|  0：普通spi<br/>1:lcdspi 复用为普通spi |
|data|string|要发送的数据|  |
|cscontrol|number|cs是否自动控制,可选参数默认0，1代表CS随数据自动变化，0代表cs先拉低数据结束再恢复|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|读取的数据内容|  |

---



## spi.close(id)

关闭SPI

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|SPI的ID，spi.SPI_1表示SPI1，Air720U系列只有SPI1作为普通SPI接口使用，固定传spi.SPI_1即可|0：普通spi<br/>1:lcdspi 复用为普通spi|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|失败|0|
|result|number|成功|1|

---



