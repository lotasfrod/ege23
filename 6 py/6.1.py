import turtle as t

k = 30
t.tracer(False)
t.left(90)

for i in range(11):
    t.forward(5*k)
    t.right(60)

t.up()
for x in range(-2,10):
    for y in range(-5,10):
        t.goto(x*k, y*k)
        t.dot(4)

t.done()