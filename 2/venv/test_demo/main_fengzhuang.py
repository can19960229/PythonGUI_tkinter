from com.yootk.info.message import *  # 导入第三方模块


class Member:

    """
    类对属性进行封装,使用setter和getter函数进行属性的访问
    一般不会使用“对象.属性”进行访问
    属性封装后不能进行外部访问，但是可以进行内部的访问
    
     """
    def set_name(self, name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
def main():
    mem = Member()  # 实例化对象
    mem.set_name("陈灿")
    mem.set_age(22)
    print(mem.get_name(),mem.get_age())

if __name__ == '__main__':
    main()  # 【设置断点】
