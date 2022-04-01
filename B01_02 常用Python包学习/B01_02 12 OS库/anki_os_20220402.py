import os

# windows如何检测a路径下的b文件是否存在，存在和不存在分别返回什么？
res = os.path.exists(r'D:\Git_Reps\SoftTest\Soft_test\SoftTest')
print(res)

# python移动文件和文件夹指令有哪些？怎么用？
import shutil
shutil.move('旧目录','新目录')



