import turtle as t

k = 20
t.tracer(False)
t.left(90)

for i in range(9):
    t.forward(12*k)
    t.right(90)

t.up()
for x in range(-1,25):
    for y in range(-1,25):
        t.goto(x*k, y*k)
        t.dot(4)
        

t.done()