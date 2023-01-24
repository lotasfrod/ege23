import turtle as t

k = 30
t.left(90)
t.tracer(False)
t.right(90)
t.forward(3*k)
t.right(270)
for i in range(12):
    t.forward(10*k)
    t.right(216)

t.up()

for x in range(-40,30):
    for y in range(-40,20):
        t.goto(x*k, y*k)
        t.dot(4)

t.done()








