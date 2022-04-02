import openpyxl as opx
import re

# 创建工作簿
wp1=""
wb1 = opx.Workbook(wp1)
for i in range(1,101):
    ws1 = wb1.create_sheet("i")
# re.search()怎么用，匹配到和未匹配到返回什么？如何获取匹配到的值？
str1 = "12345"
res1 = re.search("^\d+$",str1)
print(res1.group())

# wb1.save(wp1)