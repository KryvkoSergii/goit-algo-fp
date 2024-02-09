import turtle

def draw_pifagor_tree(branch_length, t, angle, level):
    if level == 0:
        return
    else:
        # Намалювати гілку
        t.forward(branch_length)
        t.right(angle)

        # Рекурсивно малювати праву гілку
        draw_pifagor_tree(0.7 * branch_length, t, angle, level - 1)

        # Повернутися назад
        t.left(2 * angle)

        # Рекурсивно малювати ліву гілку
        draw_pifagor_tree(0.7 * branch_length, t, angle, level - 1)

        # Повернутися назад на початковий кут
        t.right(angle)
        t.backward(branch_length)

def main():
    # Введення рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії: "))

    # Налаштування вікна turtle
    window = turtle.Screen()
    window.bgcolor("white")

    # Створення туртлу
    tree_turtle = turtle.Turtle()
    tree_turtle.speed(2)
    tree_turtle.color("green")

    # Початкові налаштування
    tree_turtle.left(90)
    tree_turtle.up()
    tree_turtle.backward(100)
    tree_turtle.down()

    # Виклик функції для малювання дерева
    draw_pifagor_tree(100, tree_turtle, 20, level)

    # Закрити вікно при кліку
    window.exitonclick()

if __name__ == "__main__":
    main()
