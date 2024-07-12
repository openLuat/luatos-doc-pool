
@[TOC]

# lbsLoc

模块功能：根据基站信息查询经纬度

## lbsLoc.request(cbFnc, reqAddr, timeout, productKey, host, port, reqTime, reqWifi)

发送基站/WIFI定位请求（仅支持中国区域的位置查询）

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cbFnc|function|用户回调函数，回调函数的调用形式为：<br>cbFnc(result,lat,lng,addr,time,locType)<br>result：number类型<br>0表示成功<br>1表示网络环境尚未就绪<br>2表示连接服务器失败<br>3表示发送数据失败<br>4表示接收服务器应答超时<br>5表示服务器返回查询失败<br>6表示socket已满，创建socket失败<br>为0时，后面的5个参数才有意义<br>lat：string类型或者nil，纬度，整数部分3位，小数部分7位，例如"031.2425864"<br>lng：string类型或者nil，经度，整数部分3位，小数部分7位，例如"121.4736522"<br>addr：目前无意义<br>time：string类型或者nil，服务器返回的时间，6个字节，年月日时分秒，需要转为十六进制读取<br>第一个字节：年减去2000，例如2017年，则为0x11<br>第二个字节：月，例如7月则为0x07，12月则为0x0C<br>第三个字节：日，例如11日则为0x0B<br>第四个字节：时，例如18时则为0x12<br>第五个字节：分，例如59分则为0x3B<br>第六个字节：秒，例如48秒则为0x30<br>locType：numble类型或者nil，定位类型，0表示基站定位成功，255表示WIFI定位成功|
|reqAddr|bool|**可选参数，默认为`nil`** 是否请求服务器返回具体的位置字符串信息，目前此功能不完善|
|timeout|number|**可选参数，默认为`20000`** 请求超时时间，单位毫秒，默认20000毫秒|
|productKey|string|**可选参数，默认为`nil`** IOT网站上的产品证书，如果在main.lua中定义了PRODUCT_KEY变量，则此参数可以传nil|
|host|string|**可选参数，默认为`nil`** 服务器域名，此参数可选，目前仅lib中agps.lua使用此参数。应用脚本可以直接传nil|
|port|string|**可选参数，默认为`nil`** 服务器端口，此参数可选，目前仅lib中agps.lua使用此参数。应用脚本可以直接传nil|
|reqTime|bool|**可选参数，默认为`nil`** 是否需要服务器返回时间信息，true返回，false或者nil不返回，此参数可选，目前仅lib中agps.lua使用此参数。应用脚本可以直接传nil|
|reqWifi|table|**可选参数，默认为`nil`** 搜索到的WIFI热点信息(MAC地址和信号强度)，如果传入了此参数，后台会查询WIFI热点对应的经纬度，此参数格式如下：<br>{<br>["1a:fe:34:9e:a1:77"] = -63,<br>["8c:be:be:2d:cd:e9"] = -81,<br>["20:4e:7f:82:c2:c4"] = -70,<br>}|

* 返回值

nil

* 例子

```lua
lbsLoc.request(cbFnc)
lbsLoc.request(cbFnc,true)
lbsLoc.request(cbFnc,nil,20000)
```

---
