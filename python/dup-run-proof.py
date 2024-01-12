import os
import time

current_work_dir = os.path.dirname(__file__) # 当前文件所在的目录
LOCKFILE = os.path.join(current_work_dir, __file__ + '.lock')

def check_lock_file():
    if os.path.exists(LOCKFILE):
        print('Script is already running. Exiting...')
        return True
    else:
        with open(LOCKFILE, 'w') as f:
            f.write('lock')
        return False

def remove_lock_file():
    os.remove(LOCKFILE)

if check_lock_file():
    exit()

# 执行脚本的代码片段

remove_lock_file()
