# 文件上传

    HTTP POST请求在文件上传场景中发挥着关键作用。用户通过POST请求可以将文件数据包含在请求体中发送给服务器，而不是像GET请求那样通过URL传递。这种方式允许上传大量数据，包括各种类型的文件，如图片、视频、文档等。服务器接收到请求后，会解析请求体中的文件数据，并存储到服务器上相应的位置。文件上传是HTTP应用中常见的功能。

下面根据demo演示HTTP文件上传的功能，示例代码如下 ([具体demo可以点此链接跳转](https://gitee.com/openLuat/LuatOS/blob/master/demo/http/main.lua))

## 示例

``` lua
---- MultipartForm上传文件
-- url string 请求URL地址
-- req_headers table 请求头
-- params table 需要传输的数据参数
function postMultipartFormData(url, params)
    local boundary = "----WebKitFormBoundary"..os.time()
    local req_headers = {
        ["Content-Type"] = "multipart/form-data; boundary="..boundary,
    }
    local body = {}

    -- 解析拼接 body
    for k,v in pairs(params) do
        if k=="texts" then
            local bodyText = ""
            for kk,vv in pairs(v) do
                print(kk,vv)
                bodyText = bodyText.."--"..boundary.."\r\nContent-Disposition: form-data; name=\""..kk.."\"\r\n\r\n"..vv.."\r\n"
            end
            table.insert(body, bodyText)
        elseif k=="files" then
            local contentType =
            {
                txt = "text/plain",             -- 文本
                jpg = "image/jpeg",             -- JPG 格式图片
                jpeg = "image/jpeg",            -- JPEG 格式图片
                png = "image/png",              -- PNG 格式图片
                gif = "image/gif",              -- GIF 格式图片
                html = "image/html",            -- HTML
                json = "application/json"       -- JSON
            }

            for kk,vv in pairs(v) do
                if type(vv) == "table" then
                    for i=1, #vv do
                        print(kk,vv[i])
                        table.insert(body, "--"..boundary.."\r\nContent-Disposition: form-data; name=\""..kk.."\"; filename=\""..vv[i]:match("[^%/]+%w$").."\"\r\nContent-Type: "..contentType[vv[i]:match("%.(%w+)$")].."\r\n\r\n")
                        table.insert(body, io.readFile(vv[i]))
                        table.insert(body, "\r\n")
                    end
                else
                    print(kk,vv)
                    table.insert(body, "--"..boundary.."\r\nContent-Disposition: form-data; name=\""..kk.."\"; filename=\""..vv:match("[^%/]+%w$").."\"\r\nContent-Type: "..contentType[vv:match("%.(%w+)$")].."\r\n\r\n")
                    table.insert(body, io.readFile(vv))
                    table.insert(body, "\r\n")
                end
            end
        end
    end
    table.insert(body, "--"..boundary.."--\r\n")
    body = table.concat(body)
    log.info("headers: ", "\r\n" .. json.encode(req_headers), type(body))
    log.info("body: " .. body:len() .. "\r\n" .. body)
    local code, headers, body = http.request("POST",url,
            req_headers,
            body
    ).wait()
    log.info("http.post", code, headers, body)
end

function demo_http_post_file()
    -- -- POST multipart/form-data模式 上传文件---手动拼接
    local boundary = "----WebKitFormBoundary" .. os.time()
    local req_headers = {
        ["Content-Type"] = "multipart/form-data; boundary=" .. boundary,
    }
    local body = "--" .. boundary .. "\r\n" ..
        "Content-Disposition: form-data; name=\"uploadFile\"; filename=\"luatos_uploadFile_TEST01.txt\"" ..
        "\r\nContent-Type: text/plain\r\n\r\n" ..
        "1111http_测试一二三四654zacc\r\n" ..
        "--" .. boundary

    log.info("headers: ", "\r\n" .. json.encode(req_headers))
    log.info("body: ", "\r\n" .. body)
    local code, headers, body = http.request("POST", "http://airtest.openluat.com:2900/uploadFileToStatic",
        req_headers,
        body         -- POST请求所需要的body, string, zbuff, file均可
    ).wait()
    log.info("http.post", code, headers, body)

    -- 也可用postMultipartFormData(url, params) 上传文件
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
                ["uploadFile"] = "/luadb/luatos_uploadFile.txt",
            }
        }
    )
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

        -- post表单提交
        demo_http_post_form()
        sys.wait(1000)
        -- 打印一下内存状态
        log.info("sys", rtos.meminfo("sys"))
        log.info("lua", rtos.meminfo("lua"))
        sys.wait(600000)
    end
end)

```

## 对应log

![780E](./image/http_upload.png)

上传结果：

![780E](./image/upload.png)