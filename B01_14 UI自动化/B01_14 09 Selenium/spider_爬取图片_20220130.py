# spider_爬取图片保存到Dpics下_20220130.py
import requests


url1 = r'https://pic.netbian.com/uploads/allimg/211102/112157-16358233172231.jpg'
r = requests.get(url1)

with open('D:/pics/16358233172231.jpg','wb') as f:
    f.write(r.content)


