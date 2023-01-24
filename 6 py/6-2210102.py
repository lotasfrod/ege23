from re import T
import turtle as t

k = 10
t.tracer(False)
t.left(90)

for i in range(9):
    t.forward(18*k)
    t.right(72)

t.up()
for x in range(-1,30):
    for y in range(-5,41):
        t.goto(x*k,y*k)
        t.dot(4)

t.done()

