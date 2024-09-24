#!/usr/bin/python3
 # -*- coding: utf-8 -*-

import os, shutil

# 更新产品手册
# for name in os.listdir(os.path.join('..', 'image')):
#     if not name.startswith('airm2m_'):
#         continue
#     print("![产品手册%s](./image/%s)" % (name, name))

# for name in os.listdir("."):
#     if not name.startswith('air'):
#         continue
#     if os.path.exists(os.path.join(name, "luatos", "docs", "product")) :
#         shutil.move(os.path.join(name, "luatos", "docs", "product"), os.path.join("root", "docs", name, "product"))

# 补齐快速入门的索引文档
# for name in os.listdir("."):
#     if not name.startswith('air'):
#         continue
#     if not os.path.exists(os.path.join(name, "luatos", "docs", "quickstart")) :
#         os.makedirs(os.path.join(name, "luatos", "docs", "quickstart"))
#     if not os.path.exists(os.path.join(name, "luatos", "docs", "quickstart", "index.md")) :
#         with open(os.path.join(name, "luatos", "docs", "quickstart", "index.md"), "w", encoding="UTF-8") as fp:
#             fp.write("# " + name + " 快速入门\r\n")
#             fp.write("\r\n")

# 补齐固件下载的文档
for name in os.listdir("."):
    if not name.startswith('air'):
        continue
    if os.path.exists(os.path.join(name, "luatos", "docs")) and not os.path.exists(os.path.join(name, "luatos", "docs", "firmware.md")) :
        with open(os.path.join(name, "luatos", "docs", "firmware.md"), "w", encoding="UTF-8") as fp:
            fp.write("# " + name + " LuatOS固件下载\r\n")
            fp.write("\r\n")

    if os.path.exists(os.path.join(name, "at", "docs")) and not os.path.exists(os.path.join(name, "at", "docs", "firmware.md")) :
        with open(os.path.join(name, "at", "docs", "firmware.md"), "w", encoding="UTF-8") as fp:
            fp.write("# " + name + " AT固件下载\r\n")
            fp.write("\r\n")
