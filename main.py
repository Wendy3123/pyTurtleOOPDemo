from turtle import Turtle,Screen    

wendy = Turtle()        #creates an object 

print(wendy)                #prints <turtle.Turtle object at 0x104cd9f40>
wendy.shape('turtle')       #change shape to turtle
wendy.color('hotpink')      #change color to hot pink
wendy.left(120)                 #move turtle wherever you like
wendy.forward(100)
wendy.left(120)
wendy.forward(100)
wendy.left(120)
wendy.forward(100)
wendy.left(120)
wendy.forward(140)
wendy.left(90)
wendy.forward(180)


my_screen = Screen()            #this creates the screen that we see showing up when we run this program
print(my_screen.canvheight)         #print 300 in terminal to show length of canvheight

my_screen.exitonclick()             #onclick will exit the white pop up screen