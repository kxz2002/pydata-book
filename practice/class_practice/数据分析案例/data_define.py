"""
定义数据存储的类
"""

class Record:
    def __init__(self,date,order_id,money,province) -> None:
        self.date = date            #订单日期
        self.order_id = order_id    #订单id
        self.money = money          #订单金额
        self.province = province    #订单省份
    def __str__(self) -> str:
        return f"date:{self.date},ID:{self.order_id},money:{self.money},province:{self.province}"