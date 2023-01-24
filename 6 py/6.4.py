import turtle as t
k = 50
t.tracer(False)
t.left(90)

for i in range(11):
    t.right(60)
    t.forward(10*k)
    t.right(60)

t.up()

for x in range(-1,10):
    for y in range(-7,10):
        t.goto(x*k, y*k)
        t.dot(4)

t.done()