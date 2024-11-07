import turtle

# Inisialisasi layar
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Inisialisasi turtle
pen = turtle.Turtle()
pen.speed(3)
pen.color("pink")
pen.width(3)

# Fungsi untuk menggambar hati
def draw_heart():
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

# Gambar hati
pen.penup()
pen.goto(0, -100)
pen.pendown()
draw_heart()

# Tulis teks "I Love You"
pen.penup()
pen.goto(0, 70)
pen.color("red")
pen.write("Love you Jonaa", align="center", font=("Arial", 24, "bold"))
pen.hideturtle()

# Menutup layar saat diklik
screen.exitonclick()
