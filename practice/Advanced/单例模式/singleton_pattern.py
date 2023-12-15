"""
单例模式
保证一个类只有一个实例，并提供一个访问它的全局访问点
"""
from str_tools import str_tools
s1 = str_tools
s2 = str_tools
print(s1)
print(s2)