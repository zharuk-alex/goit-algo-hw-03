import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=400):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    is_active = True
    while is_active:
        try:
            recursion_level = int(input("Enter the level of recursion: "))
            draw_koch_snowflake(order=recursion_level)
            is_active = False
        except ValueError:
            print("Value not is integer!")
        except KeyboardInterrupt:
            print("\nHave a nice day")
            is_active = False
