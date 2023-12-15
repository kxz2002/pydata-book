"""
和文件相关的类定义
"""

from data_define import Record
from typing import List
import json
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class FileReader:
    def read_data(self) -> List[Record]:
        """读取文件内的数据，将每一条数据封装成一条record，封装到list内返回"""
        pass

class TextFileReader(FileReader):
    def __init__(self,path) -> None:
        self.path = path
    
    def read_data(self) -> List[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list : List[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)
        f.close()
        return record_list

class JSONFileReader(FileReader):
    def __init__(self,path) -> None:
        self.path = path

    def read_data(self) -> List[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list : List[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["日期"],data_dict["订单id"],int(data_dict["订单金额"]),data_dict["订单省份"])
            record_list.append(record)
        f.close()
        return record_list



if __name__ == "__main__":
    # textReader = TextFileReader("F:\Repos\pydata-book\practice\class_practice\数据分析案例\data_text.txt")
    # textReader.read_data()
    jsonReader = JSONFileReader("F:\Repos\pydata-book\practice\class_practice\数据分析案例\data_json.txt")
    list1 = jsonReader.read_data()
    for line in list1:
        print(line)