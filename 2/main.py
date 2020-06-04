from com.yootk.info.message import *  # 导入第三方模块


class Member:
    """
    在程序中要想使用类，一般通过对象进行调用
    python中对象的实例
    对象(变量) = 名称([参数，...])

    实例化对象.属性：访问类中的属性
    实例化对象.方法():调用类中的方法

     类中属性的定义，self描述的是类自身的对象，必须要定义
      name age 是两个必须要传递的参数

    """
    info = "类属性"

    def set_info(self, name, age):
        self.name = name  # 为本对象进行属性封装
        self.age = age
        """
        进行类对象信息的返回
        """

    def get_info(self):
        return "姓名： %s ,年龄： %d" % (self.name, self.age)


def main():
    mem = Member()  # 实例化对象
    print(Member.info)
    mem.set_info("陈灿", 22)  # 通过实例化调用类中的方法
    print(mem.get_info())
    # print("我的名字： %s ,我的年龄：%s" % (mem.name, mem.age))  # 可通过实例化直接获得对象的属性
    # print(type(mem.get_info))  # 方法（面向对象的定义)


if __name__ == '__main__':
    main()  # 【设置断点】
