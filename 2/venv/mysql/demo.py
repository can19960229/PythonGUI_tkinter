#coding=utf-8
import pymysql
import traceback

tmp = "DELETE FROM user WHERE (uid,name) = (%s,%s);"   #SQL模板字符串
l_tupple = [(i,m) for i in range(49,99) for m in range(24,74)]
class mymysql(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="mysqladmin",
            database="mypythondemo",
            charset="UTF8")

    def insert_sql(self,temp,data):
        cur = self.conn.cursor()
        try:
            cur.executemany(temp,data)
            self.conn.commit()
            print("更新的数据影响行数：%s" % cur.rowcount)
            print("最后一次增长ID：%s" % cur.lastrowid)
        except:
            self.conn.rollback()
            traceback.print_exc()
        finally:
            cur.close()

if __name__ == '__main__':
    m = mymysql()
    m.insert_sql(tmp,l_tupple)