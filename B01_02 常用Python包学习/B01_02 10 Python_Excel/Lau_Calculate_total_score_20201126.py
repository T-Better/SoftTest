# 统计出每个人的总分，然后依次输出
import xlrd
import xlwt

print("--------------统计出每个人的总分，然后依次输出---------------")
# 拿取数据，写成字典，存入列表
# 打开工作簿
xlsx = xlrd.open_workbook("三年二班（各科成绩单）.xls")

# 选取sheet全班分数
sheet1 = xlsx.sheet_by_index(0)
all_data = []
num_set = set()
# 选取每行的学号、姓名、成绩
for row_i in range(1,sheet1.nrows):
    num = sheet1.cell_value(row_i,0)
    name = sheet1.cell_value(row_i,1)
    grade = sheet1.cell_value(row_i,3)

    # 将上面的键值对写成字典
    student = {
        "num":num,
        "name":name,
        "grade":grade
    }

    # 将生成的字典放到列表中
    all_data.append(student)
    num_set.add(num)
print(all_data)
print(num_set)

# 对上面的数据对每个人的分数进行计算,以学号作为标准,遍历方式
sum_list = []
for num in num_set:
    # num依次为1，2，3
    # 遍历all_data中的每个字典
    sum = 0  # 每次算一个人的总分前都要对sum清零再算，不能前后人叠加
    for student in all_data:
        if num == student["num"]:
            sum += student["grade"]
            name = student["name"]
    # 每算完一个人总分后将这些数据存字典
    sum_stu = {
        "num":num,
        "name":name,
        "grade_sum":sum
    }
    # 没存一次字典就将这个字典放入列表
    sum_list.append(sum_stu)
print(sum_list)
print("----------------结束--------------------")

print("----------------计算2班学生总分-----------------")

# 新建工作簿对象
new_workbook = xlwt.Workbook()
# 新建sheet
worksheet = new_workbook.add_sheet('2班')
# 新建单元格，并写入内容
# 写入第一列的内容
worksheet.write(0, 0, '学号')
worksheet.write(0, 1, '姓名')
worksheet.write(0, 2, '总分')
# 自动写入后面的内容
for row in range(0,len(sum_list)):
    worksheet.write(row+1,0,sum_list[row]['num'])
    worksheet.write(row+1,1,sum_list[row]['name'])
    worksheet.write(row+1,2,sum_list[row]['grade_sum'])
# 保存
new_workbook.save('2班学生总分.xls')

