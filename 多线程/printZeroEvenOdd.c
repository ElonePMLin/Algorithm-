#include <semaphore.h>
// 信号量方法
class ZeroEvenOdd {
private:
    int n;
    sem_t zeroSem;
    sem_t oddSem;
    sem_t evenSem;

public:
    ZeroEvenOdd(int n) {
        this->n = n;
        sem_init(&zeroSem, 0, 1);
        sem_init(&oddSem, 0, 0);
        sem_init(&evenSem, 0, 0);
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber) {
        for (int i = 1; i <= n; i++) {
            sem_wait(&zeroSem);
            printNumber(0);
            if (i % 2 == 0) {
                sem_post(&evenSem);
            } else {
                sem_post(&oddSem);
            }
        }
    }

    void even(function<void(int)> printNumber) {
        for (int i = 2; i <= n; i += 2) {
            sem_wait(&evenSem);
            printNumber(i);
            sem_post(&zeroSem);
        }
    }

    void odd(function<void(int)> printNumber) {
        for (int i = 1; i <= n; i += 2) {
            sem_wait(&oddSem);
            printNumber(i);
            sem_post(&zeroSem);
        }
    }
};

// 互斥锁+变量控制
class ZeroEvenOdd {
private:
    int n;
    mutex m;
    condition_variable cv;
    int flag = 0;
public:
    ZeroEvenOdd(int n) {
        this->n = n;
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber) {
        for (int i = 1; i <= n; ++i) {
            unique_lock<mutex> lock(m);
            cv.wait(lock, [&] {return flag == 0;});
            printNumber(0);
            if (i % 2 == 0) {
                flag = 2;
            } else {
                flag = 1;
            }
            cv.notify_one();
        }
    }

    void even(function<void(int)> printNumber) {
        for (int i = 2; i <= n; i += 2) {
            unique_lock<mutex> lock(m);
            cv.wait(lock, [&] {return flag == 2;});
            printNumber(i);
            flag = 0;
            cv.notify_one();
        }
    }

    void odd(function<void(int)> printNumber) {
        for (int i = 1; i <= n; i += 2) {
            unique_lock<mutex> lock(m);
            cv.wait(lock, [&] {return flag == 1;});
            printNumber(i);
            flag = 0;
            cv.notify_one();
        }
    }
};

// 原子操作
class ZeroEvenOdd {
private:
    int n;
    atomic<int> flag = 0;
public:
    ZeroEvenOdd(int n) {
        this->n = n;
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber) {
        for (int i = 1; i <= n; ++i) {
            while (flag != 0) {
                this_thread::yield();
            }
            printNumber(0);
            if (i % 2 == 0) {
                flag = 2;
            } else {
                flag = 1;
            }
        }
    }

    void even(function<void(int)> printNumber) {
        for (int i = 2; i <= n; i += 2) {
            while (flag != 2) {
                this_thread::yield();
            }
            printNumber(i);
            flag = 0;
        }
    }

    void odd(function<void(int)> printNumber) {
        for (int i = 1; i <= n; i += 2) {
            while (flag != 1) {
                this_thread::yield();
            }
            printNumber(i);
            flag = 0;
        }
    }
};
