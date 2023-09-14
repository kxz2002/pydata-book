my_str = "hello world"
value1 = my_str[1]
value2 = my_str[-1]
# my_str[0]="H" 字符串不支持修改

#寻找第一个出现的元素的下标值
index = my_str.index("world")
# print(index)  6

#replace
new_str = my_str.replace("l","L")
# print(new_str) heLLo worLd

#split
my_str = "hello world python"
my_str_list = my_str.split(" ")
# print(my_str_list) ['hello', 'world', 'python']

#strip方法
my_str="  hello world python  "
#不传参数，默认去除字符串前后空格
# print(my_str.strip()) hello world python

my_str="12hello world python21"
#传入参数，去除前后的指定字符，参数按照单个字符来删除
# print(my_str.strip("12"))  hello world python
