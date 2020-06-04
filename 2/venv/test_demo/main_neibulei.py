#内部类接收外部内实例
class Outer:
    def __init__(self):
        self.__info = "www.baidu.com"   #定义一个私有属性
    def get_info(self): #访问私有属性
        return self.__info
    class __Inner:
        def __init__(self,out):
            self.__out = out
        def print_info(self):
            print(self.__out.get_info())
    def fun(self):
        inobj = Outer.__Inner(self)     #实例化内部类对象
        inobj.print_info()

def main():
    out = Outer()
    out.fun()

if __name__ == '__main__':
    main()
