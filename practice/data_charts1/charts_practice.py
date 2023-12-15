import numpy as np
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
import os
print(np.array([1,2,3]))
print(os.system('which python'))
line = Line()# get line object
line.add_xaxis(["China","US","UK"])
line.add_yaxis("GDP",[10,20,30])
line.set_global_opts(
    title_opts=TitleOpts(title="GDP 展示",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
line.render()
