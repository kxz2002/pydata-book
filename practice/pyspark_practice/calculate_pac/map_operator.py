"""
map算子的演示
对一个数据集里面的每一个元素做同样的操作
"""
import os
from pyspark import SparkConf, SparkContext
os.environ['PYSPARK_PYTHON'] = "F:\miniconda\envs\python38\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("import_data_test")

def func(data):
    return data * 10

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])


rdd2 = rdd.map(func)  # f: (int) -> U@map提供一个函数，该函数需要有传入参数并提供一个返回值
# rdd2 = rdd.map(lambda x:x*10) 也可以使用lambda表达式
# print(rdd2.collect())

#链式调用
rdd3 = rdd.map(lambda x:x*10).map(lambda x:x+5)
# print(rdd3.collect())

# flatMap解除嵌套的map
rdd4 = sc.parallelize(["hello world","hello python","how are you"])
# rdd5 = rdd4.map(lambda x:x.split(" "))
# print(rdd5.collect()) [['hello', 'world'], ['hello', 'python'], ['how', 'are', 'you']]

rdd5 = rdd4.flatMap(lambda x:x.split(" "))
# print(rdd5.collect()) ['hello', 'world', 'hello', 'python', 'how', 'are', 'you']

sc.stop()