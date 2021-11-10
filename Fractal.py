import turtle
plus=turtle.Turtle() #plus reprezinta turtle
plus.speed(10)
plus.getscreen().bgcolor("black")
plus.color("blue")
plus.hideturtle()
plus.penup()
plus.goto(-200,50)
plus.pendown()
def deseneaza(turtle, marime):
   if marime <= 3:
       return
   else:
      for i in range(4):
          #misc turtle in fata
          turtle.forward(marime)
          deseneaza(turtle,marime/2.5)
          turtle.backward(marime)
          turtle.left(90)
n=int(input("Introduceti marimea fractalului "))
deseneaza(plus,n)
input("Apasati o tasta pentru a incheia")

