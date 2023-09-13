print('19')
def game(a,step):
    if a>=73:
        return step == 2
    if step >2 :
        return 0
    if step%2==0:
        return all([game(a+1,step+1), game(a+3,step+1), game(a*2,step+1)])
    return any([game(a+1,step+1), game(a+3,step+1), game(a*2,step+1)])

for a in range(1,73):
    print(a, game(a,0))

print('\n')
print('20')
def can_win(a):
    return (a+1>=73) or (a+3>=73) or (a*2>=73)

def game(a,step):
    if step == 0 and can_win==0:
        return 0
    if a>=73:
        return step == 3
    if step >3 :
        return 0
    if step%2==0:
        return any([game(a+1,step+1), game(a+3,step+1), game(a*2,step+1)])
    return all([game(a+1,step+1), game(a+3,step+1), game(a*2,step+1)])
for a in range(1,73):
    print(a, game(a,0))

print('\n')
print('21')
def can_win(a):
    return (a+1>=73) or (a+3>=73) or (a*2>=73)

def game(a,step):
    if step == 0 and all([can_win(a+1), can_win(a+3), can_win(a*2)]):
        return 0
    if a>=73:
        return step == 2 or step == 4
    if step >4 :
        return 0
    if step%2==0:
        return all([game(a+1,step+1), game(a+3,step+1), game(a*2,step+1)])
    return any([game(a+1,step+1), game(a+3,step+1), game(a*2,step+1)])
for a in range(1,73):
    print(a, game(a,0))