import os


p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 12 OS库\Codes\2022'

for t in os.scandir(p):
    if t.name.startswith('anki_os_20220402') and t.name.endswith('.py'):
        print(t.name,t.path,t.is_dir())









