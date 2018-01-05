# -*- coding: utf-8 -*-

# script to build snippets for Xcode.

import os
import time

HOME_DIR = os.environ['HOME']

# Xcode 存放代码块的目录
XCODE_SNIPPETS_DIR = os.path.join(
    HOME_DIR, 'Library/Developer/Xcode/UserData/CodeSnippets')

# 备份目录
date_string = time.strftime("%Y_%m_%d", time.localtime())
BACKUP_DIR = '%s.backup_%s' % (XCODE_SNIPPETS_DIR, date_string)

# 个人的代码块目录
USER_XCODE_SNIPPETS_DIR = os.path.dirname(os.path.abspath(__file__))

# 软连接命令
CMD = 'ln -s %s %s' % (
    os.path.join(USER_XCODE_SNIPPETS_DIR, 'CodeSnippets'), XCODE_SNIPPETS_DIR)


def build_snippets():
    if os.path.exists(XCODE_SNIPPETS_DIR)\
         and os.path.isdir(XCODE_SNIPPETS_DIR):
        os.rename(XCODE_SNIPPETS_DIR, BACKUP_DIR)
    os.system(CMD)


def main():
    build_snippets()


if __name__ == '__main__':
    main()
