from pyspark import SparkConf, SparkContext
import os
from typing import List

os.environ["PYSPARK_PYTHON"] = "F:\miniconda\envs\python38\python.exe"
os.environ["HADOOP_HOME"] = "F:\Hadoop\hadoop-3.0.0"
conf = SparkConf().setMaster("local[*]").setAppName("reduce_by_key_test")
conf.set("spark.default.parallelism", "1")  # 设置分区文件为1
sc = SparkContext(conf=conf)

# rdd = sc.parallelize([1,2,3,4,5])

# collect函数的返回值为list
# rdd_list:List = rdd.collect()
# print(rdd_list)

# reduce对rdd内部两两聚合
# num = rdd.reduce(lambda a,b:a+b)
# print(num) 15

# take算子，取出rdd前n个元素组合成一个list返回
# take_list = rdd.take(3)
# print(take_list) [1, 2, 3]

# count 统计rdd内有多少个元素
# count_num = rdd.count()
# print(count_num) 5

# 将数据输出到文件里,并设置输出文件分区为1
# 设置输出文件分区为1有两种方法，这里和上面的conf设置都可以实现
rdd2 = sc.parallelize([("hello", 3), ("world", 5), ("python", 7)], numSlices=1)
rdd3 = sc.parallelize([(1, 3, 5), (2, 4, 6), (7, 8, 9)], 1)

# 输出的结果是一个文件夹，不是一个文件
rdd2.saveAsTextFile("D:\output1")
rdd3.saveAsTextFile("D:\output2")

sc.stop()
