import threading,time

def thread_handle(delay):
    for num in range(10):
        time.sleep(delay) #追加延迟操作
        print("[%s] num = %s" % (threading.current_thread().name,num))  #输出提示信息
def main():
    for item in range(10):#通过循环的形式创建线程
        #创建新的线程对象，设置好该线程对象的处理函数以及函数名称，并且配置好线程名称
        thread = threading.Thread(target=thread_handle, args=(1,), name="执行线程 - %s" % item)
        thread.start() #启动线程
    print("主线程的ID： %s、主线程名称：%s " %(threading.current_thread().ident,threading.current_thread().name))
    print("当前活跃的线程个数：%s " % threading.active_count()) #存活的线程个数
    print("当前活跃线程信息： %s " % threading.enumerate())  #线程信息
if __name__ == '__main__':
    main()

