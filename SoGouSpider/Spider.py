import re

doc = ''
a = re.findall('<em.*?>(.*?)</em>', doc)
print(type(a[0]))
print(a)
