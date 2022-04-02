import openpyxl as opx
import random

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'

# 给sheet2写入数据
wb1 = opx.load_workbook(wp1)
ws2 = wb1['2月']
for r in ws2['A1:Z50']:
    for c in r:
        c.value = random.randint(1,100000)

note1 = opx.comments.Comment('重写','lzj') # 先定义一个批注变量
note2 = opx.comments.Comment('优秀','lzj') # 第一个是批注内容，第二个是批注者
ws2['A1'].comment = note1  # 然后把定义好的批注变量赋值给想要被批注的单元格
ws2['C1'].comment = note2

wb1.save(wp1)