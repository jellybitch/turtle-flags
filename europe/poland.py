import turtle
turtle.title("Poland Flag In Python")
s = turtle.getscreen()
t = turtle.Turtle()
t.pensize(10)
t.penup()

sp = input("Set speed to: ")
t.speed(int(sp))

t.fillcolor("white")
t.begin_fill()
t.goto(-240, 160)
t.pendown()
t.fd(480)
t.rt(90)
t.fd(320)
t.rt(90)
t.fd(480)
t.rt(90)
t.fd(320)
t.rt(180)

print("OUTLINE DONE")

t.end_fill()

print("WHITE FILL DONE")

t.fd(160)
t.fillcolor("#DC143C")
t.begin_fill()
t.lt(90)
t.fd(480)
t.rt(90)
t.fd(160)
t.rt(90)
t.fd(480)
t.rt(90)
t.fd(160)
t.rt(180)

print("RED OUTLINE DONE")

t.end_fill()

print("RED FILL DONE")
print("END")

turtle.done()
