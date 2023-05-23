import os

rpt= os.path.split(os.path.realpath(__file__))[0]

apt = os.path.dirname(os.path.abspath(__file__))

print(rpt)
print(apt)
