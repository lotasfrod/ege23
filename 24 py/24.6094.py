el = open('C:\\Users\\БАТЯ\\Downloads\\24_6094.txt').readline()
el = el.split('XYZY')
m = 0
for i in el:
    i = i.replace('XY', '*').replace('ZY','*').replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
    i = i.split()
    for j in i:
        m = max(m, len(j))
print(m+1)
    