- 实现带参数的装饰器
```
def outer(*args, **kwargs):
    def wrap(func):
        def wrap_inner(*args, **kwargs):
            return func(*args, **kwargs)

        return wrap_inner

    return wrap
```
- 进程、线程、协程  
进程是资源分配的最小单位, 独立内存空间, 通信使用管道(Pipe)、命名管道(FIFO)、消息队列(Message Queue) 、信号、信号量(Semaphore) 、共享内存（Shared Memory）；套接字（Socket）  
线程是操作系统调度（CPU调度）执行的最小单位, 共享进程内存，有独立的运行栈和程序计数器  
协程是程序自己管理, 由生成器实现, 共享线程资源, 更轻量
- 写一段简单的异步IO代码  
```
async def main():
    print('hello')
    asyncio.sleep(1)
    print('world')

for i in range(5):
    asyncio.get_event_loop().run_until_complete(main())
```
- tornado实现异步IO
```
class SleepHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(10)
        self.write("")
```
- 数据库连接实现异步IO 
使用异步连接库, mysqldb不支持异步; 自己实现可以使用多线程或者底层实现
- 实现上下文管理器  
with通过__enter__方法初始化，然后在__exit__中做善后以及处理异常
- 文件不关闭会怎么样  
进程关闭会占用的资源会被释放; GC回收后资源也会释放
- GIL
全局解释锁, 某个线程须先拿到GIL才允许进入CPU执行  
当一个线程遇到 I/O 任务时，将释放GIL  
计算密集型线程执行100次解释器的计步(ticks)时(计步可粗略看作Python虚拟机的指令)也会释放GIL(在python3.x中, GIL不使用ticks计数, 改为使用计时器(执行时间达到阈值后, 当前线程释放GIL)  
- 内存管理  
内存计数、垃圾回收、内存池; 小于256字节使用Pymalloc, 大对象用系统malloc; CPython引入分代垃圾回收, 可以销毁不可获取的引用  
- is和==的区别  
is是比较对象标识符即id(a)=id(b), ==是比较对象是否相等即a.\_\_eq\_\_(b)  
- 和None比较为什么用is
None在Python里是个单例对象, 一个变量如果是None, 它一定和None指向同一个内存地址. 而 == None背后调用的是__eq__, 而__eq__可以被重载
- 实现一个单例
```
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kargs):
        if not cls._instance:
            org = super(Singleton, cls)
            cls._instance = org.__new__(cls, *args, **kargs)
        
        return cls._instance
```

