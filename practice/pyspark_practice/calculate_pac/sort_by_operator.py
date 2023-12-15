from pyspark import SparkConf, SparkContext
import os
import json
os.environ["PYSPARK_PYTHON"] = "F:\miniconda\envs\python38\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("filter_test")
sc = SparkContext(conf=conf)

rdd0 = sc.parallelize([("hello", 10), ("world", 2), ("python", 3), ("LRL", 6)])
# 接受一个函数，函数的返回值用于决定排序的依据
# 这里使用了元组的第二位作为排序的依据
# numPartitions表示分区，这里1表示全局排序
rdd_final = rdd0.sortBy(lambda x: x[1], ascending=True, numPartitions=1)
# print(rdd_final.collect()) [('world', 2), ('python', 3), ('LRL', 6), ('hello', 10)]

# 一个综合案例
rdd = sc.textFile(
    "F:\Repos\pydata-book\practice\pyspark_practice\calculate_pac\data.txt"
)
rdd = rdd.flatMap(lambda x: x.strip().split("|"))

# 各个城市的销售额排名
rdd = rdd.map(lambda x:json.loads(x))
rdd_money = rdd.map(lambda x: (x["areaName"], x["money"]))

rdd_money = rdd_money.reduceByKey(lambda a, b: a + b)
rdd_money_final = rdd_money.sortBy(lambda x:int(x[1]),ascending=True,numPartitions=1)
# print(rdd_money_final.collect())

# 全部城市，有哪些商品类别在售卖
rdd_category = rdd.map(lambda x:x["category"]).distinct()
# print(rdd_category.collect())

# 北京市有哪些商品在售卖
rdd_area = rdd.map(lambda x:(x["areaName"],x["category"]))
rdd_BJ = rdd_area.filter(lambda x:x[0] == "Beijing")
rdd_BJ_category = rdd_BJ.map(lambda x:x[1]).distinct()
print(rdd_BJ_category.collect())

sc.stop()
