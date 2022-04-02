# 练习：将美少女写入beau.xlsx的第5行第3列中并保存
import xlwt

# 创建工作簿
beau = xlwt.Workbook()

# 创建sheet
sheet1 = beau.add_sheet("sheet1")

# 创建表格并写入内容
workbox = sheet1.write(4,2,"美少女")

beau.save("beau.xlsx")