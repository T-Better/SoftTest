import re


title = '<!--s-text--->双十一点燃线下经济  "小时达" 服务成<em>阿里巴巴</em>增长新引擎<!--/s-text-->'
r = re.sub('<(.*?)>','',title)
print(r)











