# -*- coding: utf-8 -*-

# script to build snippets for Xcode.

import os
import time

HOME_DIR = os.environ['HOME']

# Directory of snippets for Xcode
XCODE_SNIPPETS_DIR = os.path.join(
    HOME_DIR, 'Library/Developer/Xcode/UserData/CodeSnippets')

# Backup Directory
date_string = time.strftime("%Y_%m_%d", time.localtime())
BACKUP_DIR = '%s.backup_%s' % (XCODE_SNIPPETS_DIR, date_string)

# Directory of our own snippets
USER_XCODE_SNIPPETS_DIR = os.path.dirname(os.path.abspath(__file__))

# link command
CMD = 'ln -s %s %s' % (
    os.path.join(USER_XCODE_SNIPPETS_DIR, 'CodeSnippets'), XCODE_SNIPPETS_DIR)


def build_snippets():
    if os.path.islink(XCODE_SNIPPETS_DIR):  # remove if existing
        print('Remove link : %s' % XCODE_SNIPPETS_DIR)
        os.remove(XCODE_SNIPPETS_DIR)
    elif os.path.exists(XCODE_SNIPPETS_DIR):  # rename and backup
        print('Rename %s to %s' % XCODE_SNIPPETS_DIR, BACKUP_DIR)
        os.rename(XCODE_SNIPPETS_DIR, BACKUP_DIR)
    print('Create link : %s' % CMD)  
    os.system(CMD)
    print('Done')  


def main():
    build_snippets()


if __name__ == '__main__':
    main()
