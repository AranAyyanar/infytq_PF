import turtle 
wn = turtle.Screen()    
wn.setup(540,508)       

alex = turtle.Turtle()      
alex.shape("turtle")     
alex.color("blue")         

destination="east"
if (destination=="north"):
    alex.left(90)
    alex.forward(50)
elif(destination=="south"):
    alex.left(-90)
    alex.forward(50)
elif(destination=="west"):
    alex.left(180)
    alex.forward(50)
elif(destination=="east"):
    alex.left(0)
    alex.forward(50)
else:
    pass 
