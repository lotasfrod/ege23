x = ((64**25+4**10)-(16**20+32**3))
c = ''
while x>0:
    c+=str(x%4)
    x//=4
print(c)
#c = '000000023300000000000000000000000000000033333333333333333333333333333333333'
#print(len(c))