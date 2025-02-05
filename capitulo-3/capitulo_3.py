import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# **Resolução dos Exercícios do Capítulo 3**""")
    return


@app.cell
def _(mo):
    mo.md(r"""1. Write a function named print_right that takes a string named text as a parameter and prints the string with enough leading spaces that the last letter of the string is in the 40th column of the display.""")
    return


@app.cell
def _():
    def print_right(text):
        spaces = 40 - len(text)
        print(f"{' '*spaces}{text}")

    print_right('Water')
    print_right('Fire')
    print_right('Computer Science')
    return (print_right,)


@app.cell
def _(mo):
    mo.md(r"""2. Write a function called triangle that takes a string and an integer and draws a triangle with the given height, made up of copies of the string.""")
    return


@app.cell
def _():
    def triangle(text, height):
        for i in range(1, height + 1):
            print(text*i)

    triangle('A', 10)
    return (triangle,)


@app.cell
def _(mo):
    mo.md(r"""3. Write a function called rectangle that takes a string and two integers and draws a rectangle with the given width and height, made up of copies of the string.""")
    return


@app.cell
def _():
    def rectangle(text, height, length):
        for i in range(height):
            print(text * length)

    rectangle('A', 4, 12)
    return (rectangle,)


@app.cell
def _(mo):
    mo.md(
        r"""
        4. The song “99 Bottles of Beer” starts with this verse:
            ```
            99 bottles of beer on the wall,
            99 bottles of beer.
            Take one down, pass it around,
            98 bottles of beer on the wall.
            ```
            Then the second verse is the same, except that it starts with 98 bottles and ends with 97. The song continues—for a very long time—until there are 0 bottles of beer. Write a function called bottle_verse that takes a number as a parameter and displays the verse that starts with the given number of bottles.
        """
    )
    return


@app.cell
def _():
    def bottle_verse(number):
        print(f'{number} bottles of beer on the wall,')
        print(f'{number} bottles of beer.')
        print('Take one down, pass it around,')
        print(f'{number - 1} bottles of beer on the wall.')

    for i in range(99, 0, -1):
        bottle_verse(i)
        print()
    return bottle_verse, i


if __name__ == "__main__":
    app.run()
