
@[TOC]

# http

模块功能：HTTP客户端

## http.request(method, url, cert, head, body, timeout, cbFnc, rcvFileName, tCoreExtPara)

发送HTTP请求

* 参数

|名称|传入值类型|释义|
|-|-|-|
|method|string|HTTP请求方法<br>支持"GET"，"HEAD"，"POST"，"OPTIONS"，"PUT"，"DELETE"，"TRACE"，"CONNECT"|
|url|string|HTTP请求url<br>url格式(除hostname外，其余字段可选；目前的实现不支持hash),url中如果包含UTF8编码中文，则需要调用string.rawurlEncode转换成RFC3986编码。<br>|------------------------------------------------------------------------------|<br>| protocol |||   auth    |      host       |           path            | hash  |<br>|----------|||-----------|-----------------|---------------------------|-------|<br>|          |||           | hostname | port | pathname |     search     |       |<br>|          |||           |----------|------|----------|----------------|       |<br>" http[s]  :// user:pass @ host.com : 8080   /p/a/t/h ?  query=string  # hash  "<br>|          |||           |          |      |          |                |       |<br>|------------------------------------------------------------------------------||
|cert|table|**可选参数，默认为`nil`** table或者nil类型，ssl证书，当url为https类型时，此参数才有意义。cert格式如下：<br>{<br>caCert = "ca.crt", --CA证书文件(Base64编码 X.509格式)，如果存在此参数，则表示客户端会对服务器的证书进行校验；不存在则不校验<br>clientCert = "client.crt", --客户端证书文件(Base64编码 X.509格式)，服务器对客户端的证书进行校验时会用到此参数<br>clientKey = "client.key", --客户端私钥文件(Base64编码 X.509格式)<br>clientPassword = "123456", --客户端证书文件密码[可选]<br>}|
|head|table|**可选参数，默认为`nil`** nil或者table类型，自定义请求头<br>http.lua会自动添加Host: XXX、Connection: short、Content-Length: XXX三个请求头<br>如果这三个请求头满足不了需求，head参数传入自定义请求头，如果自定义请求头中存在Host、Connection、Content-Length三个请求头，将覆盖http.lua中自动添加的同名请求头<br>head格式如下：<br>如果没有自定义请求头，传入nil或者{}；否则传入{head1="value1", head2="value2", head3="value3"}，value中不能有\r\n|
|body|param|**可选参数，默认为`nil`** nil、string或者table类型，请求实体<br>如果body仅仅是一串数据，可以直接传入一个string类型的body即可<br><br>如果body的数据比较复杂，包括字符串数据和文件，则传入table类型的数据，格式如下：<br>{<br>[1] = "string1",<br>[2] = {file="/ldata/test.jpg"},<br>[3] = "string2"<br>}<br>例如上面的这个body，索引必须为连续的数字(从1开始)，实际传输时，先发送字符串"string1"，再发送文件/ldata/test.jpg的内容，最后发送字符串"string2"<br><br>如果传输的文件内容需要进行base64编码再上传，请把file改成file_base64，格式如下：<br>{<br>[1] = "string1",<br>[2] = {file_base64="/ldata/test.jpg"},<br>[3] = "string2"<br>}<br>例如上面的这个body，索引必须为连续的数字(从1开始)，实际传输时，先发送字符串"string1"，再发送文件/ldata/test.jpg经过base64编码后的内容，最后发送字符串"string2"|
|timeout|number|**可选参数，默认为`30000`** http请求应答整个过程中，每个子过程的超时时间，单位毫秒，默认为30秒，子过程包括如下两种：<br>1、pdp数据网络激活的超时时间<br>2、http请求发送成功后，分段接收服务器的应答数据，每段数据接收的超时时间|
|cbFnc|function|**可选参数，默认为`nil`** 执行HTTP请求的回调函数(请求发送结果以及应答数据接收结果都通过此函数通知用户)，回调函数的调用形式为：<br>cbFnc(result,prompt,head,body)<br>result：true或者false，true表示成功收到了服务器的应答，false表示请求发送失败或者接收服务器应答失败<br>prompt：string类型，result为true时，表示服务器的应答码；result为false时，表示错误信息<br>head：table或者nil类型，表示服务器的应答头；result为true时，此参数为{head1="value1", head2="value2", head3="value3"}，value中不包含\r\n；result为false时，此参数为nil<br>body：string类型，如果调用request接口时传入了rcvFileName，此参数表示下载文件的完整路径；否则表示接收到的应答实体数据|
|rcvFileName|string|**可选参数，默认为`nil`** string类型时，保存“服务器应答实体数据”的文件名，可以传入完整的文件路径，也可以传入单独的文件名，如果是文件名，http.lua会自动生成一个完整路径，通过cbFnc的参数body传出<br>function类型时，rcvFileName(stepData,totalLen,statusCode)<br>stepData: 本次服务器应答实体数据<br>totalLen: 实体数据的总长度<br>statusCode：服务器的应答码   |
|tCoreExtPara|table|**可选参数，默认为`nil`** table类型{rcvBufferSize=0}修改缓冲空间大小，解决窗口满连接超时问题，单位:字节|

* 返回值

string rcvFilePath，如果传入了rcvFileName，则返回对应的完整路径；其余情况都返回nil

* 例子

```lua
http.request("GET","www.lua.org",nil,nil,nil,30000,cbFnc)
http.request("GET","http://www.lua.org",nil,nil,nil,30000,cbFnc)
http.request("GET","http://www.lua.org:80",nil,nil,nil,30000,cbFnc,"download.bin")
http.request("GET","www.lua.org/about.html",nil,nil,nil,30000,cbFnc)
http.request("GET","www.lua.org:80/about.html",nil,nil,nil,30000,cbFnc)
http.request("GET","http://wiki.openluat.com/search.html?q=123",nil,nil,nil,30000,cbFnc)
http.request("POST","www.test.com/report.html",nil,{Head1="ValueData1"},"BodyData",30000,cbFnc)
http.request("POST","www.test.com/report.html",nil,{Head1="ValueData1",Head2="ValueData2"},{[1]="string1",[2] ={file="/ldata/test.jpg"},[3]="string2"},30000,cbFnc)
http.request("GET","https://www.baidu.com",{caCert="ca.crt"})
http.request("GET","https://www.baidu.com",{caCert="ca.crt",clientCert = "client.crt",clientKey = "client.key"})
http.request("GET","https://www.baidu.com",{caCert="ca.crt",clientCert = "client.crt",clientKey = "client.key",clientPassword = "123456"})
```

---
