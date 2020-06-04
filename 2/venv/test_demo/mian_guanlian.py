class member:
    def __init__(self,**kwargs):  #可以随意编写很多属性
        self.__name = kwargs.get("name")
        self.__age = kwargs.get("age")
        self.__childen = []     #表示一个人的全部后代，通过一个列表来描述
    def get_childen(self):      #获取全部后代信息
        return self.__childen
    def get_info(self):
        return "【member类】姓名： %s、年龄：%s " % (self.__name,self.__age)
    #setter、getter方法，略
    def set_car(self,car):      #设置人与车的关联
        self.__car = car
    def get_car(self):          #获取人对应车的信息
        return self.__car
class Car:
    def __init__(self,**kwargs):
        self.__brand = kwargs.get("brand")
        self.__price = kwargs.get("price")
    def set_member(self,member):
        self.__member = member
    def get_member(self):
        return self.__member
    def get_info(self):
        return "【car类】品牌： %s、价格： %s" %(self.__brand,self.__price)
def main():
    #第一步：各自实例化对象
    mem = member(name="陈官华", age=46)        #独立类对象
    chd_a = member(name="陈灿",age=22)
    chd_b = member(name="陈征宇",age=19)
    car = Car(brand="兰博基尼",price=1800000)
    car_a = Car(brand="奔驰G50",price=1500000)
    car_b = Car(brand="玛莎拉蒂",price=5600000)

    #第二步：根据对象引用关系设置关联
    mem.set_car(car)    #一个人设置对应的汽车关联
    car.set_member(mem) #一辆车对应的人的信息关联
    chd_a.set_car(car_a)
    chd_b.set_car(car_b)
    car_a.set_member(chd_a)
    car_b.set_member(chd_b)
    mem.get_childen().append(chd_a)
    mem.get_childen().append(chd_b)
    #第三步：根据关联关系获取相应的内容
    print(mem.get_info())   #获得父辈的基本信息
    print("\t|- %s" % mem.get_car().get_info())
    for child in mem.get_childen():
        print(child.get_info())
        print("\t|- %s" % child.get_car().get_info())





if __name__ == '__main__':
    main()