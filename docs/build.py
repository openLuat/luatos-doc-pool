#!/usr/bin/python3
import os, sys, re
import json, shutil
import subprocess

def do_build(path):
    # 读取mkdocs文件
    if not os.path.exists(path) :
        return
    root = os.path.abspath(path)
    # 拷贝产品手册的图片到当前目录
    shutil.copytree("../image", root + "/docs/image", dirs_exist_ok=True)
    # 拷贝自定义主题文件
    shutil.copytree("custom_theme", root + "/custom_theme", dirs_exist_ok=True)
    # 如果是AT文档,且不是Air724UG系列,那就拷贝一下AT手册
    if str(path).endswith("at") or str(path).endswith("at/") :
        if "air724ug" not in path:
            shutil.copytree("../doc/AT开发资料/AT_Command_Manual/docs/Command_List", root + "/docs/Command_List", dirs_exist_ok=True)

    gitroot = os.path.abspath("../../")
    cmd = "docker run --rm -v {}:/opt/gitee/ -w /opt/gitee/luatos-doc-pool/docs/{} registry.cn-beijing.aliyuncs.com/wendal/mkdocs-material build"
    cmd = cmd.format(gitroot, path.replace("\\", "/"))
    try :
        subprocess.check_call(cmd, shell=True)
        if path != "root" :
            os.makedirs("/opt/docs/site/" + path + "/", exist_ok=True)
            shutil.copytree(path + "/site", "/opt/docs/site/" + path + "/", dirs_exist_ok=True)
        else :
            os.makedirs("/opt/docs/site/", exist_ok=True)
            shutil.copytree(path + "/site", "/opt/docs/site/", dirs_exist_ok=True)
    except:
        import traceback
        traceback.print_exc()

def git_hook():
    subprocess.check_call(["git", "pull"])
    for name in os.listdir(".") :
        if os.path.isdir(name) :
            do_build(os.path.join(name, "at"))
            do_build(os.path.join(name, "luatos"))
    # 然后还需要编译跟目录
    do_build("root")

if __name__ == '__main__':
    git_hook()
