#include <semaphore.h>
// 信号量方法
class FooBar {
private:
    int n;
    sem_t fooSemaphore;
    sem_t barSemaphore;

public:
    FooBar(int n) {
        this->n = n;
        sem_init(&fooSemaphore, 0, 1);
        sem_init(&barSemaphore, 0, 0);

    }

    void foo(function<void()> printFoo) {

        for (int i = 0; i < n; i++) {

        	// printFoo() outputs "foo". Do not change or remove this line.
            sem_wait(&fooSemaphore);  // 等待foo的信号
        	printFoo();
            sem_post(&barSemaphore);  // 为bar添加信号
        }
    }

    void bar(function<void()> printBar) {

        for (int i = 0; i < n; i++) {

        	// printBar() outputs "bar". Do not change or remove this line.
            sem_wait(&barSemaphore);
        	printBar();
            sem_post(&fooSemaphore);
        }
    }
};

// 互斥锁
// mutex lock1, lock2
// lock1.lock();  上锁
// lock1.unlock();  解锁

// 条件变量
class FooBar {
private:
    int n;
    mutex mtx;
    condition_variable cv;
    bool foo_done=false;
public:
    FooBar(int n) {
        this->n = n;
    }
    void foo(function<void()> printFoo) {
        for (int i = 0; i < n; i++) {
            unique_lock<mutex>locker(mtx);
            cv.wait(locker,[&](){return foo_done==false;});
            printFoo();
            foo_done=true;
            cv.notify_one();
        }
    }
    void bar(function<void()> printBar) {
        for (int i = 0; i < n; i++) {
            unique_lock<mutex>locker(mtx);
            cv.wait(locker,[&](){return foo_done;});
            printBar();
            foo_done=false;
            cv.notify_one();
        }
    }
};

// 异步操作
class FooBar {
private:
    int n;
    promise<void>readyFoo,readyBar;
    future<void>futureFoo,futureBar;
public:
    FooBar(int n) {
        this->n = n;
        futureFoo=readyFoo.get_future();
        futureBar=readyBar.get_future();
    }
    void foo(function<void()> printFoo) {
        for (int i = 0; i < n; i++) {
            printFoo();
            readyFoo.set_value();
            futureBar.get();
            promise<void>newReadyBar;
            future<void>newFutureBar;
            readyBar=move(newReadyBar);
            newFutureBar=readyBar.get_future();
            futureBar=move(newFutureBar);
        }
    }
    void bar(function<void()> printBar) {
        for (int i = 0; i < n; i++) {
            promise<void>newReadyFoo;
            future<void>newFutureFoo;
            readyFoo=move(newReadyFoo);
            newFutureFoo=readyFoo.get_future();
            futureFoo=move(newFutureFoo);
            printBar();
            readyBar.set_value();
        }
    }
};

// 原子操作（JAVA？）
class FooBar {
private:
    int n;
    atomic<bool>foo_done=false;
public:
    FooBar(int n) {
        this->n = n;
    }
    void foo(function<void()> printFoo) {
        for (int i = 0; i < n; i++) {
            while(foo_done){
                this_thread::yield();
            }
            printFoo();
            foo_done=true;
        }
    }
    void bar(function<void()> printBar) {
        for (int i = 0; i < n; i++) {
            while(foo_done==false){
                this_thread::yield();
            }
            printBar();
            foo_done=false;
        }
    }
};


