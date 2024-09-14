# Air780EP的LuatOS使用HTTP指南

## 一. 概述

http是物联网中比较常用的功能，本文介绍如何用Air780EP开发板，了解get/post。
本篇文章通过LuatOS开发来为大家讲解get/post的用法

## 二. 材料准备

1. [[EVB_Air780EP]](https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-24795286339.2.14481170f8sPv8&id=764253232987)开发板一套，包括天线SIM卡，USB线。
2. PC电脑，以及登录官方IOT后台 <https://iot.openluat.com/>
3. 固件和DEMO下载地址 [LuatOS软件包](https://gitee.com/openLuat/LuatOS/releases "LuatOS软件包")
4. 注：使用http库,需要引入**sysplus**库, 且需要在**task内**使用

## 三. API说明


| API接口             | 描述                    |
| :------------------ | ----------------------- |
| http.request()       | get或post一个http客户端 |


## 实现流程

### 1. 创建一个Task协程

**接口**  ​

sys.taskInit(func, arg1, arg2, argN)

**参数**

| 传入值类型 | 解释                                                 |
| ---------- | ---------------------------------------------------- |
| function   | 待执行的函数,可以是匿名函数, 也可以是local或全局函数 |
| any        | 需要传递的参数1,可选                                 |
| any        | 需要传递的参数2,可选                                 |
| any        | 需要传递的参数N,可选                                 |

**返回值**

| 返回值类型 | 解释     |
| ---------- | -------- |
| task       | 协程对象 |

### 2. 等待网络就绪

```lua
if mobile then         -- Air780E/Air600E系列
--mobile.simid(2)
-- LED = gpio.setup(27, 0, gpio.PULLUP)
device_id = mobile.imei()
log.info("ipv6", mobile.ipv6(true)) --因为示例中有链接ipv6网址，所以需要打开此功能
sys.waitUntil("IP_READY", 30000)
```

### 3. 创建一个http实例

**接口**  ​

http.request(method,url,headers,body,opts,ca_file,client_ca, client_key, client_password)

**参数**

| 传入值类型 | 解释                                                         |
| ---------- | ------------------------------------------------------------ |
| string        | 请求方法, 支持 GET/POST 等合法的HTTP方法 |
| string     | url地址, 支持 http和https, 支持域名, 支持自定义端口 |
| tabal        | 请求头 可选 例如 {[“Content-Type”] = “application/x-www-form-urlencoded”} |
| string/zbuff | body 可选 |
| table | 额外配置 可选 包含 timeout:超时时间单位ms 可选,默认10分钟,写0即永久等待 dst:下载路径,可选 adapter:选择使用网卡,可选 debug:是否打开debug信息,可选,ipv6:是否为ipv6 默认不是,可选 callback:下载回调函数,参数 content_len:总长度 body_len:以下载长度 userdata 用户传参,可选 userdata:回调自定义传参 |
| string | 服务器ca证书数据, 可选, 一般不需要 |
| string | 客户端ca证书数据, 可选, 一般不需要, 双向https认证才需要 |
| string | 客户端私钥加密数据, 可选, 一般不需要, 双向https认证才需要 |
| string | 客户端私钥口令数据, 可选, 一般不需要, 双向https认证才需要 |

**返回值**

| 返回值类型 | 解释                                   |
| ---------- | -------------------------------------- |
| int | code , 服务器反馈的值>=100, 最常见的是200.如果是底层错误,例如连接失败, 返回值小于0 |
| tabal | headers 当code>100时, 代表服务器返回的头部数据 |
| string/int | body 服务器响应的内容字符串,如果是下载模式, 则返回文件大小 |

## 示例

本文以**demo_lua\LuatOS\demo\http**这个demo为例作为演示

1. 创建一个Task协程

```lua
sys.taskInit(function()
sys.wait(100)     -- 打印一下支持的加密套件, 通常来说, 固件已包含常见的99%的加密套件
-- if crypto.cipher_suites then
--     log.info("cipher", "suites", json.encode(crypto.cipher_suites()))
-- end
-------------------------------------
-------- HTTP 演示代码 --------------
-------------------------------------
sys.waitUntil("net_ready") -- 等联网
while 1 do
-- 演示GET请求
demo_http_get()
-- 表单提交
-- demo_http_post_form()
-- POST一个json字符串
-- demo_http_post_json()
-- 上传文件, mulitform形式
-- demo_http_post_file()
-- 文件下载
-- demo_http_download()
-- gzip压缩的响应, 以和风天气为例
-- demo_http_get_gzip()
sys.wait(1000)
-- 打印一下内存状态
log.info("sys", rtos.meminfo("sys"))
log.info("lua", rtos.meminfo("lua"))
sys.wait(600000)
end
end)
```

2. 开始演示GET请求

```lua
function demo_http_get()
-- 最普通的Http GET请求
local code, headers, body = http.request("GET", "https://www.air32.cn/").wait()
log.info("http.get", code, headers, body)
local code, headers, body = http.request("GET", "https://mirrors6.tuna.tsinghua.edu.cn/", nil, nil, {ipv6=true}).wait()
log.info("http.get", code, headers, body)
sys.wait(100)
local code, headers, body = http.request("GET", "https://www.luatos.com/").wait()
log.info("http.get", code, headers, body)
-- 按需打印
-- code 响应值, 若大于等于 100 为服务器响应, 小于的均为错误代码
-- headers是个table, 一般作为调试数据存在
-- body是字符串. 注意lua的字符串是带长度的byte[]/char*, 是可以包含不可见字符的
-- log.info("http", code, json.encode(headers or {}), #body > 512 and #body or body)
end
```

**第一个get请求body返回服务器响应的内容字符串**

![image.png](https://cdn.openluat-luatcommunity.openluat.com/images/20240809162951115_image.png)

**第二个服务器暂不支持，所以会返回链接失败**

![image.png](https://cdn.openluat-luatcommunity.openluat.com/images/20240809163258647_image.png)

**第三个get返回结果**

![image.png](https://cdn.openluat-luatcommunity.openluat.com/images/20240809170822667_image.png)

3. 开始演示POST请求

**注：post请求需要将demo_http_post_file()打开**

![image.png](https://cdn.openluat-luatcommunity.openluat.com/images/20240809172802706_image.png)

```lua
function demo_http_post_file()
-- 定义一个局部变量boundary，用于构建multipart/form-data的边界标识符
-- 这里通过当前时间戳来确保boundary的唯一性
local boundary = "----WebKitFormBoundary"..os.time()
-- 设置HTTP请求头，指定内容类型为multipart/form-data，并附上boundary
local req_headers = {
    ["Content-Type"] = "multipart/form-data; boundary="..boundary,
           }
-- 手动拼接multipart/form-data的请求体
-- 包括文件信息（文件名、类型等）和文件内容
local body = "--"..boundary.."\r\n"..
             "Content-Disposition: form-data; name=\"uploadFile\";filename=\"luatos_uploadFile_TEST01.txt\""..
             "\r\nContent-Type: text/plain\r\n\r\n"..
             "1111http_测试一二三四654zacc\r\n"..
             "--"..boundary
-- 打印请求头和请求体，用于调试
log.info("headers: ", "\r\n"..json.encode(req_headers))
log.info("body: ", "\r\n"..body)
-- 发起HTTP POST请求，将文件上传到指定的URL
-- 使用http.request函数，传入方法（POST）、URL、请求头和请求体
-- 然后调用.wait()方法等待请求完成，并获取响应的状态码、响应头和响应体
local code, headers, body = http.request("POST","http://airtest.openluat.com:2900/uploadFileToStatic",
        req_headers,
        body -- POST请求所需要的body
).wait()
-- 打印HTTP响应的状态码、响应头和响应体
log.info("http.post", code, headers, body)
-- 使用postMultipartFormData函数上传文件
-- 这个函数是OpenLuat环境提供的，用于简化multipart/form-data的上传
-- 这里展示了如何定义要上传的文件
postMultipartFormData(
    "http://airtest.openluat.com:2900/uploadFileToStatic",
    {
        -- texts =
        -- {
        --     ["imei"] = "862991234567890",
        --     ["time"] = "20180802180345"
        -- },
        files =
        {
            ["uploadFile"] = "/luadb/luatos_uploadFile.txt",  -- 指定要上传的文件路径
        }
    }
    )

end
```

运行结果：
![image.png](https://cdn.openluat-luatcommunity.openluat.com/images/20240809173625028_image.png)
![image.png](https://cdn.openluat-luatcommunity.openluat.com/images/20240809173716947_image.png)
其他演示案例请看代码详情
