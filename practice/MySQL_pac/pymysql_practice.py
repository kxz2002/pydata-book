from pymysql import Connection

conn = Connection(host="localhost", port=3306, user="root", password="kxz020623",autocommit=True)
print(conn.get_server_info()) #打印连接信息

# 获取游标对象
cursor = conn.cursor()
# 先选择数据库
# conn.select_db("test")
# 执行sql
# cursor.execute("create table test_pymysql(id int);")

#查询操作
conn.select_db("world")
cursor.execute("select * from student;")
results:tuple = cursor.fetchall()
for r in results:
    print(r)

cursor.execute("insert into student values(10,'Alice',22,'女')")
#conn.commit() 更改数据后需要提交才能生效，不过也可以配置autocommit选项来自动提交

#关闭连接
conn.close()