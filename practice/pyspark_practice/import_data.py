from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("import_data_test")

sc = SparkContext(conf=conf)

# 通过parallelize方法将python对象加载到Spark里面，变成rdd对象
# rdd1 = sc.parallelize([1,2,3,4,5])
# rdd2 = sc.parallelize((1,2,3,4,5))
# rdd3 = sc.parallelize({1,2,3,4,5})
# rdd4 = sc.parallelize("abcdefg")
# rdd5 = sc.parallelize({"key1":"value1","key2":"value2"})

# 如果要查看rdd里面有什么内容，需要调用collect()方法
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())

#读取文件
# rdd = sc.textFile("F:\Repos\pydata-book\practice\pyspark_practice\hello.txt")
# print(rdd.collect())

sc.stop()