import turtle
makaio=turtle.Turtle()
makaio.width(20)
makaio.speed(30)

def draw_star(color):
    makaio.color(color)
    for side in range(5):
        makaio.forward(100)
        makaio.right(144)
        

feeling=input("How are you feeling?")
if (feeling=='happy'):
    draw_star('pink')
elif(feeling=='sad'):
    draw_star('blue')

