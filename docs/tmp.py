#!/usr/bin/python3
 # -*- coding: utf-8 -*-

import os, shutil

# for name in os.listdir(os.path.join('..', 'image')):
#     if not name.startswith('airm2m_'):
#         continue
#     print("![产品手册%s](./image/%s)" % (name, name))

# for name in os.listdir("."):
#     if not name.startswith('air'):
#         continue
#     if os.path.exists(os.path.join(name, "luatos", "docs", "product")) :
#         shutil.move(os.path.join(name, "luatos", "docs", "product"), os.path.join("root", "docs", name, "product"))

for name in os.listdir("."):
    if not name.startswith('air'):
        continue
    if not os.path.exists(os.path.join(name, "luatos", "docs", "quickstart")) :
        os.makedirs(os.path.join(name, "luatos", "docs", "quickstart"))
    if not os.path.exists(os.path.join(name, "luatos", "docs", "quickstart", "index.md")) :
        with open(os.path.join(name, "luatos", "docs", "quickstart", "index.md"), "w", encoding="UTF-8") as fp:
            fp.write("# " + name + " 快速入门\r\n")
            fp.write("\r\n")
