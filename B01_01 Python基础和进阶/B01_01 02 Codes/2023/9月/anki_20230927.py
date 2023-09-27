# 定义一个全局变量 name = "张三", 定义一个函数 my_test1, 在函数 my_test1 内部修改全局变量 name 的值为”李四”
name = "张三"
def my_test1():
    global name
    name = "李四"

# 全局变量num的值被my_test1函数改变了
my_test1()
print(name)