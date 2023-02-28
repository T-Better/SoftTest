import requests


url = r'https://pic.netbian.com/uploads/allimg/211102/112157-16358233172231.jpg'
r = requests.get(url)
with open('a.jpg',mode='wb+') as f:
    f.write(r.content)








