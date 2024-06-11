from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooLock = Lock()
        self.fooLock.acquire()  # 确保bar不能执行
        self.barLock = Lock()
        # self.barLock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.barLock.acquire()
            printFoo()
            self.fooLock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.fooLock.acquire()
            printBar()
            self.barLock.release()
