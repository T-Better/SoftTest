import openpyxl as opx
import re

# 创建工作簿
wp1=""
wb1 = opx.load_workbook(wp1)
wss = wb1.worksheets
ws1 = wb1['1月']

ws1.append(['a',b])
