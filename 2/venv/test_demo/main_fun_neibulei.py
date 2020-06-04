#内部类接收外部内实例
class Outer:
    def __init__(self):
        self.__info = "www.baidu.com"   #定义一个私有属性
    def print_info(self,title):
        print("%s: %s " % (title,self.__info))
    def fun(self,msg):
        out_obj = self
        subtitle = "百度"
        class Inner:
            def send(self):
                out_obj.print_info(msg + subtitle)
        Inner().send()

def main():
    out = Outer()
    out.fun("网址")

if __name__ == '__main__':
    main()
