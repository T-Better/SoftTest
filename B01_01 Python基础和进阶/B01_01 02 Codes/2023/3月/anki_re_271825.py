import re
a = 'abcFBIabcCIAabc'
r = re.findall('fbia',a,re.I)
print(r) # 预期 FBIa




