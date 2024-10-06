# 使用Air201的fota脚本进行升级
通过前面从gitee仓库下拉后的代码文件中找到本次需要使用到的fota脚本，位置位于`\LuatOS-Air201\demo\fota`文件夹中，若没有找到该脚本，可能代码并非最新，请根据前面教学重新拉取。

本教程是通过使用`\LuatOS-Air201\demo\fota`下的fota脚本代码对Air201模块进行远程升级操作。操作分为通过合宙iot平台或者通过第三方自建服务器进行远程升级。升级文件可以仅升级脚本文件（script），也可以仅升级底层固件（core），以及脚本文件+底层固件同时升级。

> 固件地址：https://gitee.com/openLuat/LuatOS-Air201/tree/master/core
>
> 脚本地址：https://gitee.com/openLuat/LuatOS-Air201/tree/master/demo/fota

## 1，搭建环境

在Luatools工具项目管理中新建项目，重新选择底层固件和脚本文件。

也可以在原有项目下通过删除旧脚本、添加新脚本的方式进而实现不同功能。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTliMjExMTMxYmRiODk4YTNkOTUzZjEyZTU4ZWExNmRfb3UxUzdyZ2pFNmtSandWQTlSdHROTDUzZHpobVJMOFNfVG9rZW46V1h4WWJjVERWb2pmRm94cnRaNmNsaU9PbnRkXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)

## 2，通过合宙iot平台进行script+core升级

###  2.1 在iot平台创建项目登录[合宙云平台](https://iot.openluat.com/cloud/main)如果没有账号，创建账号新建项目![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=Njg0NWYwZTk1NGZmOGVlODk1Y2M1NzNjNjZmZTRhOTBfV1U0QkVxVlJlZzBscm94TEFwdVdEUkREOW9wTWNnUlFfVG9rZW46Vms3OWJOaUswb3FMeWl4cXloQWNlWWZxbjA1XzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)复制对应项目的PRODUCT_KEY![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NmEwYmZkMTFlNDA1NDNlY2ZmNWM4ODY5MTJkYmRkMzZfcXJhZFozaWk4MHZ1VW1CT3ZQZDROTFRZc2xzczk3TElfVG9rZW46SEQ4a2Jzd1o5b2tSaU94MkN5M2NBdnVkblJjXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)

###  2.2 修改脚本，生成升级文件core说明**core****旧版本core****新版本core**例子LuatOS-SoC_V1003_EC718U.socLuatOS-SoC_V1004_Air201.soc要求大于等于旧版本core版本号新旧版本core支持的功能相同script说明**Script** **main.lua****旧版本** **（模块端本地烧录的）****新版本** **（生成的量产文件，远程升级包）****要求**PROJECT （项目名称）fotademofotademo新旧版本保持一致VERSION （软件版本号）1.0.01.0.1大于等于旧版本 VERSIONPROJECT_KEY （项目密钥）2rzI6QjtNPkMABNmHWL91HjAQHFiDoR72rzI6QjtNPkMABNmHWL91HjAQHFiDoR7和iot平台创建的产品 ProjectKey保持一致

###  2.3 按照新版本需求，修改main.lua

 如下图所示，PROJECT和PRODUCT_KEY保持不变，PRODUCT_KEY需和服务器保持一致，VERSION修改为1.0.1

> 注意事项：1. main.lua 内填写版本号要符合 x.y.z 形式, 其中 x/y/z 均为数值, 不限于个位数；2. 若fota使用合宙iot平台, 版本号中的 y 会被忽略, 推荐写0, 务必留意

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=YmMwZmQ0NWYzYWNjMjUxY2NjNjNhNTIxNTE2ZWY3ZDdfeHVvaURydHdqTVVaUmZtdlcxRGppQzVweDRITVZMWVZfVG9rZW46VTF5RGJqVGtHb2owM2l4elFRa2NxWE9wbnlkXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)

###  2.4 使用Luatools工具生成bin文件差分包注意：只有Luatools版本2.1.89以上支持生成bin文件差分包，低版本仅支持生成sota文件只升级脚本时的差分包制作流程   修改好main.lua后，根据下方图示生成量产文件，其中就包含了bin文件差分包![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NTc0YjRmYzk2ZDYwODIyYTNhOTQyNWRkMGVjMDE3NjlfMmlPSmVleHpMRWtGMHRmalZ1c3dWbTVlbk1EVWxYWG1fVG9rZW46SkY3V2JvVmRyb1FpcG14ODdCbmNyNHBMbmdjXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)  点击生成量产文件后，Luatools工具会根据你选择的目录下自动创建`\SOC量产及远程升级文件\Air201` ，bin文件差分包便在此文件夹里面。![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=YWMxNzBlZGQ4NTMzZDdjZjQ5NDM0ODQwOTBhYzIyY2FfN0NURHppRkxOTXZWWWczYjRRV1M4RjNwRGdIeVFaeWNfVG9rZW46RHlJM2JHenJhb0FvZVN4U1d3Z2M0ODU4bm9mXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)  如果你是只打算进行脚本升级，那么下方固件升级便不用再看了，直接跳转到2.5节即可。需要升级底层固件的差分包制作教程生成新版本的量产固件![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=OGJjMDc5NDlmYjM1Y2E0MzhjYzJhN2JiMTAwNTExNjVfTmFqM3A1VHlwNDJBNmltdndlemVQT0tvNXEwUGpCYWhfVG9rZW46R3plSWJQRzlubzBUeXJ4QTMwOWNqQ1BybkZjXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)根据新旧固件生成bin文件差分包![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NjcwNTk1NzMxMTY0NmE1M2NmNzc5NjgwMzBiNWNiMWVfNE5RTGloTXQ2amlRb0s5M2xYTElaVjZqZktBT2RtcWhfVG9rZW46TlJMMGJQcFNKbzVDY1d4cXB5SmNjNnNrbnBjXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)    箭头所指即为生成的bin文件差分包![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MDg0MmJlNjQzMmY4MmFjN2U0OGUxYzliMDRmZDAyMGRfb242SkNTc2kxcVRjcW93c0tmd3BUYzNvY2ZRZmJvTzBfVG9rZW46UnYzVWJKcmxpb1NWTWR4S3A3WmNmUnhBbm9mXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)

###  2.5 在iot平台配置升级包进入iot平台，打开我的项目->固件列表->创建固件![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=OGI3OGVkMDc3YjU1NzcwZGIwZmFiNjVmM2QzMmY0NmZfUlRLTFpGaEpabktqbGIwTjNza25MdVJMM2o5MzVhaEpfVG9rZW46RDhidGJ6VzJzb2JBVUl4Tk1ZeGNiNFlObjZnXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)选择新固件升级文件   注意：此时的固件名要与模块现在上电后的固件名保持一致，否则会导致远程升级不通过![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=OGIzYzE0OWZlNGQwODU4MzIyMGI4YTdmODk3OTFmOWFfc2NDNzNtTTEwZGJlU1V3eWJpRExMRDBuOEw1eXdwMG1fVG9rZW46QWVYUmJoSUlMb1dzbmx4T204cGNudmxJbmhkXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)如果升级全部设备选项选择的是否，则需要添加指定设备![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTE2NWE2OTViY2EyNTdjNjczNmJjMjQ5MWM4ZjI2YmFfSTBJWnRlMW5NaTFQYVFKY2VRbk05TVdYWnh4MHd0Qk5fVG9rZW46R2RwM2JZZFlIb2g5U3d4UWhaZGNJYkZYblZkXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)

###  2.6 模块开机，完成升级![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ODdjMjE1ODczZGI5YmE3Nzg3MzQwMzVmYTFmNTMyNGZfb0tveWtseUdYTGJaNm9CUndLTVpwVjE2WU4zQzZ2dTBfVG9rZW46SVUzWmJyU2Jqb3NmZ2J4NWJkMWNuZUJvbjdmXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)

## 3，通过第三方自建服务器进行升级

###  3.1 准备模块中使用的旧版本core升级文件![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MjdkMjBjMWU0OWI4YmNlYmU2MmMxMWI5ZjhmNWQ1YTdfMldqNFRyaHdrZ1RPNXE1bmdkU05Rb2FoWGJKVkcydHZfVG9rZW46SlBYTmJwRUgwb25BUTh4dGoyVGM5YmxPblhkXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)

###  3.2 使用Luatools分别生成新旧版本的升级包![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=YTg4ZWVkZjFkYTY1MWYxZDcxY2FjY2VlYjdiNGJjYThfMUVmTFVIN2tLWUp1bU9CaWVZZlVPaXR0OVF2ZjhDdW1fVG9rZW46WW5KYmJ0V09Tb1JicDJ4WUJocWNIcERVblpkXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)  点击生成量产文件后，Luatools工具根据你选择的目录下自动创建`\SOC量产及远程升级文件\Air201` ，生成的升级包便在此文件夹里面。![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=N2ZjNGRiZDk3ZDQwNGFiYTU4MjlkMzZiM2Q0Mzg1ODFfWWRQQWw0Mm9jSFNQcW9OTVNHM2kxcmhXNWtSNVJIdGlfVG9rZW46TFlPTWJtTFI0b3N1QjV4ZU5ORGMydTlzbmJkXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)

###  3.3 使用Luatools工具生成差分文件  使用luatools生成升级文件，无论core是否需要升级，升级文件必须包含core，因为差分会用到，使用luatools内的soc差分工具生成即可。![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=OTBjMjJiNWIxNjI4Nzk0YzQwMDBkMTNkMTdkNTUwNDNfVEVjM3ZkakZRZEc2MklLU0h2MnBEN2FhdzlmQmVXbGdfVG9rZW46UFRsUmJkUHo1b0twR0V4N1RaTWNmSUlWbnhjXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)  生成对应差分包如下图所示，注意差分包大小不能超过480k。![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MmVmYjgwODQ1YmY4NjIzOTA3NzVlYTEyMzc0M2ZhNWJfcDJ2SEFNOTFTWUJuZ29qZnRma1pJcHAzcFJyempQUG1fVG9rZW46UTV0T2JQZ1Vpb1BjeVh4NFhGNmN6c2s4bkhLXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)

###  3.4 差分包上传到第三方自建服务器  lua固件默认支持HTTP获取升级包  在main.lua中做如下修改，打开使用自建服务器进行升级部分代码，填写对应的url![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTBmOWU2YzBjMDBkZTc0MWY2Y2E5ODhjMjgxZjg0ZjdfR2JvZU9oQ3J6b2t5ZGN5Y1VOcG5uZVJaeE13eVVqbDJfVG9rZW46TlZOZ2JPRzFub3VZZnJ4SEgwNmNYVUV4bk9kXzE3MjgxMzY5NDk6MTcyODE0MDU0OV9WNA)

###  3.5 使用其他协议实现自建服务器远程升级

 参考脚本库中配置。无论使用哪种协议，远程升
