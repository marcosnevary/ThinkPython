import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# **Resoluções dos Exercícios do Capítulo 4**""")
    return


@app.cell
def _(mo):
    mo.md(r"""## As animações não estão disponíveis pois o **marimo** não fornece suporte para a biblioteca **jupyturtle**.""")
    return


@app.cell
def _():
    from jupyturtle import make_turtle, forward, left, penup, pendown
    return forward, left, make_turtle, pendown, penup


@app.cell
def _(mo):
    mo.md(r"""1. Write a function called rectangle that draws a rectangle with given side lengths.""")
    return


@app.cell
def _(forward, left, make_turtle):
    def rectangle(height, length):
        for _ in range(2):
            forward(height)
            left(90)
            forward(length)
            left(90)

    make_turtle()
    rectangle(100, 30)
    return (rectangle,)


@app.cell
def _(mo):
    mo.md(r"""2. Write a function called rhombus that draws a rhombus with a given side length and a given interior angle.""")
    return


@app.cell
def _(forward, left, make_turtle):
    def rhombus(length, angle):
        for _ in range(2):
            forward(length)
            left(angle)
            forward(length)
            left(180 - angle)

    make_turtle()
    rhombus(50, 60)
    return (rhombus,)


@app.cell
def _(mo):
    mo.md(r"""3. Now write a more general function called parallelogram that draws a quadrilateral with parallel sides. Then rewrite rectangle and rhombus to use parallelogram.""")
    return


@app.cell
def _(forward, left, make_turtle, pendown, penup):
    def parallelogram(first_side, second_side, angle):
        for _ in range(2):
            forward(first_side)
            left(angle)
            forward(second_side)
            left(180 - angle)

    def rectangle_other(length, height):
        parallelogram(length, height, 90)

    def rhombus_other(length, angle):
        parallelogram(length, length, angle)

    make_turtle()
    penup()
    forward(-80)
    pendown()
    parallelogram(30, 50, 60)
    penup()
    forward(60)
    pendown()
    rectangle_other(40, 20)
    penup()
    forward(60)
    pendown()
    rhombus_other(50, 50)
    return parallelogram, rectangle_other, rhombus_other


@app.cell
def _(mo):
    mo.md(r"""4. Write an appropriately general set of functions that can draw shapes like this.""")
    return


@app.cell
def _(forward, left, make_turtle, pendown, penup):
    from math import cos, radians

    def triangle(length, angle):
        base = (2*length**2 - 2*length**2*cos(radians(angle)))**0.5
        forward(base)
        left(180 - (180 - angle)/2)
        forward(length)
        left(180 - angle)
        forward(length)
        left(180 - (180 - angle)/2)
        forward(base)
        left(angle)

    def polygon(num_sides, radius):
        angle = 360/num_sides
        for _ in range(num_sides):
            triangle(radius, angle)

    make_turtle(delay=0.02)
    penup()
    forward(-100)
    pendown()
    polygon(5, 30)
    penup()
    forward(80)
    pendown()
    polygon(8, 30)
    penup()
    forward(85)
    pendown()
    polygon(10, 30)

    return cos, polygon, radians, triangle


@app.cell
def _(mo):
    mo.md(r"""5. Write an appropriately general set of functions that can draw flowers like this.""")
    return


@app.cell
def _(forward, left, make_turtle, pendown, penup):
    from math import pi

    def polyline(n, length, angle):
        for _ in range(n):
            forward(length)
            left(angle)

    def arc(radius, angle):
        arc_length = 2 * pi * radius * angle / 360
        n = 30
        length = arc_length / n
        step_angle = angle / n
        polyline(n, length, step_angle)

    def petal(num, radius):
        angle = 360/num
        for _ in range(num):
            arc(radius, angle)
            left(180 - angle)
            arc(radius, angle)
            left(180)

    make_turtle(delay=0)
    penup()
    forward(-100)
    pendown()
    petal(6, radius=30)
    penup()
    forward(70)
    pendown()
    petal(8, radius=40)
    penup()
    forward(80)
    pendown()
    petal(10, radius=70)
    return arc, petal, pi, polyline


if __name__ == "__main__":
    app.run()
