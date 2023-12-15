from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "F:\miniconda\envs\python38\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("filter_test")
sc = SparkContext(conf=conf)

# filter算子接受一个函数，如果返回值为true则保留数据，否则丢弃数据
rdd = sc.parallelize([1,2,3,4,5])
rdd2 = rdd.filter(lambda x:x>2)
print(rdd2.collect())

# distinct算子可以实现对rdd去重
rdd3 = sc.parallelize([1,1,1,2,2,3,4,5,5,6])
rdd3 = rdd3.distinct()
print(rdd3.collect())

sc.stop()
