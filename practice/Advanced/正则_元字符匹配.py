import re

s='itheima1 @@python2 !!666 ##itcast3'

#找出全部的数字
# result = re.findall(r'\d',s) # 字符串前面带上r的标记，说明字符串中转义字符无效，就是普通字符的意思
# print(result) # ['1', '2', '6', '6', '6', '3']

# 找出全部的特殊字符
# result = re.findall(r'\W',s)
# print(result) # [' ', '@', '@', ' ', '!', '!', ' ', '#', '#']

# []可以表示匹配[]里面列举的字符
# result = re.findall(r'[a-zA-Z]',s) # 这个范围是可以自行修改的，如[a-cA-D1-6]
# print(result) # ['i', 't', 'h', 'e', 'i', 'm', 'a', 'p', 'y', 't', 'h', 'o', 'n', 'i', 't', 'c', 'a', 's', 't']

# 案例
# 匹配账号，只能由数字或字母组成，长度限制6-10位
r = '^[a-zA-Z0-9]{6,10}$'
s1 = '1234567890'
print(re.findall(r,s1)) # ['1234567890']

# 匹配QQ号，长度5-11，纯数字，第一位不为零
r = '^[1-9][0-9]{4,10}$'
print(re.findall(r,s1))

# 匹配邮箱地址，只允许QQ，163，gmail这三种格式
# {内容}.{内容}@{内容}.{内容}.{内容}
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s2 = 'a.b.c.d@qq.e.f.g'
print(re.findall(r,s2)) # [('a.b.c.d@qq.e.f.g', '.d', 'qq', '.g')]