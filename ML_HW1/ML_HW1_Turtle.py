import turtle


# Function to draw a rectangle with a given color
def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


# Function to draw a horse
def draw_horse():
    turtle.speed(2)
    turtle.color("brown")

    # Body
    turtle.penup()
    turtle.goto(-30, -30)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(60)
        turtle.left(90)
    turtle.end_fill()

    # Head
    turtle.penup()
    turtle.goto(30, 30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()


# Function to draw the background
def draw_background():
    # Draw grass
    draw_rectangle(-300, -150, 600, 300, "green")

    # Draw barn
    draw_rectangle(-100, -30, 200, 120, "red")


# Main function
def main():
    turtle.bgcolor("skyblue")  # Set background color

    draw_background()
    draw_horse()

    turtle.done()


if __name__ == "__main__":
    main()
