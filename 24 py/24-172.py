import re
with open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 24\\24-171.txt') as t:
  t = [x.strip().replace('XYZ', '*') for x in t]

maximum = 0
for x in t:
  posl = re.findall(r'[^*]{0,1}[*]{1,}[^*]{0,1}', x)
  for word in posl:
    lenght = 0
    if word[0] in 'XYZ':
      lenght +=1
    if word[-1] in 'XYZ':
      lenght +=1
    lenght += word.count('*')*3
    if lenght > maximum:
      maximum = lenght
print(maximum)
