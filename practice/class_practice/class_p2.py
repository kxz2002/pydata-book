class Phone:
    IMEI = None
    producer = "HM"

    def call_by4G(self):
        print("call by 4G")

class NFCReader:
    nfcType = "5th"
    producer = "hm"
    def read_card(self):
        print("read card")
    def write_card(self):
        print("write card")

#继承以及多继承
class Phone2022(NFCReader,Phone):
    face_id = "1001"
    producer = "ITCAST" #复写，方法的复写也是一样的，只要重写方法体就可以了

    __currrent_voltage = 0.5 #不论是成员属性还是成员方法，在名称前添加两个下划线，就可以被声明为私有

    def __keep_single_core(self):
        print("keep single core")
    
    def call_by4G(self):
        print("子类的4G通话:")
        #调用父类方法
        # 1.使用父类名
        # print(f"producer: {Phone.producer}")
        # Phone.call_by4G(self)#不需要传self进去了
        # 2.使用super()
        print(f"producer: {super().producer}")
        super().call_by4G()#不需要传self进去了

    def call_5G(self):
        if self.__currrent_voltage>=1:
            print("5G is on")
        else:
            self.__keep_single_core()


phone2022 = Phone2022()
# phone2022.call_5G()
# phone2022.call_by4G()
print(phone2022.producer)
phone2022.read_card()
phone2022.call_by4G()