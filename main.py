# python多进程
import multiprocessing
import random
import time
from multiprocessing import Pool
from multiprocessing import Process


def run(name, t):
    print('%s running' % name)
    # t = random.randrange(1, 5)
    time.sleep(t)
    print(name, 'running end with time', t, 's.')
    return t


def worker(k, q):
    t = 0
    print("processname", k)
    for i in range(int(k)+1):
        x = random.randint(1, 1)
        t += x
    q.put(t)


def func(i):
    return i*i


# def main():
    # """
    # CASE 1: 可以进行多进程运行，但不方便无法回收返回值。
    # """
    # print("Number of CPU is", multiprocessing.cpu_count())
    #
    # p1 = Process(target=run, args=('a', 4, ))  # 必须加,号
    # p2 = Process(target=run, args=('b', 3, ))
    # p3 = Process(target=run, args=('c', 2, ))
    # p4 = Process(target=run, args=('d', 1, ))
    #
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # print('主线程')

# def main():
#     """
#     CASE 2: 通过 multiprocessing.Queue() 回收各个进程的返回值，但缺陷在于不方便排序。
#     """
#     q = multiprocessing.Queue()
#     jobs = []
#     for i in range(10):
#         p = multiprocessing.Process(target=worker, args=(str(i), q))
#         jobs.append(p)
#         p.start()
#
#     for p in jobs:
#         p.join()
#
#     results = [q.get() for j in jobs]
#     print(results)
#     return 0


def main():
    """
    CASE 3: 通过 multiprocessing.pool() 回收各个进程的返回值，方便排序。
    """
    cpu_num = multiprocessing.cpu_count()
    pool = Pool(processes=cpu_num)  # 开5个进程的进程池
    # ret = pool.map(func, list(range(1, cpu_num+1)))
    # print(ret)
    results = []
    for i in range(cpu_num):
        results.append(pool.apply_async(func, (i+1,)))
    pool.close()  # 关闭进程池，表示不能再往进程池中添加进程，需要在join之前调用
    pool.join()  # 等待进程池中的所有进程执行完毕
    print("Sub-process(es) done.")
    for res in results:
        print(res.get())
    return 0


if __name__ == '__main__':
    main()

# 1. 多进程基本模板
# 2. 反馈回收
# 3. 锁
# 4. 通信
# 参考：https://www.cnblogs.com/jiangfan95/p/11439207.html
