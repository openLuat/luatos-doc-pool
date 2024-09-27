# GET请求

    HTTP GET请求是一种用于从指定资源URI（统一资源标识符）请求数据的HTTP方法。它通常用于请求服务器发送资源（如HTML页面、图片等）给客户端，且请求信息包含在URL中。

下面根据demo演示HTTP的GET请求用法，示例代码如下 ([具体demo可以点此链接跳转](https://gitee.com/openLuat/LuatOS/blob/master/demo/http/main.lua))

## 示例

``` lua

function demo_http_get()
    -- 最普通的Http GET请求
    local code, headers, body = http.request("GET", "https://www.air32.cn/").wait()
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

sys.taskInit(function()
    sys.wait(100)
    -- 打印一下支持的加密套件, 通常来说, 固件已包含常见的99%的加密套件
    -- if crypto.cipher_suites then
    --     log.info("cipher", "suites", json.encode(crypto.cipher_suites()))
    -- end

    -------- HTTP 演示代码 --------------
    sys.waitUntil("net_ready") -- 等联网
    while 1 do

        -- 演示GET请求
        demo_http_get()
        sys.wait(1000)
        -- 打印一下内存状态
        log.info("sys", rtos.meminfo("sys"))
        log.info("lua", rtos.meminfo("lua"))
        sys.wait(600000)
    end
end)

```

## 对应log

![780E](./image/http_get.png)