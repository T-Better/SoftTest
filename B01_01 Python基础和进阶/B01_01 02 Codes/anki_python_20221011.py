# 斐波那契数列
"""
def feb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return feb(n-1) + feb(n-2)

print(feb(5))
"""

# 读取yaml
"""
import yaml

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_01 Python基础和进阶\B01_01 02 Codes'
y1 = r'\data_20220207.yaml'
yp1 = p1+y1
with open(yp1,'r') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    print(data)
"""


# 转换成三行
"""
a=3
b=5
c = a if a>b else b
print(c)
"""




