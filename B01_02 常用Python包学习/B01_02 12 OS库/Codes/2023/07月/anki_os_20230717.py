import os


p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 12 OS库\Codes\2022'


for f in os.scandir(p):
    if f.name.startswith('anki_os_20220402') and f.name.endswith('.py'):
        print(f.name, f.path,f.is_dir())











