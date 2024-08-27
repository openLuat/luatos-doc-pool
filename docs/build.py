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
    try :
        subprocess.check_call("docker run --rm -v {}:/docs registry.cn-beijing.aliyuncs.com/wendal/mkdocs-material build".format(root), shell=True)
        os.makedirs("/opt/docs/site/" + path + "/", exist_ok=True)
        shutil.copytree(path + "/site", "/opt/docs/site/" + path + "/", dirs_exist_ok=True)
    except:
        import traceback
        traceback.print_exc()

def git_hook():
    subprocess.check_call(["git", "pull"])
    for name in os.listdir(".") :
        if os.path.isdir(name) :
            do_build(os.path.join(name, "at"))
            do_build(os.path.join(name, "luatos"))

from bottle import post, run, template

@post('/api/git_hook')
def index():
    git_hook()
    return "ok"



if __name__ == '__main__':
    git_hook()
    
    if len(sys.argv) > 1 and sys.argv[1] == "web":
        run(host='0.0.0.0', port=8000)
