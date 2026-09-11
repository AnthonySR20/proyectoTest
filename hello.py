import turtle
import random

# -----------------------------
# Configuración de la pantalla
# -----------------------------
pantalla = turtle.Screen()
pantalla.setup(width=800, height=600)
pantalla.bgcolor("black")
pantalla.title("Figuras geométricas en movimiento")
pantalla.tracer(0)

ANCHO = 800
ALTO = 600

# -----------------------------
# Crear figuras
# -----------------------------
figuras = []

colores = [
    "red",
    "blue",
    "green",
    "yellow",
    "cyan",
    "orange",
    "purple",
    "white"
]

formas = [
    "square",
    "circle",
    "triangle"
]

for i in range(10):

    figura = turtle.Turtle()
    figura.speed(0)
    figura.penup()

    # Forma aleatoria
    figura.shape(random.choice(formas))

    # Color aleatorio
    figura.color(random.choice(colores))

    # Tamaño
    tamaño = random.randint(1, 3)
    figura.shapesize(tamaño, tamaño)

    # Posición inicial
    figura.goto(
        random.randint(-350, 350),
        random.randint(-250, 250)
    )

    # Velocidad
    figura.dx = random.choice([-4, -3, 3, 4])
    figura.dy = random.choice([-4, -3, 3, 4])

    # Velocidad de rotación
    figura.rotacion = random.choice([-5, -3, 3, 5])

    figuras.append(figura)


# -----------------------------
# Movimiento
# -----------------------------
def mover():

    for figura in figuras:

        # Posición actual
        x = figura.xcor()
        y = figura.ycor()

        # Tamaño aproximado de la figura
        tamaño = 15 * figura.shapesize()[0]

        # Nuevas posiciones
        nuevo_x = x + figura.dx
        nuevo_y = y + figura.dy

        # -------------------------
        # Rebote izquierda / derecha
        # -------------------------
        if nuevo_x + tamaño >= ANCHO / 2:
            nuevo_x = ANCHO / 2 - tamaño
            figura.dx *= -1

        elif nuevo_x - tamaño <= -ANCHO / 2:
            nuevo_x = -ANCHO / 2 + tamaño
            figura.dx *= -1

        # -------------------------
        # Rebote arriba / abajo
        # -------------------------
        if nuevo_y + tamaño >= ALTO / 2:
            nuevo_y = ALTO / 2 - tamaño
            figura.dy *= -1

        elif nuevo_y - tamaño <= -ALTO / 2:
            nuevo_y = -ALTO / 2 + tamaño
            figura.dy *= -1

        # Aplicar movimiento
        figura.goto(nuevo_x, nuevo_y)

        # Girar
        figura.right(figura.rotacion)

    # Actualizar pantalla
    pantalla.update()

    # Continuar animación
    pantalla.ontimer(mover, 20)


# Iniciar
mover()

# Mantener ventana abierta
pantalla.mainloop()
