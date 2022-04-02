# Change_names_v20211024.py

import os

doc_path = input(r"请输入文件夹路径（例如C:\abc）:")  # 所要修改文件所在路径，注意斜杠
doc_name = input('请输入要添加或删除的名字：')  # 所要修改的文件名，包含后缀
reconfirm = int(input('添加请按1，删除请按2：'))  # 1:新增文件；2：删除文件名

# 返回指定文件夹下的文件和文件夹的名字，返回是一个列表
path_list = os.listdir(doc_path)  # 自动读取doc_path下的所有文件并返回其列表

# 遍历目录列表中的每一个数据
for doc in path_list:
    if reconfirm == 1:  # 如果是新增执行如下指令
        new_name = doc_name + doc  # 新文件名字=我们要添加的名字+原文档名
        print(new_name)
    elif reconfirm == 2:  # 如果是删除文档
        pre_long = len(doc_path)  # 计算
        new_name = doc[pre_long:]
        print(new_name)
    else:
        print('输入错误')
        break

    os.chdir(doc_path)  # 改变当前工作目录到指定路径
    os.rename(doc, new_name)  # 重命名