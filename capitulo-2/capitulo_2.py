import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# **Resoluções dos Exercícios do Capítulo 2**""")
    return


@app.cell
def _():
    import math
    return (math,)


@app.cell
def _(mo):
    mo.md(r"""1. The volume of a sphere with radius r is (4/3)*πr³. What is the volume of a sphere with radius 5? Start with a variable named radius and then assign the result to a variable named volume. Display the result. Add comments to indicate that radius is in centimeters and volume is in cubic centimeters.""")
    return


@app.cell
def _(math):
    radius = 5 # cm
    volume = 4/3*math.pi*radius**3 # cm³

    volume
    return radius, volume


@app.cell
def _(mo):
    mo.md(r"""2. A rule of trigonometry says that for any value of x, cos²(x) + sin²(x) = 1. Let’s see if it’s true for a specific value of x like 42. Create a variable named x with this value. Then use math.cos and math.sin to compute the sine and cosine of x, and the sum of their squares. The result should be close to 1. It might not be exactly 1 because floating-point arithmetic is not exact—it is only approximately correct.""")
    return


@app.cell
def _(math):
    x = 42
    cos = math.cos(x)
    sin = math.sin(x)
    sum = cos**2 + sin**2

    sum
    return cos, sin, sum, x


@app.cell
def _(mo):
    mo.md(
        r"""
        3. Now let’s compute e² three ways:
            1. Use math.e and the exponentiation operator (**).
            2. Use math.pow to raise math.e to the power 2.
            3. Use math.exp, which takes as an argument a value, x, and computes ex.
        """
    )
    return


@app.cell
def _(math):
    first_way = math.e**2
    second_way = math.pow(math.e, 2)
    third_way = math.exp(2)

    print(first_way)
    print(second_way)
    print(third_way)
    return first_way, second_way, third_way


if __name__ == "__main__":
    app.run()
