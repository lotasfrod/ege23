import turtle as t

k = 20
t.left(90)
t.tracer(False)
t.screensize(1200)
for i in range(7):
    t.forward(10*k)
    t.left(120)

t.up()
for x in range(-10,10):
    for y in range(-10,10):
        t.goto(x*k, y*k)
        t.dot(4)

t.done()
