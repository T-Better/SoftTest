import xlrd
import xlwt


"""
要求：统计出下表中每人总成绩，然后输出到一个名为"143班2012年夏季期末成绩分数汇总"的表格中
"""

# 一、拿取数据，存在字典中

# 1. 打开工作簿
xlxs1 = xlrd.open_workbook("143期末成绩.xls")

# 2. 选取sheet页
sheet1 = xlxs1.sheet_by_index(0)

# 3. *难点* 拿取每个单元格中的内容，一个人一个字典
all_data = []
num_set = set()  # 提前定义一个集合用于去重
for row_i in range(1,sheet1.nrows):  # 先不要想全读取，先细化，读一个人的，读一行
    num = sheet1.cell_value(row_i,0)
    name = sheet1.cell_value(row_i,1)
    grade = sheet1.cell_value(row_i,3)

    student = {
        "学号":num,
        "姓名":name,
        "成绩":grade
    }
    all_data.append(student)
    num_set.add(num)
print(all_data)
print(num_set)

# 问题：上面生成的数据有重复的，接下来汇总并去重
"""
二、*难点* 将拿到的进行汇总 方法：通过学号来对比做初步遍历，此时需要一个比对，一个是表
中数据，一个是去重后的学号num_set集合然后对同一个学号中的多个内容求和放到一个新的字典中
"""
sum_data = []
for num in num_set:  # 因为需要对两个列表中的对象都做比较，所以都要遍历
    grade_sum = 0
    for student in all_data:
        if num == student["学号"]:
            grade_sum = grade_sum + student["成绩"]
            name = student["姓名"]  # 虽然重复赋值，但也省去了下面拿取该值的麻烦
            # num = student["学号"]

    # 将生成的数据存入字典
    student_data = {
        "学号":num,
        "姓名":name,
        "总成绩":grade_sum
    }
    sum_data.append(student_data)

print(sum_data)

# 三、将汇总的数据写入excel表中并保存
# 1. 创建工作簿
new_xlxs = xlwt.Workbook()

# 2. 创建sheet页
sheet2 = new_xlxs.add_sheet("sheet1")

# 3. 写入数据
# 3.1 先写好格式
sheet2.write(0,0,"学号")
sheet2.write(0,1,"姓名")
sheet2.write(0,2,"总分数")

# 3.2 将上面得到的sum_data按照位置填充进去,按列写入 *难点*
for row in range(0,len(sum_data)):
    sheet2.write(row+1,0,sum_data[row]["学号"])  # 管第一列导入
    sheet2.write(row+1,1,sum_data[row]["姓名"])
    sheet2.write(row+1,2,sum_data[row]["总成绩"])

# 4. 保存
new_xlxs.save("143班2012年夏季期末成绩分数汇总.xls")