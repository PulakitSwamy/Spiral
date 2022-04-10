import turtle as t

def spiral(sides, turn, color, width):
    pen = t.Turtle()
    pen.color(color)
    pen.width(width)
    pen.speed(100)
    for n in range(sides):
        pen.forward(n)
        pen.right(turn)

spiral(75, 45, "green", 5)