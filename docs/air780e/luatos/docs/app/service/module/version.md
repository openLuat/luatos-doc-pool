# 硬件版本

模块远程升级需要上传模块硬件版本，解决和分析某些问题的时候可能也会需要确认模块硬件版本，以下为模块硬件版本的获取方法。

## 获取硬件版本

**hmeta.hwver()**

获取模组的硬件版本号

```lua
sys.taskInit(function()
	log.info("hmeta", hmeta.hwver and hmeta.hwver())
    -- 实例输出：hmeta	A16
end)
```
