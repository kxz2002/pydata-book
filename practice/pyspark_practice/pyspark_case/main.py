from data_define import Record
from file_define import FileReader, TextFileReader, JSONFileReader
from typing import List

import os
from pyspark import SparkConf,SparkContext
os.environ["PYSPARK_PYTHON"] = "F:\miniconda\envs\python38\python.exe"
os.environ["HADOOP_HOME"] = "F:\Hadoop\hadoop-3.0.0"
conf = SparkConf().setMaster("local[*]").setAppName("reduce_by_key_test")
conf.set("spark.default.parallelism", "1")  # 设置分区文件为1
sc = SparkContext(conf=conf)

rdd_origin = sc.textFile("F:\Repos\pydata-book\practice\pyspark_practice\pyspark_case\search_log.txt")
# 打印输出，热门搜索时间段小时精度，top3
rdd_h = rdd_origin.map(lambda x:(x[:2],1)).reduceByKey(lambda a,b:a+b).sortBy(lambda x:x[1],numPartitions=1,ascending=False)
# print(rdd_h.collect())

# 打印输出，热门搜索关键词top3
rdd_split = rdd_origin.map(lambda x:x.split("\t"))
print(rdd_split.collect())
# rdd_word = rdd_origin.map(lambda x:x)
# 打印输出，统计netflix在那个时间段被搜索最多

sc.stop()