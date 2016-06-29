import turtle

def draw_square(some_turtle):
    
    some_turtle.color("yellow")
    some_turtle.shape("turtle")
    some_turtle.speed(30)
    for i in range(1,5):
        some_turtle.forward(150)
        some_turtle.left(90)

def draw_circle(loma):

    loma.shape("arrow")
    loma.color("yellow")
    loma.speed(1)
    loma.circle(100)

    

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    square = turtle.Turtle()
    for i in range(1,75):
        draw_square(square)
        square.left(5)
        if(i is 37):
            square.left(85)
            square.forward(300)
            square.backward(300)
            square.right(85)
        
    window.exitonclick()
    

draw_art()
