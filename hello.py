import turtle
import random

# Configuración de la ventana
pantalla = turtle.Screen()
pantalla.setup(width=800, height=600)
pantalla.bgcolor("black")
pantalla.title("Figuras geométricas en movimiento")
pantalla.tracer(0)

# Crear figuras
figuras = []

colores = ["red", "blue", "green", "yellow", "cyan", "orange", "purple"]

for i in range(8):
    figura = turtle.Turtle()
    figura.speed(0)
    figura.penup()
    figura.shape("square")
    figura.color(random.choice(colores))

    # Tamaño aleatorio
    tamaño = random.randint(1, 3)
    figura.shapesize(tamaño, tamaño)

    # Posición inicial
    figura.goto(
        random.randint(-350, 350),
        random.randint(-250, 250)
    )

    # Velocidad
    figura.dx = random.choice([-3, -2, 2, 3])
    figura.dy = random.choice([-3, -2, 2, 3])

    figuras.append(figura)


# Animación
def mover():
    for figura in figuras:
        x = figura.xcor()
        y = figura.ycor()

        # Mover figura
        figura.goto(x + figura.dx, y + figura.dy)

        # Rebotar en los bordes
        if x > 380 or x < -380:
            figura.dx *= -1

        if y > 280 or y < -280:
            figura.dy *= -1

        # Rotación
        figura.right(5)

    pantalla.update()
    pantalla.ontimer(mover, 20)


mover()

pantalla.mainloop()
