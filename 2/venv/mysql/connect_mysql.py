import pymysql
#链接数据库，必须设置数据库e连接的主机名称、端口号、用户名、密码、数据库名称
# host="localhost",port=3306,user="root",password="mysqladmin",database="mypythondemo"
import traceback
#传统的pymysql组件支持的是原生的SQL
SQL_01 = "INSERT INTO user(name,age,birthday,salary,note) " \
      "VALUES ('陈征宇', 19,'2010-09-09',8000.0,'www.baidu.com')"

SQL = "SELECT uid, name, age, birthday, salary, note FROM user " \
      "WHERE name LIKE %s LIMIT %s, %s" 			# 数据分页查询

SQL_03 = "DELETE FROM user WHERE (name,age,birthday,salary) = (%s,%s,%s,%s)" 		# SQL模版

'''
SQL_02 = """
    USE mypythondemo ;
    DROP TABLE IF EXISTS company ;
    CREATE TABLE company(
        cid	BIGINT	AUTO_INCREMENT	COMMENT '公司ID',
        name   	VARCHAR(30) 		COMMENT '公司名称' ,
        loc 	VARCHAR(100) 		COMMENT '公司位置' ,
        note	TEXT			COMMENT '公司介绍' ,
        CONSTRAINT pk_uid PRIMARY KEY(cid)
    ) engine=INNODB ;
    INSERT INTO company(name, loc, note) VALUES 
	 ('沐言优拓（沐言童趣旗下品牌）', '北京', 'www.yootk.com') ;
"""
'''

tmp = "insert into user(name,age,birthday,salary) values(%s,%s,%s,%s);"   #SQL模板字符串
l_tupple = [('陈征宇', 19,'2010-09-09',8000.0),('陈征宇', 20,'2010-09-09',8000.0)]   #生成数据参数，list里嵌套tuple

def main():
    keyword = "%陈灿%"  # 查询关键字
    current_page = 4  # 当前页
    line_size = 5

    try:
        CONN = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="mysqladmin",
            database="mypythondemo",
            charset="UTF8")
        print("连接诶成功，当前版本：%s" % CONN.get_server_info())
        print("事务提交模式：%s" % CONN.get_autocommit())
        cmd = CONN.cursor() #获得数据库的操作指向
'''
#有错误的代码！！！！！！！
#批处理executemany
        data_list = []  # 保存数据列表
       # for num in range(1001):  # 增加1000条数据
        data_list.remove(('陈征宇', 19,'2010-09-09',8000.0,"www.baidu.com"))  # 添加批处理数据
          #  if num % 20 == 0:  # 每20条执行批处理
        cmd.executemany(SQL, data_list)  # 执行数据增加操作
        data_list.clear()
'''
#数据更新操作
#        cmd.execute(SQL_01)    #执行SQL_01语句
#        cmd.execute(SQL_02)
        cmd.executemany(tmp,l_tupple)



#分页模糊查询
        cmd.execute(query=SQL, args=[keyword,
                                     (current_page - 1) * line_size, line_size])  # 执行SQL操作
        for user_row in cmd.fetchall():  # 迭代每一行数据
            uid = user_row[0]  # 获取第1列数据
            name = user_row[1]  # 获取第2列数据
            age = user_row[2]  # 获取第3列数据
            birthday = user_row[3]  # 获取第4列数据
            salary = user_row[4]  # 获取第5列数据
            note = user_row[5]  # 获取第6列数据
            print("用户ID：%s、姓名：%s、年龄：%s、生日：%s、月薪：%s、备注：%s" %
                  (uid, name, age, birthday, salary, note))  # 输出查询结果

        CONN.commit()  # 提交事务，如果事务不提交，更新不生效
        print("更新的数据影响行数：%s" % cmd.rowcount)
        print("最后一次增长ID：%s" % cmd.lastrowid)

    except:
        print("处理异常：" +traceback.format_exc())
    finally:
        CONN.close()

if __name__ == '__main__':
    main()