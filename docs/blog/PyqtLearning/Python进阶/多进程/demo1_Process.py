# 使用multiprocessing模块: 创建Process的实例，传入任务执行函数作为参数

'''
参考：https://blog.csdn.net/weixin_33921444/article/details/112156537
Process常用属性与方法：
    name：进程名
    pid：进程id
    run()：自定义自雷时重写该方法
    start()：开启进程
    join(timeout=None)：阻塞进程【父进程等待子进程结束后才继续执行】
    terminate()：终止进程
    is_alive()：判断进程是否存活
'''

import os, time
from multiprocessing import Process


def worker():
    print('子进程执行>>> pid={0},ppid={1}'.format(os.getpid(), os.getppid()))
    time.sleep(2)
    print('子进程终止>>> pid={0}'.format(os.getpid()))


def main():
    print('主进程执行中>>> pid={0}'.format(os.getpid()))
    ps = []
    # 创建子进程实例
    for i in range(2):
        p = Process(target=worker, name="worker" + str(i), args=())
        ps.append(p)

    # 开启进程
    for i in range(2):
        ps[i].start()

    # 阻塞进程（等待子进程执行结束）
    for i in range(2):
        ps[i].join()
    print('主进程终止')


if __name__ == '__main__':
    main()

'''
# 上述代码执行结果
主进程执行中>>> pid=31200
子进程执行>>> pid=23960,ppid=31200
子进程执行>>> pid=18008,ppid=31200
子进程终止>>> pid=23960
子进程终止>>> pid=18008
主进程终止


# 去掉join()后的执行结果
主进程执行中>>> pid=33848
主进程终止
子进程执行>>> pid=33544,ppid=33848
子进程执行>>> pid=33112,ppid=33848
子进程终止>>> pid=33544
子进程终止>>> pid=33112
'''
