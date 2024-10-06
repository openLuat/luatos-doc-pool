# Air201的MQTT功能
<video data-lark-video-uri="drivetoken://B8nTb4

本章开始学习使用Air201模块进行MQTT链接操作，所需要用到的脚本存于`LuatOS-Air201\demo\mqtt`文件夹中，若没有找到该脚本，可能代码并非最新，请根据前面教学重新拉取。

本章教程是通过使用`LuatOS-Air201\demo\mqtt`下的脚本代码对Air201模块进行MQTT链接操作。操作例程包括有MQTT单链接、MQTT多链接、MQTT SSL不带证书链接、MQTT SSL带证书链接，大家可根据自身需求选择对应的例程学习。

> 固件地址：https://gitee.com/openLuat/LuatOS-Air201/tree/master/core
>
> 脚本地址：https://gitee.com/openLuat/LuatOS-Air201/tree/master/demo/mqtt

## 1，搭建环境

###  1.1 Luatools工具

在Luatools工具项目管理中新建项目，重新选择底层固件和脚本文件。

也可以在原有项目下通过删除旧脚本、添加新脚本的方式进而实现不同功能。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NDYzY2RjZjhiZDU4ODEyNDVmOTRmMjQ0N2U5ZDI1MDhfTExtMHV2ck5YemNJNEdpdGxzbGFNMWxFOElHU3pUUW5fVG9rZW46S05ONGJvenpob0dBWUZ4c1hWQWNzV2ZQbm1jXzE3MjgxMzcwNzg6MTcyODE0MDY3OF9WNA)

###  1.2 MQTTX工具

本章教程以MQTTX工具为例进行学习，下载地址为 https://mqttx.app/ ，大家也可以使用其他MQTT工具。现在大家先照着我的操作，我们先把MQTTX工具配置一下。

下载好软件后，根据下方图中操作指示填写信息。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=YTFkY2ZhY2RlZmVjMmVhOTNmMGRiMzZiMjgzZTliYWZfUk96cFMzeVZKYUJqQzFrVmhCVUtsRnFpdXNuZUluZ1dfVG9rZW46RDczN2JZb3Fmb3JJNTh4eFVJRGNWMlNNbnNoXzE3MjgxMzcwNzg6MTcyODE0MDY3OF9WNA)

填写好信息，点击连接。下一步开始添加订阅主题和发布消息主题，看下图，注意主题格式

> 订阅主题格式要求默认为 /luatos/pub/ 加模块的IMEI号，例如 /luatos/pub/864536071785271
>
> 发布主题格式要求默认为 /luatos/pub/ 加模块的IMEI号，例如 /luatos/sub/864536071785271

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MzJhNjA5ODRjOTAyMmMxOTFlYWNkY2IxYmQwNDgxOTlfNU5FYXN0RHNmSVdGQWRaSVRIamQ1VHJCVTg1d0JmdDlfVG9rZW46WFJEUmJFR3Yyb0hUV2l4TFhFM2NIQTJwbnZiXzE3MjgxMzcwNzg6MTcyODE0MDY3OF9WNA)

MQTTX配置已经完成，现在开始正式学习，学成之后便可通过MQTT进行自由通信了，实际效果如下图所示：

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MWQ1YWIzYzVkNzk0NzFlNzQxNmI1NWQ0YjBlODllOTlfR1dkZ29ITWFwYUdmYmhyYzNQcnFyV2ZyYnBFTmtTalRfVG9rZW46TVRMOWJ4aHBIb2tsNUV4RXlBeGNLaHZ0bkhmXzE3MjgxMzcwNzg6MTcyODE0MDY3OF9WNA)

## 2，MQTT单链接示例

###  2.1 main.lua说明

 在main.lua中我们需要调用single_mqtt，代码参考如下：

```Lua
-- LuaTools需要PROJECT和VERSION这两个信息
PROJECT = "mqttdemo"
VERSION = "1.0.0"

--[[
本demo需要mqtt库, 大部分能联网的设备都具有这个库
mqtt也是内置库, 无需require
]]

-- sys库是标配
_G.sys = require("sys")
--[[特别注意, 使用mqtt库需要下列语句]]
_G.sysplus = require("sysplus")

require "single_mqtt"       -- MQTT单链接

-- require "multilink_mqtt"    -- MQTT多链接

-- require "ssl_mqtt"             -- MQTTS SSL链接

-- 用户代码已结束---------------------------------------------
-- 结尾总是这一句
sys.run()
-- sys.run()之后后面不要加任何语句!!!!!
```

###  2.2 single_mqtt.lua说明

 下面将对single_mqtt.lua中的代码进行简单说明，并指导大家修改指定参数，以便顺利进行MQTT单链接操作。

- 在代码开头部分，根据自己的服务器修改指定的参数。
  -   需要注意的是user_name和password在有些服务器上是可以不传入的，或者是对传入的值没有要求限制。

  -   要根据实际服务器要求来填写。

```Lua
--根据自己的服务器修改以下参数
local mqtt_host = "lbsmqtt.airm2m.com"
local mqtt_port = 1884
local mqtt_isssl = false
local client_id = "abc"
local user_name = "user"
local password = "password"

local pub_topic = "/luatos/pub/" .. (mcu.unique_id():toHex())
local sub_topic = "/luatos/sub/" .. (mcu.unique_id():toHex())
```

- 此task实现的是mqtt的连接、订阅消息、发布消息的流程。
  - 要先等待网络就绪之后才可进行mqtt后续操作
  - 待网络就绪之后，根据代码编写情况此时client_id、pub_topic和sub_topic会发生变化，会覆盖掉代码开头部分时的配置，这点需要注意。device_id为模块的IMEI号

```Lua
sys.taskInit(function()
    -- 等待联网
    local ret, device_id = sys.waitUntil("net_ready")
    -- 下面的是mqtt的参数均可自行修改
    client_id = device_id
    pub_topic = "/luatos/pub/" .. device_id
    sub_topic = "/luatos/sub/" .. device_id

    -- 打印一下上报(pub)和下发(sub)的topic名称
    -- 上报: 设备 ---> 服务器
    -- 下发: 设备 <--- 服务器
    -- 可使用mqtt.x等客户端进行调试
    log.info("mqtt", "pub", pub_topic)
    log.info("mqtt", "sub", sub_topic)

    if mqtt == nil then
        while 1 do
            sys.wait(1000)
            log.info("bsp", "本bsp未适配mqtt库, 请查证")
        end
    end

    -------------------------------------
    -------- MQTT 演示代码 --------------
    -------------------------------------

    mqttc = mqtt.create(nil, mqtt_host, mqtt_port, mqtt_isssl)

    mqttc:auth(client_id,user_name,password) -- client_id必填,其余选填
    -- mqttc:keepalive(240) -- 默认值240s
    mqttc:autoreconn(true, 3000) -- 自动重连机制

    mqttc:on(function(mqtt_client, event, data, payload)
        -- 用户自定义代码
        log.info("mqtt", "event", event, mqtt_client, data, payload)
        if event == "conack" then
            -- 联上了
            sys.publish("mqtt_conack")
            mqtt_client:subscribe(sub_topic)--单主题订阅
            -- mqtt_client:subscribe({[topic1]=1,[topic2]=1,[topic3]=1})--多主题订阅
        elseif event == "recv" then
            log.info("mqtt", "downlink", "topic", data, "payload", payload)
            sys.publish("mqtt_payload", data, payload)
        elseif event == "sent" then
            -- log.info("mqtt", "sent", "pkgid", data)
        -- elseif event == "disconnect" then
            -- 非自动重连时,按需重启mqttc
            -- mqtt_client:connect()
        end
    end)

    -- mqttc自动处理重连, 除非自行关闭
    mqttc:connect()
    sys.waitUntil("mqtt_conack")
    while true do
        -- 演示等待其他task发送过来的上报信息
        local ret, topic, data, qos = sys.waitUntil("mqtt_pub", 300000)
        if ret then
            -- 提供关闭本while循环的途径, 不需要可以注释掉
            if topic == "close" then break end
            mqttc:publish(topic, data, qos)
        end
        -- 如果没有其他task上报, 可以写个空等待
        --sys.wait(60000000)
    end
    mqttc:close()
    mqttc = nil
end)
```

- 此task的功能为模块每3秒向服务器发送一次数据

```Lua
-- 这里演示在另一个task里上报数据, 会定时上报数据,不需要就注释掉
sys.taskInit(function()
    sys.wait(3000)
    local data = "123,"
    local qos = 1 -- QOS0不带puback, QOS1是带puback的
    while true do
        sys.wait(3000)
        if mqttc and mqttc:ready() then
            local pkgid = mqttc:publish(pub_topic, data .. os.date(), qos)
        end
    end
end)
```

- 此代码可实现mqtt-uart透传，利用串口工具给服务器发消息或者接收来自服务器的消息
  - 注意要使用串口1，且波特率为9600

```Lua
-- 以下是演示与uart结合, 简单的mqtt-uart透传实现,不需要就注释掉
local uart_id = 1
uart.setup(uart_id, 9600)
uart.on(uart_id, "receive", function(id, len)
    local data = ""
    while 1 do
        local tmp = uart.read(uart_id)
        if not tmp or #tmp == 0 then
            break
        end
        data = data .. tmp
    end
    log.info("uart", "uart收到数据长度", #data)
    sys.publish("mqtt_pub", pub_topic, data)
end)
sys.subscribe("mqtt_payload", function(topic, payload)
    log.info("uart", "uart发送数据长度", #payload)
    uart.write(1, payload)
end)
```

- 此task是通过使用rtos.meminfo()查询内存信息，并进行打印。rtos库详细信息请参考 [RTOS底层操作库](https://wiki.luatos.com/api/rtos.html?highlight=rtos#rtos-meminfo-type) 。

```Lua
sys.taskInit(function ()
    while true do
        sys.wait(3000)
        log.info("lua", rtos.meminfo())
        log.info("sys", rtos.meminfo("sys"))
    end
end)
```

###  2.3 示例效果

 MQTT单链接示例如下图所示，实现效果为模块每3秒向服务器发送一次数据

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=M2RmNmIyMzYyNzJjZDE3MDRlYjM1OGExYTVlYTQxODhfVklnZVk3MUlBWkpCeEY2R3p1MGtjTTI4cE5MWWZmZmRfVG9rZW46R2k1Q2JGN2Frb3FRWHF4SlpFSmNsMWJCbkFiXzE3MjgxMzcwNzg6MTcyODE0MDY3OF9WNA)

前面代码中所提到的mqtt-uart透传实现效果图如下所示：

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=YTJlNjFhNGU2MzFhZDBjZGM4MjM3NmJjODY1MGViMDdfV0FuenkzUDU4dXREMVBCNWwwaHU3Z0lPNWxZUEg5VGlfVG9rZW46WmtZVmJaTFJRb0JBS2t4ODZoZWM1eDVYbnhoXzE3MjgxMzcwNzg6MTcyODE0MDY3OF9WNA)

## 3，MQTT多链接示例

###  3.1 main.lua说明

 在main.lua中我们需要调用multilink_mqtt，代码参考如下：

```Lua
-- LuaTools需要PROJECT和VERSION这两个信息
PROJECT = "mqttdemo"
VERSION = "1.0.0"

--[[
本demo需要mqtt库, 大部分能联网的设备都具有这个库
mqtt也是内置库, 无需require
]]

-- sys库是标配
_G.sys = require("sys")
--[[特别注意, 使用mqtt库需要下列语句]]
_G.sysplus = require("sysplus")

-- require "single_mqtt"       -- MQTT单链接

require "multilink_mqtt"    -- MQTT多链接

-- require "ssl_mqtt"             -- MQTTS SSL链接

-- 用户代码已结束---------------------------------------------
-- 结尾总是这一句
sys.run()
-- sys.run()之后后面不要加任何语句!!!!!
```

###  3.2 multilink_mqtt.lua说明

- 在代码开头部分，大家根据自己的服务器修改指定的参数
  - 特别说明：`client1_pub_topic` 、`client1_sub_topic` 、`client2_pub_topic` 和 `client2_sub_topic` 在后面函数中会再次赋参数，因此会覆盖掉这里的参数，所以大家可以选择不填。
  - ```Lua
    --根据自己的服务器修改以下参数
    local mqtt1_param = {
        mqttc = nil,
        host = "lbsmqtt.airm2m.com",
        port = 1884,
        is_ssl = false,
        clientId = "client1",
        username = "user",
        password = "password"
    }
    
    local mqtt2_param = {
        mqttc = nil,
        host = "lbsmqtt.airm2m.com",
        port = 1884,
        is_ssl = false,
        clientId = "client2",
        username = "user",
        password = "password"
    }
    
    local client1_pub_topic = ""
    local client1_sub_topic = ""
    
    local client2_pub_topic = ""
    local client2_sub_topic = ""
    ```
- 此`create_mqtt`函数主要功能是创建并配置MQTT客户端对象，具体步骤包括：
  - 使用`mqtt.create`创建一个MQTT客户端对象，并将其存储在`mqtt_param`表的`mqttc`字段中。
  - 使用`log.info`打印MQTT客户端的配置信息。
  - 使用`mqttc:auth`进行MQTT三元组配置。
  - 使用`mqttc:autoreconn`配置自动重连机制，`true`表示启动自动重连机制，`3000`为自动重连周期，单位为ms。
  - ```Lua
    -- 创建mqtt客户端对象
    function create_mqtt(mqtt_param)
        mqtt_param["mqttc"] = mqtt.create(nil, mqtt_param["host"], mqtt_param["port"], mqtt_param["is_ssl"])
        
        log.info("mqtt", "mqttc", mqtt_param["host"], mqtt_param["port"], mqtt_param["is_ssl"], mqtt_param["clientId"], mqtt_param["username"], mqtt_param["password"])
    
        mqtt_param["mqttc"]:auth(mqtt_param["clientId"], mqtt_param["username"], mqtt_param["password"]) -- client_id必填,其余选填
        -- mqttc:keepalive(240) -- 默认值240s
        mqtt_param["mqttc"]:autoreconn(true, 3000) -- 自动重连机制
    end
    ```
- 此`mqtt_client1`函数主要功能是创建并配置一个MQTT客户端1（client 1），并链接到指定的MQTT服务器，具体步骤包括：
  - `client1_pub_topic`和`client1_sub_topic`分别定义了客户端1的上报主题和订阅主题，`device_id`为设备的IMEI号。
  - 使用`log.info`函数打印客户端1的上报和下发主题。
  - 使用`create_mqtt`函数创建MQTT客户端1，并传入`mqtt1_param`表中参数。
  - 设置MQTT客户端1的事件回调函数，`event`为事件类型标识，可能出现的值有`"conack"`（连接确认）、`"recv"`（接收消息）、`"sent"`（发送完成）、`"disconnect"`（服务器断开连接）等，再根据不同事件类型执行不同的功能。
  - 调用`connect`方法连接到MQTT服务器。
  - ```Lua
    function mqtt_client1()
        client1_pub_topic = "/luatos/pub/client1/" .. device_id
        client1_sub_topic = "/luatos/sub/client1/" .. device_id
    
        -- 打印一下上报(pub)和下发(sub)的topic名称
        -- 上报: 设备 ---> 服务器
        -- 下发: 设备 <--- 服务器
        -- 可使用mqtt.x等客户端进行调试
        log.info("mqtt1", "pub", client1_pub_topic)
        log.info("mqtt1", "sub", client1_sub_topic)
    
        -- 创建第一个mqtt客户端
        create_mqtt(mqtt1_param)
        mqtt1_param["mqttc"]:on(function(mqtt_client, event, data, payload)
            -- 用户自定义代码
            log.info("mqtt", "event", event, mqtt_client, data, payload)
            if event == "conack" then
                -- 联上了
                sys.publish("mqtt1_conack")
                mqtt_client:subscribe(client1_sub_topic)--单主题订阅
                -- mqtt_client:subscribe({[topic1]=1,[topic2]=1,[topic3]=1})--多主题订阅
            elseif event == "recv" then
                log.info("mqtt", "downlink", "topic", data, "payload", payload)
                sys.publish("mqtt_payload", data, payload)
            elseif event == "sent" then
                -- log.info("mqtt", "sent", "pkgid", data)
            -- elseif event == "disconnect" then
                -- 非自动重连时,按需重启mqttc
                -- mqtt_client:connect()
            end
        end)
        mqtt1_param["mqttc"]:connect()
    end
    ```
- 此`mqtt_client2`函数主要功能是创建并配置一个MQTT客户端2（client 2），并链接到指定的MQTT服务器，代码内容与`mqtt_client1`类似，便不再做介绍了。
  - ```Lua
    function mqtt_client2()
        client2_pub_topic = "/luatos/pub/client2/" .. device_id
        client2_sub_topic = "/luatos/sub/client2/" .. device_id
        
        log.info("mqtt2", "pub", client2_pub_topic)
        log.info("mqtt2", "sub", client2_sub_topic)
    
        -- 创建第二个mqtt客户端2
        create_mqtt(mqtt2_param)
        mqtt2_param["mqttc"]:on(function(mqtt_client, event, data, payload)
            -- 用户自定义代码
            log.info("mqtt", "event", event, mqtt_client, data, payload)
            if event == "conack" then
                -- 联上了
                sys.publish("mqtt2_conack")
                mqtt_client:subscribe(client2_sub_topic)--单主题订阅
                -- mqtt_client:subscribe({[topic1]=1,[topic2]=1,[topic3]=1})--多主题订阅
            elseif event == "recv" then
                log.info("mqtt", "downlink", "topic", data, "payload", payload)
                sys.publish("mqtt_payload", data, payload)
            elseif event == "sent" then
                -- log.info("mqtt", "sent", "pkgid", data)
            -- elseif event == "disconnect" then
                -- 非自动重连时,按需重启mqttc
                -- mqtt_client:connect()
            end
        end)
        mqtt2_param["mqttc"]:connect()
    end
    ```
- 此`sys.taskInit`为主task函数，函数主要功能是初始化刚才那两个MQTT客户端，确保它们能够成功连接到服务器，并进行周期性的发布消息以实现与服务器的通信。代码中还进行了设备联网检查及库的兼容性验证，确保在合适环境下运行。具体步骤包括：
  - 使用`sys.waitUntil`让系统等待网络连接就绪。
  - 使用`mobile.imei()`获取模块IMEI号后赋值给`device_id`作为设备ID。
  - 代码检查是否存在有可用的MQTT库。若不存在，进入一个无限循环，每秒打印一个日志信息，告知用户未找到 MQTT 库。
  - 分别启动两个MQTT客户端，并等待与服务器成功连接的确认。
  - 设定要发布的数据及qos（服务质量）等级，qos为1表示消息至少会被传递一次。
  - 使用一个无限循环，每隔3秒检查MQTT客户端是否准备好，并发送带有时间戳的数据到指定的主题。
  - ```Lua
    -- 主task
    sys.taskInit(function()
        -- 等待联网
        sys.waitUntil("IP_READY")
        
        device_id = mobile.imei()   -- 获取模块的IMEI
        
        -- 检测当前底层core是否有包含mqtt库
        if mqtt == nil then
            while 1 do
                sys.wait(1000)
                log.info("bsp", "本bsp未适配mqtt库, 请查证")
            end
        end
    
        sys.taskInit(mqtt_client1)      -- 创建并连接第一个mqtt客户端
        sys.waitUntil("mqtt1_conack")
    
        sys.taskInit(mqtt_client2)      -- 创建并连接第二个mqtt客户端
        sys.waitUntil("mqtt2_conack")
    
        sys.wait(3000)
        local data = "123,"
        local qos = 1 -- QOS0不带puback, QOS1是带puback的
        while true do
            sys.wait(3000)
            if mqtt1_param["mqttc"] and mqtt1_param["mqttc"]:ready() then
                local pkgid = mqtt1_param["mqttc"]:publish(client1_pub_topic, data .. os.date(), qos)
            end
    
            if mqtt2_param["mqttc"] and mqtt2_param["mqttc"]:ready() then
                local pkgid = mqtt2_param["mqttc"]:publish(client2_pub_topic, data .. os.date(), qos)
            end
        end
        
        -- 主动断开mqtt连接
        -- mqtt1_param["mqttc"]:close()
        -- mqtt1_param["mqttc"] = nil
    
        -- mqtt2_param["mqttc"]:close()
        -- mqtt2_param["mqttc"] = nil
    end)
    ```
- 此`sys.taskInit`的主要功能是每隔3秒打印一次Lua程序和操作系统的内存使用情况。
  - ```Lua
    sys.taskInit(function ()
        -- 循环打印内存占用情况
        while true do
            sys.wait(3000)
            log.info("lua", rtos.meminfo())
            log.info("sys", rtos.meminfo("sys"))
        end
    end)
    ```

###  3.3 示例效果

 Client 1：

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=OGJlOGJhZGZiNGI1ZDY2MzJmNGY4MWU4NjIzNjZhM2ZfUDhJeXFpNmlsT2hPUzN5Z0lTU1hJZGZGeWRBZ21mWE1fVG9rZW46QXl3UmJhU0xNbzFZT1d4Sm9IcWM3UTVlbjRjXzE3MjgxMzcwNzg6MTcyODE0MDY3OF9WNA)

Client 2：

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=YTM3OTk4ZWEzYTBjYTg4YjdhOTRjZWNiZjkwMzBlMjRfOGxQbW1yMWNpdGpSd2FYYWJiWlVLQVpSZUdUVVVZNVFfVG9rZW46WW9uNGJsZFZWb0FYclF4dVh0dWM0Vm9Gbk1nXzE3MjgxMzcwNzg6MTcyODE0MDY3OF9WNA)

##  4，MQTT SSL不带证书链接示例

###  4.1 main.lua说明

 在main.lua中我们需要调用ssl_mqtt，代码参考如下：

```Lua
-- LuaTools需要PROJECT和VERSION这两个信息
PROJECT = "mqttdemo"
VERSION = "1.0.0"

--[[
本demo需要mqtt库, 大部分能联网的设备都具有这个库
mqtt也是内置库, 无需require
]]

-- sys库是标配
_G.sys = require("sys")
--[[特别注意, 使用mqtt库需要下列语句]]
_G.sysplus = require("sysplus")

-- require "single_mqtt"       -- MQTT单链接

-- require "multilink_mqtt"    -- MQTT多链接

require "ssl_mqtt"             -- MQTTS SSL链接

-- 用户代码已结束---------------------------------------------
-- 结尾总是这一句
sys.run()
-- sys.run()之后后面不要加任何语句!!!!!
```

###  4.2 ssl_mqtt.lua说明

- 在代码开头部分，根据自己的服务器修改对应参数。
  - 特别注意，MQTT SSL不带证书链接与带证书链接为同一个文件，我们本节教程是MQTT SSL不带证书链接，因此要将 mqtt_isssl 的值改为 true ，大家可自行参考下方代码进行修改。
  - ```Lua
    --根据自己的服务器修改以下参数
    local mqtt_host = "broker.emqx.io"
    local mqtt_port = 8883
    local mqtt_isssl = true -- 是否使用ssl> false 不加密 | true 无证书加密 | table 有证书加密
    -- 带证书的ssl连接，把证书文件作为脚本文件一起烧录到模块内，就可以用/luadb/路径直接读取
        mqtt_isssl = {
            server_cert = io.readFile("/luadb/broker.emqx.io-ca.crt"),
            client_cert=nil,
            client_key=nil,
            client_password=nil,
            verify=1;
        }
    local client_id = "abc"
    local user_name = "user"
    local password = "password"
    
    local pub_topic = "/luatos/pub/" .. (mcu.unique_id():toHex())
    local sub_topic = "/luatos/sub/" .. (mcu.unique_id():toHex())
    
    local mqttc = nil
    ```
- 其余代码部分就与MQTT单链接示例中的 single_mqtt.lua 代码相同，同样为避免重复信息过多，影响阅读感受，大家可转到 2.2 single_mqtt.lua说明 进行了解。

###  4.3 示例效果

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NjgxOTFkMzFjMDgzMDQ0MmRkYjljY2I2OGZlNWQwZmZfdEZmWmJ4dFluSHBUb210WldvU0ZBNnh2cTg3dVJ2VWRfVG9rZW46RjJCTWJ6YldubzVIdFF4ZmlTRGNvSWVHbkdiXzE3MjgxMzcwNzg6MTcyODE0MDY3OF9WNA)

##  5，MQTT SSL带证书链接示例

###  5.1 main.lua说明

 在main.lua中我们依旧是需要调用ssl_mqtt，代码参考如下：

```Lua
-- LuaTools需要PROJECT和VERSION这两个信息
PROJECT = "mqttdemo"
VERSION = "1.0.0"

--[[
本demo需要mqtt库, 大部分能联网的设备都具有这个库
mqtt也是内置库, 无需require
]]

-- sys库是标配
_G.sys = require("sys")
--[[特别注意, 使用mqtt库需要下列语句]]
_G.sysplus = require("sysplus")

-- require "single_mqtt"       -- MQTT单链接

-- require "multilink_mqtt"    -- MQTT多链接

require "ssl_mqtt"             -- MQTTS SSL链接

-- 用户代码已结束---------------------------------------------
-- 结尾总是这一句
sys.run()
-- sys.run()之后后面不要加任何语句!!!!!
```

###  5.2 ssl_mqtt.lua说明

- 在代码开头部分，依旧需要大家根据自己的服务器进行修改对应参数。
  - 不过需要注意的是，本次是使用MQTT SSL带证书链接，所以需要将 mqtt_isssl 的值改为 table 。
  - 另外需要注意的是，既然是带证书链接，那么肯定是需要准备好证书文件了，大家在使用自己的服务器时，一定要准备好对应的证书文件才行，证书文件建议直接放在 `LuatOS-Air201\demo\mqtt` 文件夹下，证书文件路径根据代码中示例自行修改。
  - 在烧录时，要将证书文件作为脚本文件一同烧录到模块中去，第二章包含有烧录教程，大家可自行参考。
  - ```Lua
    --根据自己的服务器修改以下参数
    local mqtt_host = "broker.emqx.io"
    local mqtt_port = 8883
    -- 无证书加密 和 下面带证书的ssl方式 根据实际需求配置（二选一）
    -- local mqtt_isssl = true    -- 设置为true，为无证书加密
    local mqtt_isssl = {          -- 设置为table类型，带证书的ssl
        -- 把证书文件作为脚本文件一起烧录到模块内，就可以用/luadb/路径直接读取
        server_cert = io.readFile("/luadb/broker.emqx.io-ca.crt"),
        client_cert=nil,
        client_key=nil,
        client_password=nil,
        verify=1;
    }
    local client_id = "abc"
    local user_name = "user"
    local password = "password"
    
    local pub_topic = "/luatos/pub/" .. (mcu.unique_id():toHex())
    local sub_topic = "/luatos/sub/" .. (mcu.unique_id():toHex())
    
    local mqttc = nil
    ```
- 其余代码部分就与MQTT单链接示例中的 single_mqtt.lua 代码相同，为避免重复信息过多，影响阅读感受，大家可转到 2.2 single_mqtt.lua说明 进行了解。

###  5.3 示例效果

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NThjNWZkYjQ3Yjk4OGQ1YmVlMTEzOTZhZGYwOGI4MTBfMmo4VzdqWTN2RldNSU55U2lkQm9vemFXNFZQeURXbXVfVG9rZW46TllFcGJEU094b0dCRU54bjJaS2NFd1lNbjllXzE3MjgxMzcwNzg6MTcyODE0MDY3OF9WNA)

ltEojZUZxiHbGcaa5Fn9c" data-lark-video-mime="video/mp4" data-lark-video-size="5145384" data-lark-video-duration="0" data-lark-video-name="d3e50ea050fdf61bb8d688242b1e10d6.mp4" data-lark-video-width="720" data-lark-video-height="1280"></video>
