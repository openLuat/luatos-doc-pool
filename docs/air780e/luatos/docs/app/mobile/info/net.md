# 切换网络

网络切换可以通过进出飞行模式，锁定band，重启协议栈，配置小区重选信号差值门限来进行切换网络。

## 进出飞行模式

如果模块长时间注册不上网络，可以通过进出飞行模式的方式，重新注册网络。

**mobile.flymode(index, enable)**

进出飞行模式，index编号,默认0. 在支持双卡的模块上才会出现0或1的情况。

enable是否设置为飞行模式，true为设置，false为退出,可选。

```lua
sys.taskInit(function()
    -- 如果在刚开机就要执行获取，最好先加些延时，等待网络注册成功
    sys.wait(4000)
    --进入飞行模式   
    log.info("进入飞行模式 ", mobile.flymode(0,true))
    -- 实例输出：I/user.进入飞行模式 	true mobile NETIF_LINK_OFF -> IP_LOSE 

    sys.wait(2000)  
    -- 延时2秒退出飞行模式 
    log.info("退出飞行模式 ", mobile.flymode(0,false)) 
    -- 实例输出：I/user.退出飞行模式 	false mobile NETIF_LINK_ON -> IP_READY
end)
```

## 获取当前使用/支持的band

**mobile.getBand(band)**

获取当前使用/支持的band。band：输出band

## 设置使用的band

**mobile.setBand(band, num)**

设置使用的band。band：输入使用的band，num：band数量。

```lua
sys.taskInit(function()
	local band = zbuff.create(40)
    local band1 = zbuff.create(40)
        
    mobile.getBand(band)
    log.info("当前使用的band:")
    for i=0,band:used()-1 do
        log.info("band", band[i])
    end
    -- 实例输出：当前使用的band: 1 3 5 8 34 38 39 40 41
        
    -- 改成使用38,39,40
    band1[0] = 38
    band1[1] = 39
    band1[2] = 40
    mobile.setBand(band1, 3)
        
    band1:clear()
    mobile.getBand(band1)
    log.info("修改后使用的band:")
    for i=0,band1:used()-1 do
        log.info("band", band1[i])
    end
    -- 实例输出：修改后使用的band: 38 39 40
        
    -- 改回原先使用的band，也可以下载的时候选择清除fs
    mobile.setBand(band, band:used())    

    mobile.getBand(band1)
    log.info("修改回默认使用的band:")
    for i=0,band1:used()-1 do
        log.info("band", band1[i])
    end
	-- 实例输出：修改回默认使用的band: 1 3 5 8 34 38 39 40 41
end)
```

## 重启协议栈

如果模块长时间注册不上网络，可以重启协议栈，重新注册网络。

**mobile.reset()**

```lua
sys.taskInit(function()
    -- 如果在刚开机就要执行获取，最好先加些延时，等待网络注册成功
    sys.wait(4000)
    --进入飞行模式   
    log.info("重启协议栈", mobile.reset())
    -- 实例输出：
    -- 重启协议栈 [10:35:23.554]D/mobile NETIF_LINK_OFF -> IP_LOSE
              --[10:35:25.562]D/mobile NETIF_LINK_ON -> IP_READY
end)
```

## 辅助周期性或者自动功能

**mobile.setAuto（check_sim_period, get_cell_period, search_cell_time, auto_reset_stack, network_check_period）**

设置一些辅助周期性或者自动功能，目前支持SIM卡暂时脱离后恢复，周期性获取小区信息，网络遇到严重故障时尝试自动恢复。

```lua
sys.taskInit(function()
    -- check_sim_period: SIM卡自动恢复时间，单位毫秒，建议5000~10000，和飞行模式/SIM卡切换冲突，不能			再同一时间使用，必须错开执行。写0或者不写则是关闭功能
    -- get_cell_period: 周期性获取小区信息的时间间隔，单位毫秒。获取小区信息会增加部分功耗。写0或者不写则          是关闭功能
    -- search_cell_time: 每次搜索小区时最大搜索时间，单位秒。不要超过8秒
    -- auto_reset_stack: 网络遇到严重故障时尝试自动恢复，和飞行模式/SIM卡切换冲突，true开启，false关		闭，开始状态是false，留空则不做改变
    -- 设置定时检测网络是否正常并且在检测到长时间无网时通过重启协议栈来恢复，无网恢复时长，单位ms，建议            60000以上，为网络搜索网络保留足够的时间，留空则不做更改      
    log.info("辅助周期性或者自动功能", mobile.setAuto(5000,0,8,true,60000))
end)
```

## 网络特殊配置

**mobile.config(item, value)**

```lua
sys.taskInit(function()
--配置小区重选信号差值门限，不能大于15dbm，必须在飞行模式下才能用
mobile.flymode(0,true)
mobile.config(mobile.CONF_RESELTOWEAKNCELL, 15)
--开启网络静态优化        
mobile.config(mobile.CONF_STATICCONFIG, 1) 
mobile.flymode(0,false)
end)
```

## 锁定/解锁小区

**mobile.lockCell(mode, earfcn, pci)**

锁定/解锁小区，仅用于外场测试，没接触过的，或者生产环境中请勿使用

mode: 操作码 0删除优先的频点，1设置优先频点，2锁定小区，3解锁小区

earfcn: 下行频点

pci: phycellid

```lua
sys.taskInit(function()
	mobile.lockCell(2,1860,32)    --锁定小区
	mobile.lockCell(3)            --解锁小区
end)
```
