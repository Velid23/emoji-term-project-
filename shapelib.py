import turtle
t=turtle
turtle.hideturtle()
turtle.Screen()

def Smiley_Face():
 #face
 turtle.penup()
 turtle.goto(-300,50)
 turtle.pendown()
 turtle.begin_fill()
 turtle.color(1, 0.686, 0.176)
 turtle.circle(60)
 turtle.end_fill()
 turtle.penup() 

 #left eye
 turtle.color('white')
 turtle.goto(-320,120)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(15)
 turtle.end_fill()
 turtle.penup() 

 #right eye
 turtle.color('white')
 turtle.goto(-280,120)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(15)
 turtle.end_fill()
 turtle.penup()

 #inside left eye
 turtle.color('black')
 turtle.goto(-320,125)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(8)
 turtle.end_fill()
 turtle.penup()

 #inside right eye
 turtle.color('black')
 turtle.goto(-280,125)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(8)
 turtle.end_fill()
 turtle.penup()

 #mouth
 turtle.color(1, 0.239, 0.882) 
 turtle.goto(-326,105)
 turtle.right(90)
 turtle.begin_fill()
 turtle.circle(25,180)
 turtle.end_fill()
 turtle.penup()

 #tooth
 turtle.color('white')
 turtle.goto(-318,103)
 turtle.right(90)
 turtle.begin_fill()
 turtle.forward(35)
 turtle.left(90)
 turtle.forward(3)
 turtle.left(90)
 turtle.forward(35)
 turtle.left(90)
 turtle.forward(3)
 turtle.end_fill()
 turtle.penup()

def cool():
 #face
 turtle.home()
 turtle.penup()
 turtle.goto(-120,50)
 turtle.pendown()
 turtle.begin_fill()
 turtle.color(1, 0.686, 0.176)
 turtle.circle(60)
 turtle.end_fill()
 turtle.penup() 

 #left glass
 turtle.color(0.192, 0.106, 0.255)
 turtle.goto(-150,120)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(20,360,20)
 turtle.end_fill()
 turtle.penup() 

 #right glass
 turtle.color(0.192, 0.106, 0.255)
 turtle.goto(-90,120)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(20,360,20)
 turtle.end_fill()
 turtle.penup()

 #left frame
 turtle.color(0.553, 0.392, 0.773)
 turtle.goto(-150,120)
 turtle.pendown()
 turtle.pensize(4)
 turtle.circle(20,360,20)
 turtle.penup() 

 #right frame
 turtle.color(0.553, 0.392, 0.773)
 turtle.goto(-90,120)
 turtle.pendown()
 turtle.pensize(4)
 turtle.circle(20,360,20)
 turtle.penup() 

 #bridge
 turtle.color(0.553, 0.392, 0.773)
 turtle.goto(-130,145)
 turtle.hideturtle()
 turtle.pendown()
 turtle.pensize(6)
 turtle.forward(20)
 turtle.penup()

 #inside left
 turtle.color('white')
 turtle.goto(-140,140)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(3)
 turtle.end_fill()
 turtle.penup()

 #inside right
 turtle.color('white')
 turtle.goto(-80,140)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(3)
 turtle.end_fill()
 turtle.penup()

 #  #mouth
 turtle.color(0.251, 0.165, 0.192) 
 turtle.goto(-142,105)
 turtle.right(70)
 turtle.pendown()
 turtle.pensize(6)
 turtle.circle(25,150)
 turtle.penup()

def suprised():
 #face
 turtle.home()
 turtle.penup()
 turtle.goto(30,50)
 turtle.pendown()
 turtle.begin_fill()
 turtle.color(1, 0.686, 0.176)
 turtle.circle(60)
 turtle.end_fill()
 turtle.penup() 

  #left eye
 turtle.color('white')
 turtle.goto(5,120)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(15)
 turtle.end_fill()
 turtle.penup() 

 #right eye
 turtle.color('white')
 turtle.goto(40,120)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(15)
 turtle.end_fill()
 turtle.penup()

 #inside left eye
 turtle.color('black')
 turtle.goto(5,125)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(8)
 turtle.end_fill()
 turtle.penup()

 #inside right eye
 turtle.color('black')
 turtle.goto(40,125)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(8)
 turtle.end_fill()
 turtle.penup()

  #mouth
 turtle.color(1, 0.239, 0.882) 
 turtle.goto(0,95)
 turtle.right(90)
 turtle.begin_fill()
 turtle.circle(20)
 turtle.end_fill()
 turtle.penup()


def lughing():
 turtle.home()
 turtle.penup()
 turtle.goto(180,50)
 turtle.pendown()
 turtle.begin_fill()
 turtle.color(1, 0.686, 0.176)
 turtle.circle(60)
 turtle.end_fill()
 turtle.penup() 

 #left eye
 turtle.color(0.251, 0.165, 0.192)
 turtle.goto(165,120)
 turtle.pensize(4)
 turtle.setheading(90)
 turtle.pendown()
 turtle.circle(10,180)
 turtle.penup()

 #right eye
 turtle.color(0.251, 0.165, 0.192)
 turtle.goto(210,120)
 turtle.pensize(4)
 turtle.setheading(90)
 turtle.pendown()
 turtle.circle(10,180)
 turtle.penup()

 #mouth
 turtle.color(1, 0.239, 0.882) 
 turtle.goto(155,100)
 turtle.begin_fill()
 turtle.circle(25,180)
 turtle.end_fill()
 turtle.penup()

 #tooth
 turtle.color('white')
 turtle.goto(160,98)
 turtle.begin_fill()
 turtle.right(90)
 turtle.forward(35)
 turtle.left(90)
 turtle.forward(3)
 turtle.left(90)
 turtle.forward(35)
 turtle.left(90)
 turtle.forward(3)
 turtle.end_fill()
 turtle.penup()

 turtle.goto(150,110)
 turtle.pendown()
 turtle.color('blue')
 turtle.right(-320)
 turtle.pensize(6)
 turtle.forward(20)
 turtle.penup()

 turtle.goto(215,110)
 turtle.pendown()
 turtle.color('blue')
 turtle.right(270)
 turtle.pensize(6)
 turtle.forward(20)
 turtle.penup()

