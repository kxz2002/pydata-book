from data_define import Record
from file_define import FileReader, TextFileReader, JSONFileReader
from typing import List
from pymysql import Connection

textFilerReader = TextFileReader(
    "F:\Repos\pydata-book\practice\class_practice\数据分析案例\data_text.txt"
)
jsonFileReader = JSONFileReader(
    "F:\Repos\pydata-book\practice\class_practice\数据分析案例\data_json.txt"
)

jan_data: List[Record] = textFilerReader.read_data()
feb_data: List[Record] = jsonFileReader.read_data()

all_data: List[Record] = jan_data + feb_data

conn = Connection(
    host="localhost", port=3306, user="root", password="kxz020623", autocommit=True
)

cursor = conn.cursor()

conn.select_db("py_sql")

# for record in all_data:
#     sql = f"insert into orders values('{record.date}','{record.order_id}',{record.money},'{record.province}')"
#     cursor.execute(sql)

f = open("F:\Repos\pydata-book\practice\MySQL_pac\data.txt","w",encoding="utf-8")
select_sql = "select * from orders"
cursor.execute(select_sql)
results:tuple = cursor.fetchall()
# print(results)
for record in results:
    content = f"{str(record[0])},{record[1]},{str(record[2])},{record[3]}\n"
    f.write(content)
conn.close()
f.close()