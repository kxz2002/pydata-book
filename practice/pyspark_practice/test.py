from pyspark import SparkConf, SparkContext

#创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)
# 打印pySpark版本
print(sc.version)
# 停止SparkContext对象的运作（停止PySpark程序）
sc.stop()