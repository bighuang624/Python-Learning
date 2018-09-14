# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
进程和线程
'''



'''
多进程 multiprocessing
'''
# fork() : 创建子进程的系统调用。每调用一次，将当前父进程复制一份子进程，并分别在两个进程中返回一次
# 子进程永远返回 0，而父进程返回子进程的 ID

# Python 的 os 模块封装了包括 fork 在内的常见系统调用
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# multiprocessing 模块 : 跨平台版本的多进程模块
from multiprocessing import Process
import os

def run_proc(name):    # 子进程要执行的代码
    print('RUn child process %s (%s)...' % (name, os.getpgid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))    # 创建子进程时，只需要传入一个执行函数和函数的参数
    print('Child process will start.')
    p.start()    # start() : 启动
    p.join()    # join() : 等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')


# 启动大量子进程时，用进程池的方式批量创建子进程 
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()    # 调用 join() 之前必须先调用 close()，调用 close() 之后就不能继续添加新的 Process 了
    p.join()    # 等待所有子进程执行完毕
    print('All subprocesses done.')

