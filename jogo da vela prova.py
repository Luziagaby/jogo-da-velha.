from turtle import Turtle,onscreenclick, onkey, listen, Screen
lu = Turtle ()
tela = Screen()
lu.speed(0)
resultado = 0
numero = 0

def trocar ():
    global resultado
    global numero
    numero = numero + 1
    resultado = numero % 2


lu.forward(100)
lu.backward(100)
lu.right(90)
lu.forward(100)
lu.left(180)
lu.forward(100)
lu.forward(100)
lu.backward(100)
lu.left(90)
lu.forward(100)
lu.left(180)
lu.forward(200)
lu.left(90)
lu.forward(100)
lu.backward(100)
lu.right(90)
lu.forward(100)
lu.backward(100)
lu.right(90)
lu.forward(100)
lu.right(90)
lu.forward(200)
lu.backward(300)
lu.forward(100)
lu.left(90)
lu.forward(100)
lu.backward(100)
lu.right(90)
lu.forward(100)
lu.left(90)
lu.forward(100)

def jogar(x, y): 
    lu.penup()
    lu.goto(x - (x % 100) + 50, y - (y % 100) + 50)
    if resultado == 0:
        x2()
    if resultado == 1:
        circulo()
    trocar()

def circulo():
    lu.color('red')
    lu.right(90)
    lu.forward(45)
    lu.left(90)
    r = 45
    lu.pendown()
    lu.circle(r)

def x2():
    lu.color('black')
    lu.pendown()
    lu.right(45)
    for _ in range(4):
        lu.forward(50)
        lu.forward(-50)
        lu.right(90)
    lu.left(45)

tela.onscreenclick(jogar)

listen()
tela.mainloop()