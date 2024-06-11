// This header is part of the thread support library.
#include <semaphore.h>

class Foo {

protected:
    sem_t firstJobDone;
    sem_t secondJobDone;

public:

    Foo() {
        // 初始化
        // int sem_init(sem_t *sem,int pshared,unsigned int value);
        // pshared，指明信号共享情况（0，进程内的线程共享；非0，进程之间共享，并应该定位共享内存区域）
        // value，设置初始信号量
        // sem_init() 成功时返回 0；错误时，返回 -1，并把 errno 设置为合适的值。
        sem_init(&firstJobDone, 0, 0);
        sem_init(&secondJobDone, 0, 0);
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first".
        printFirst();
        sem_post(&firstJobDone);  // firstJobDone 资源增加1
    }

    void second(function<void()> printSecond) {
        sem_wait(&firstJobDone);  // firstJobDone 资源减少1
        // printSecond() outputs "second".
        printSecond();
        sem_post(&secondJobDone);  // secondJobDone 资源增加1

    }

    void third(function<void()> printThird) {
        sem_wait(&secondJobDone); // secondJobDone 资源减少1
        // printThird() outputs "third".
        printThird();
    }
};
