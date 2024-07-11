@[TOC]

# socket
socket（套接字）接口是建立和服务器通信的基础数据管道，有了这个接口就可以连接任何服务器，并进行数据通信
## socketcore.sock_conn(type,addr,port[,cert][,recvBufferLen][,insist][,local_port][,hostNameFlag])

建立套接字连接。异步接口，连接结果通过rtos.recv()接口获取的消息返回

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|type|number|套接字类型| 0/1/2/3，TCP/UDP/SSL/RAW|
|addr|string|服务器地址|ip地址字符串，或者域名|
|port|number|服务器端口|取值范围0-65535|
|cert|table|SSL套接字加密信息|可选参数[4]|
|recvBufferLen|number|接收buffer大小|可选参数[5],单位字节,注意: 目前仅TCP和UDP支持,SSL不支持 |
|insist|number|单项认证校验失败是否坚持访问链接，默认连接,可选参数[6]|0/1,否/是|
|local_port|number|本地端口|取值范围0-65535 当非SSL时可选参数[7]|
|hostNameFlag|number|服务器域名是否上报,默认不上报,可选参数[8]|0/1,否/是|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|成功：套接字ID（>=0)，失败：nil|  |

**例子**

```lua
--[[
    cert.hostName       SSL套接字，服务器域名
    cert.caCert         SSL套接字，服务器证书
    cert.clientCert     SSL套接字，客户端证书
    cert.clientKey      SSL套接字，客户端密钥
]]
-- TCP连接
socket_id = socketcore.sock_conn(0, "www.baidu.com", 80)
-- UDP连接
socket_id2 = socketcore.sock_conn(1, "36.7.87.100", 6770)
-- SSL连接
local cert = {hostName = address}
if self.cert then
    if self.cert.caCert then
        if self.cert.caCert:sub(1, 1) ~= "/" then self.cert.caCert = "/lua/" .. self.cert.caCert end
        cert.caCert = io.readFile(self.cert.caCert)
    end
    if self.cert.clientCert then
        if self.cert.clientCert:sub(1, 1) ~= "/" then self.cert.clientCert = "/lua/" .. self.cert.clientCert end
        cert.clientCert = io.readFile(self.cert.clientCert)
    end
    if self.cert.clientKey then
        if self.cert.clientKey:sub(1, 1) ~= "/" then self.cert.clientKey = "/lua/" .. self.cert.clientKey end
        cert.clientKey = io.readFile(self.cert.clientKey)
    end
end
self.id = socketcore.sock_conn(2, address, port, cert)
end

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使socket API，链接为：[socket](https://doc.openluat.com/wiki/21?wiki_page_id=4193 "socket")

---



## socketcore.sock_conn_ext(type,addr,port[,cert][,recvBufferLen][,insist][,local_port][,hostNameFlag])

等同于socketcore.sock_conn()

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|type|number|套接字类型| 0/1/2/3，TCP/UDP/SSL/RAW|
|addr|string|服务器地址|ip地址字符串，或者域名|
|port|number|服务器端口|取值范围0-65535|
|cert|table|SSL套接字加密信息|可选参数[4]|
|recvBufferLen|number|接收buffer大小|可选参数[5],单位字节,注意: 目前仅TCP和UDP支持,SSL不支持|
|insist|number|单项认证校验失败是否坚持访问链接,默认连接,可选参数[6]|0/1,否/是|
|local_port|number|本地端口|取值范围0-65535 当非SSL时可选参数[7]|
|hostNameFlag|number|服务器域名是否上报,默认不上报,可选参数[8]|0/1,否/是|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|成功：套接字ID（>=0)，失败：nil|  |

**例子**

```lua
--[[
    cert.hostName       SSL套接字，服务器域名
    cert.caCert         SSL套接字，服务器证书
    cert.clientCert     SSL套接字，客户端证书
    cert.clientKey      SSL套接字，客户端密钥
]]

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使socket API，链接为：[socket](https://doc.openluat.com/wiki/21?wiki_page_id=4193 "socket")

---



## socketcore.sock_send(socket_id,data)

发送数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|socket_id|number|socketcore.sock_conn函数返回值|取值>=0 |
|data|string|需要发送的数据|string类型|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result1|boolean|0/1,失败/成功|0/1|
|result2|number|0/1/2/...,成功/错误码1/错误码2/...|0/1/2/.../20|

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使socket API，链接为：[socket](https://doc.openluat.com/wiki/21?wiki_page_id=4193 "socket")

---



## socketcore.sock_getremainbuf(socket_id)

读取剩余缓冲区大小

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|socket_id|number|socketcore.sock_conn函数返回值|取值>=0 |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|当前剩余可用缓冲大小|单位b|

---



## socketcore.sock_close(socket_id)

关闭套接字连接。异步接口，关闭结果通过rtos.recv()接口获取的消息返回

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|socket_id|number|socketcore.sock_conn函数返回值|取值>=0|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|boolean| 0/1,失败/成功|0/1|

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使socket API，链接为：[socket](https://doc.openluat.com/wiki/21?wiki_page_id=4193 "socket")

---



## socketcore.sock_recv(socket_id,buff_len)

接收数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|socket_id|number|套接字描述符|取值>=0|
|buff_len|number|接收数据的缓冲区大小|取值>0|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|接收的数据|预留缓冲区首地址|

**例子**

```lua
-- 接收数据
-- socket_id为socketcore.sock_conn返回的套接字描述符
local recv_len = 64
local data = socketcore.sock_recv(socket_id, recv_len)

```此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使socket API，链接为：[socket](https://doc.openluat.com/wiki/21?wiki_page_id=4193 "socket")

---



## socketcore.sock_destroy(socket_id)

释放套接字socketcore.sock_conn分配的内存

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|socket_id|number|socketcore.sock_conn函数返回值|取值>=0|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number| 0/1,失败/成功|0/1|

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使socket API，链接为：[socket](https://doc.openluat.com/wiki/21?wiki_page_id=4193 "socket")

---



## socketcore.sock_setopt(sock_index,level,optname,optval)

socket的属性参数设置

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|sock_index|number|socketcore.sock_conn函数返回值|取值>=0|
|level|number|套接字类型选项|目前支持的level值：socketcore.SOL_SOCKET，socketcore.IPPROTO_TCP|
|optname|number|socket属性|目前支持的值:socketcore.SO_KEEPALIVE，socketcore.TCP_KEEPIDLE，socketcore.TCP_KEEPINTVL，socketcore.TCP_KEEPCNT,socketcore.SO_REUSEADDR|
|optval|number|对应的属性参数值|取值>=0|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1,成功/失败|0/-1|

**例子**

```lua
socketcore.sock_setopt(id,socketcore.SOL_SOCKET, socketcore.SO_KEEPALIVE,1)
--开启保活功能

socketcore.sock_setopt(id,socketcore.IPPROTO_TCP, socketcore.TCP_KEEPIDLE,30)
--在30秒内，链接上无任何数据交互，则发送初始保活探针

socketcore.sock_setopt(id,socketcore.IPPROTO_TCP, socketcore.TCP_KEEPINTVL,60)
--如果保活探针发送失败，60s再次重传

socketcore.sock_setopt(id,socketcore.IPPROTO_TCP, socketcore.TCP_KEEPCNT,3)
--保活探针的最大重传数量为3
end

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使socket API，链接为：[socket](https://doc.openluat.com/wiki/21?wiki_page_id=4193 "socket")

---



