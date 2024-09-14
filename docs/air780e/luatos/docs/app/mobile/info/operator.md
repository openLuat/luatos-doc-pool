# 运营商信息

可以通过查询卡的IMSI的MNC来判断
IMSI共有15位，其结构如下：
MCC+MNC+MSIN ，(MNC+MSIN=NMSI)
MCC：Mobile Country Code，移动国家码，MCC的资源由国际电联(ITU)统一分配和管理，唯一识别移动用户所属的国家，共3位，中国为460;
MNC:Mobile Network Code，移动网络码，共2位，中国移动00、02、04、07、08，中国联通01、06、09，中国电信03、05、11
MSIN:Mobile Subscriber Identification Number共有10位

## 当前SIM卡的IMSI

**mobile.imsi()**

```lua
sys.taskInit(function()
    -- 如果在刚开机就要执行获取，最好先加些延时，防止sim卡刚上电还未准备好，读取失败。
    sys.wait(2000)

    -- 获取IMSI
    -- 对于双卡单待的设备来说,只能获取当前SIM卡的IMSI
    local imsi = mobile.imsi()  
    log.info("sim_imsi", imsi) 
    -- 实例输出：sim_imsi 460081899904186，08说明是中国移动卡
end)
```

## 当遇到获取IMSI失败

可以按照以下情况排查：

### 硬件排查

1. 是否有查入SIM卡
2. SIM卡插入方向是否正确
3. 如果尝试过有其他卡插入可以读取到，就这张sim卡不行。
   - 可以检查下sim金属面是否比较脏、有刮痕，可以用橡皮擦或者少量酒精擦拭。
   - 卡的厚度相对比较薄，可以尝试垫一点卫生纸，缩短接触距离。
4. SIM卡电路设计有问题。可以进入 air780e.cn 打开硬件设计手册，其中包含SIM卡座的设计电路，作为排查参考。

### 软件排查

1. 是否将接口放在刚开机就立即会执行的位置，并且没有加延时。可能会出现模块开机sim卡还未读取到，软件就走到获取IMSI，这个时候就会获取失败。
2. SIM卡插入的sim硬件接口, 且切换到正确的SIM卡槽(开机立即设置,或者进飞行模式设置)

```
SIM0 -> mobile.simid(0)
SIM1 -> mobile.simid(1)

自动选择 -> mobile.simid(2)
```
