#!/usr/bin/python
# -*- coding: utf-8 -*-


# pushd code from
# https://gist.github.com/Tatsh/7131812

import os.path
import subprocess
import shmutil
import os
 
class PushdContext:
    cwd = None
    original_dir = None
 
    def __init__(self, dirname):
        self.cwd = os.path.realpath(dirname)
 
    def __enter__(self):
        self.original_dir = os.getcwd()
        os.chdir(self.cwd)
        return self
 
    def __exit__(self, type, value, tb):
        os.chdir(self.original_dir)
 
def pushd(dirname):
    return PushdContext(dirname)
 
## Example use
# with pushd('./anfplaylists') as ctx:
#     print(ctx.cwd, ctx.original_dir)
# print(os.getcwd())


def call(commandList):
	return subprocess.check_call(commandList)

def shell(shellCommand):
	return subprocess.check_call(shellCommand, shell=True)

# http://stackoverflow.com/questions/814167/easiest-way-to-rm-rf-in-python
def rm_rf(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.exists(path):
        os.remove(path)
