# Semaphore(1).acquire() -1，使信号量减1
# Semaphore(0).release() +1，使信号量加1
from threading import Semaphore


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_sem = Semaphore(1)  # 控制 zero() 的执行
        self.even_sem = Semaphore(0)  # 控制 even() 的执行
        self.odd_sem = Semaphore(0)   # 控制 odd() 的执行

    # 输出一个 0
    def zero(self, printNumber):
        for i in range(self.n):
            self.zero_sem.acquire()  # 获取 zero_sem 的信号量，只有当信号量大于 0 时才能继续执行
            printNumber(0)
            if i % 2 == 0:
                self.odd_sem.release()  # 释放 odd_sem 的信号量，允许 odd() 执行
            else:
                self.even_sem.release()  # 释放 even_sem 的信号量，允许 even() 执行

    # 输出一个偶数
    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):
            self.even_sem.acquire()  # 获取 even_sem 的信号量，只有当信号量大于 0 时才能继续执行
            printNumber(i)
            self.zero_sem.release()  # 释放 zero_sem 的信号量，允许 zero() 执行

    # 输出一个奇数
    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):
            self.odd_sem.acquire()  # 获取 odd_sem 的信号量，只有当信号量大于 0 时才能继续执行
            printNumber(i)
            self.zero_sem.release()  # 释放 zero_sem 的信号量，允许 zero() 执行
