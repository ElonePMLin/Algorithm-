from threading import Lock


class Foo:
    def __init__(self):
        self.firstEnd = Lock()
        self.secondEnd = Lock()
        self.firstEnd.acquire()  # 获取锁
        self.secondEnd.acquire()  # 获取锁

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstEnd.release()  # 释放锁

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.firstEnd:  # 等待锁被释放 或者 写 self.firstEnd.acquire()  # 获取锁 也可以
            printSecond()
            self.secondEnd.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.secondEnd:  # 等待锁被释放 或者 写 self.secondEnd.acquire()  # 获取锁 也可以
            printThird()
