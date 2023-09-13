from itertools import permutations
def lox(s):
    l = ''.join(s)
    if l[0]=='0': return False
    if l[-1] not in ['0','5']: return False
    for c in ['02', '20', '04', '40', '06', '60', '08', '80', '00',
               '24', '42', '26', '62', '28', '82', '22',
               '46', '64', '48', '84', '44',
               '68', '86', '66', '88',
               '13', '31', '15', '51', '17', '71', '19', '91', '11',
               '35', '53', '37', '73', '39', '93', '33',
               '57', '75', '59', '95', '55',
               '79', '97', '77', '99']:
        if c in l:
            return False
    return True
c=0
for x in permutations('0123456789',5):
    if lox(x):
        c+=1
print(c)