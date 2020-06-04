
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm #orm的所有工具
import sqlalchemy.orm.session  #数据库操作的核心
import datetime

#当前给定的地址中还有一个 MySQL-Connector操作组件, 需要单独安装
#定义MySQL数据库方言（直接在连接上通过字符串的形式定义）以及连接地址
# 连接时必须明确的设置数据库方言（mysql）、底层数据库操作组件（mysql-connector）和数据库连接信息
MySQL_URL = "mysql+mysqlconnector://root:mysqladmin@localhost:3306/mypythondemo"

class User(sqlalchemy.ext.declarative.declarative_base()):   # 定义数据表映射类  sqlalchemy.ext.declarative.api.Base

    #数据表名称,说明该操作是针对数据表‘user’的,并一般该类名称的定义为表的名称首字母大写,如：class User
    __tablename__= "user"
    #定义字段和类属性的关系
    uid = sqlalchemy.Column(sqlalchemy.BIGINT,primary_key = True)  #描述对应的数据列  映射user.uid字段
    name = sqlalchemy.Column(sqlalchemy.String)  # 映射user.name字段
    age = sqlalchemy.Column(sqlalchemy.Integer)  # 映射user.age 字段
    birthday = sqlalchemy.Column(sqlalchemy.Date)  # 映射user.birthday字段
    salary = sqlalchemy.Column(sqlalchemy.Float)  # 映射user.salary字段
    note = sqlalchemy.Column(sqlalchemy.String)  # 映射user.note字段
    def __repr__(self) -> str:  # 对象输出
        return "用户编号：%s、姓名：%s、年龄：%s、生日：%s、月薪：%s、备注：%s" % \
               (self.uid, self.name, self.age, self.birthday, self.salary, self.note)

def main():
    engine = sqlalchemy.create_engine(MySQL_URL, encoding ="UTF-8", echo = True) # echo = True 打开日志，返回所有操作信息
    sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)  # 获得Session类
    session = sqlalchemy.orm.session.Session()  #实例化Session对象
    #查询数据
    result = session.query(User).filter(User.name.like("%陈灿%")).offset(8).limit(5).all()
  #  result = session.query(User).filter(User.name.like("%陈灿%")).slice(5, 20).all()
   # result = session.query(User).filter(User.name.like("%陈灿%"))[0:2]  # 数据查询


    print(result)
    # 操作完成，关闭连接
    session.close()  #关闭session （释放连接）

if __name__ == '__main__':
    main()