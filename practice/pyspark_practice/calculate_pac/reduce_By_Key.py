from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "F:\miniconda\envs\python38\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("reduce_by_key_test")
sc = SparkContext(conf=conf)

# reduceByKey算子：
# 接收数据必须是KV类型，也即二元元组，前一个值为key后一个为value
# 根据key的值进行分组，组内数据实现聚合
rdd = sc.parallelize([("男", 99), ("男", 77), ("男", 66), ("女", 99), ("女", 88)])

rdd2 = rdd.reduceByKey(lambda a, b: a + b)
# print(rdd2.collect()) [('男', 242), ('女', 187)]

rdd3 = sc.textFile("F:\Repos\pydata-book\practice\pyspark_practice\hello.txt")
word_rdd = rdd3.flatMap(lambda x: x.split(" "))
word_rdd = word_rdd.map(lambda x: (x, 1))
count_rdd = word_rdd.reduceByKey(lambda a, b: a + b)
print(count_rdd.collect())

sc.stop()