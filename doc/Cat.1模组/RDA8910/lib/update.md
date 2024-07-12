
@[TOC]

# update

模块功能：远程升级.

## update.request(cbFnc, url, period, redir)

启动远程升级功能

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cbFnc|function|**可选参数，默认为`nil`** 每次执行远程升级功能后的回调函数，回调函数的调用形式为：<br>cbFnc(result)，result为true表示升级包下载成功，其余表示下载失败<br>如果没有设置此参数，则升级包下载成功后，会自动重启|
|url|string|**可选参数，默认为`nil`** 使用http的get命令下载升级包的url，如果没有设置此参数，默认使用Luatiot平台的url<br>如果用户设置了url，注意：仅传入完整url的前半部分(如果有参数，即传入?前一部分)，http.lua会自动添加?以及后面的参数，例如：<br>设置的url="www.userserver.com/api/site/firmware_upgrade"，则http.lua会在此url后面补充下面的参数<br>"?project_key=".._G.PRODUCT_KEY<br>.."&imei="..misc.getimei()<br>.."&device_key="..misc.getsn()<br>.."&firmware_name=".._G.PROJECT.."_"..rtos.get_version().."&version=".._G.VERSION<br>如果用户设置了url，且url前面增加三个井号"###",http.lua会自动忽略"###"并以用户填入的url作为请求地址，不会自动添加模块信息，例如：<br>设置的url="###www.userserver.com"/api/site/firmware_upgrade?customparam=test",则http.lua会将此url开头的"###"忽略,并以此url为地址进行请求<br>"www.userserver.com"/api/site/firmware_upgrade?customparam=test"<br>如果redir设置为true，还会补充.."&need_oss_url=1"|
|period|number|**可选参数，默认为`nil`** 单位毫秒，定时启动远程升级功能的间隔，如果没有设置此参数，仅执行一次远程升级功能|
|redir|bool|**可选参数，默认为`nil`** 是否访问重定向到阿里云的升级包，使用Luat提供的升级服务器时，此参数才有意义<br>为了缓解Luat的升级服务器压力，从2018年7月11日起，在iot.openluat.com新增或者修改升级包的升级配置时，升级文件会备份一份到阿里云服务器<br>如果此参数设置为true，会从阿里云服务器下载升级包；如果此参数设置为false或者nil，仍然从Luat的升级服务器下载升级包|

* 返回值

nil

* 例子

```lua
update.request()
update.request(cbFnc)
update.request(cbFnc,"www.userserver.com/update")
update.request(cbFnc,nil,4*3600*1000)
update.request(cbFnc,nil,4*3600*1000,true)
```

---

## update.setDownloadProcessCbFnc(cbFnc)

设置升级包下载过程中的下载进度通知回调函数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cbFnc|function|下载进度通知回调函数，回调函数的调用形式如下：<br>cbFnc(step)<br>step表示下载进度：取值范围是0到100，下载进度更新很快，建议在回调函数中，每隔5或者10执行一次实际动作|

* 返回值

nil

* 例子

```lua
update.setDownloadProcessCbFnc(function(step) end)
```

---

## update.getUpdateMsg()

获取请求升级包时服务器返回的信息

* 参数

无

* 返回值

updateMsg, 若没有请求升级或服务器未返回相关信息，则返回值为nil，否则返回服务器返回的相关信息

* 例子

```lua
local msg = getUpdateMsg()
```

---
