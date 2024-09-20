# 唯一ID

**mcu.unique_id()**接口获取的是真正的唯一ID，如果需要以IMEI作为唯一属性，使用**mobile.imei()**接口获取：[IMEI获取 - 合宙文档中心 (openluat.com)](https://docs.openluat.com/air780e/luatos/app/mobile/info/imei/)

## 获取唯一ID

**mcu.unique_id()**

获取设备唯一id. 注意,可能包含不可见字符,如需查看建议toHex()后打印

```lua
sys.taskInit(function()
	local unique_id = mcu.unique_id()
	log.info("unique_id", unique_id:toHex())
    -- 实例输出：unique_id	4A5139383707942E55FF	20
end)
```
