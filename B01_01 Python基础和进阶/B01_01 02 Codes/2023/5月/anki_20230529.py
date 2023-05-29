import os


p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 12 OS库\Codes\2022'

for i in os.scandir(p):
    if i.name.startswith('anki_os_20220402') and i.name.endswith('.py'):
        print(i.name,i.path,i.is_dir())












