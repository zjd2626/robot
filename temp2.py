#coding=utf-8
import re
str2='     Hello     world,   I love China!      '
words=reversed(re.split(r'(\s+)',str2))
print(list(words))
revwords=''.join(reversed(re.split(r'(\s+)',str2)))
print(revwords)
