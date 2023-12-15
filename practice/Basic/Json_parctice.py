#Json 与 Python字典的互相转换
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print(sys.version)

import json
data=[{"name":"Mike","age":"11"},{"name":"张三","age":"20"},{"name":"Amy","age":"20"}]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

s = '[{"name": "Mike", "age": "11"}, {"name": "张三", "age": "20"}, {"name": "Amy", "age": "20"}]'
json_data = json.loads(s)
print(type(json_data))
print(json_data)