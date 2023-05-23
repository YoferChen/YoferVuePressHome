# 使用multiprocessing模块: 派生Process的子类，重写run方法

import os,time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self):
        Process.__init__(self)  # 初始化父类
    # 重写run方法
    def run(self):
        print("子进程开始>>> pid={0},ppid={1}".format(os.getpid(),os.getppid()))
        time.sleep(2)
        print("子进程终止>>> pid={0}".format(os.getpid()))

def main():
    print("主进程开始>>> pid={}".format(os.getpid()))
    myProcess=MyProcess()
    myProcess.start()  # 调用run方法执行进程（类似java）
    myProcess.join()
    print("主进程{0}终止".format(os.getpid()))

if __name__ == '__main__':
    main()

'''
主进程开始>>> pid=29948
子进程开始>>> pid=13556,ppid=29948
子进程终止>>> pid=13556
主进程29948终止
'''