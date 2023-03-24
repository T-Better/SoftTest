# Practice1_v20211026.py
"""
需求：在指定的文件夹下面
（1）找到有多少个文件，有多少个文件夹，分别都是什么
（2）找到包含哪些文字的文件，分别都是什么
（3）找到指定后缀名的文件（例如excel文件），分别都是什么
（4）忽略大小写问题
"""
import os,re

# 第一步：将所有文件夹和文件便利出来，将其名字分开存放在files和dirs两个列表中
ipath = r'D:\BaiduNetdiskWorkspace\\Work\C-人行-浪潮\C00-浪潮 人行事务\C03_文档'
os.chdir(ipath)  # 改变当前工作目录到指定的路径
files = []  # 文件
dirs = []  # 文件夹
for e in os.scandir():  # os.scandir()：遍历当前路径下的所有文件和文件夹，返回所有文件、文件夹的名字、路径、是否是路径判断等
    if e.is_dir():
        dirs.append(e.name)  # 将该文件追加到dirs列表中
    else:  # 如果是文件，将改文件的名字追加到files列表中
        files.append(e.name)
print(f'(1)文件夹共{len(dirs)}个，分别是{dirs}')
print(f'(2)文件共{len(files)}个,分别是{files}')
print("-"*10)

# 第二步：将所有包含“附件”的文件找出来并计数
tmplist1 = []  # 存放所有包含附件字段的文件名
for f in files:
    if "附件" in f:
        tmplist1.append(f)
print(f'(3)附件共{len(tmplist1)}个，分别是{tmplist1}')
print("="*10)

# 第三步：在第二步基础上找出附件中有多少excle文档
tmplist2 = []  # 存放是excel的
for fn in tmplist1:  # 遍历所有附件
    dot_p = fn.rfind('.')  # 找见附件后缀前面点的位置，用于下面将后缀名取出判断类型
    if fn[dot_p+1:] in ['xlsx','xls']:  # 判断是不是excel(新旧都有) ;
        # 也可以用if fn.endswith('.xlsx')来实现
        tmplist2.append(fn)  # 将excel添加到列表tmplist2中
print(f'(4)Excel文件共{len(tmplist2)}个,分别是{tmplist2}')
print("+"*10)

# 找出包含log的文件名
tmplist3 = []  # 存放包含log的文件名
for fn3 in files:  # 再次遍历非目录
    retmp = r'.+log.+'  # 找出其中包含log的文件 ！设计一个能匹配到包含log文件的正则表达式难倒了
    res = re.match(retmp, fn3,re.I)  # re.I:忽略大小写;不知道为啥没有匹配到...
try:
    tmplist3.append(res.group())  # group()分组返回整个字符串
except Exception as result:
    print(result)
print(f'包含log的文件有{len(tmplist3)}个，分别是{tmplist3}')