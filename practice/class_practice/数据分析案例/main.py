from file_define import FileReader,TextFileReader,JSONFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
from typing import List

textFilerReader = TextFileReader("F:\Repos\pydata-book\practice\class_practice\数据分析案例\data_text.txt")
jsonFileReader = JSONFileReader("F:\Repos\pydata-book\practice\class_practice\数据分析案例\data_json.txt")

jan_data:List[Record] = textFilerReader.read_data()
feb_data:List[Record] = jsonFileReader.read_data()

all_data:List[Record] = jan_data + feb_data
# print(all_data)

data_dict = {}

for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date]+=record.money
    else:
        data_dict[record.date] = record.money

#可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("每日销售额柱状图.html")