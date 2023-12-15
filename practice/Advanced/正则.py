"""
演示python正则模块re
"""

import re
s = 'python hello world python'

# match 从头开始匹配
# 如果头部就没有匹配到返回none
result = re.match('python',s)
print(result) # <re.Match object; span=(0, 6), match='python'>
print(result.span()) # (0, 6)
print(result.group()) # python

# search 搜索匹配
# 从头开始找能匹配的字符串，找到第一个就停止，后面的都不管
# 如果没有找到就返回none
s1 = '1python hello world'
result = re.search('python',s1)
print(result) # <re.Match object; span=(1, 7), match='python'>

# findall 搜索全部匹配
# 没找到就返回一个空的list[]
result = re.findall('python',s)
print(result) # ['python', 'python']