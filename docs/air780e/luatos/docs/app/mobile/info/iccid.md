# ICCID获取

ICCID：Integrate circuit card identity 集成电路卡识别码即[SIM卡号，相当于手机卡的身份证。 ICCID为IC卡的识别号码，共由20位字符组成，其编码格式为：XXXXXX 0MFSS YYGXX XXXX。前六位运营商代码。

## mobile.iccid(id)

获取ICCID

**参数**

| 传入值类型 | 解释                         |
| ---------- | ---------------------------- |
| int        | SIM卡的编号, 例如0, 1, 默认0 |

**返回值**

| 返回值类型 | 解释                  |
| ---------- | --------------------- |
| string     | ICCID值,若失败返回nil |

**例子**

```
log.info("iccid", mobile.iccid()) --898604981022C0254186
```

