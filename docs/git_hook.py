#!/usr/bin/python3

import subprocess

from bottle import post, run, template

@post('/api/git_hook')
def index():
    subprocess.check_call(["git", "pull"])
    subprocess.check_call(["python3", "build.py"])
    return "ok"

if __name__ == '__main__':
    index()
    run(host='0.0.0.0', port=8000)
