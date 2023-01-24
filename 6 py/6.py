import turtle as t
k = 10 #масштаб
t.tracer(False)
t.left(90) #развернуть черепаху на "север"

for i in range(11):
    
    t.forward(36*k)
    t.right(72)



   


t.up() #поднимим перо
for x in range(-16,10):
    for y in range(-5,41):
        t.goto(x*k, y*k) #в точку с заданными координатами
        t.dot(4) #ставим точку


t.done()