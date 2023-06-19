# 读取excel中的测试cases
import openpyxl as opx
from config import *


wb1 = opx.load_workbook(excelpath)
ws_caladd = wb1['caladd']
ws_calsub = wb1['calsubtract']
ws_calmul = wb1['calmultiply']
ws_caldev = wb1['caldevide']

class GetData():
    """获取各excel表中字段内容"""
    def get_data(self,ws_i):
        """获取数据公用方法"""
        data_list = []
        for n in ws_i.iter_rows(min_row=2):
            tmp_list = []
            for c in n:
                tmp_list.append(c.value)
            data_list.append(tmp_list)
        print(data_list)
        return data_list

    def get_adddata(self):
        """获取加法数据，返回列表对象"""
        return self.get_data(ws_caladd)

    def get_subdata(self):
        """获取减法数据，返回列表对象"""
        return self.get_data(ws_calsub)

    def get_muldata(self):
        """获取乘法数据，返回列表对象"""
        return self.get_data(ws_calmul)

    def get_devdata(self):
        """获取除法数据，返回列表对象"""
        return self.get_data(ws_caldev)

# if __name__ == "__main__":
#     gd = GetData()
#     gd.get_adddata()
#     gd.get_subdata()
#     gd.get_muldata()
#     gd.get_devdata()



