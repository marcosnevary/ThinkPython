import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# **Resoluções dos Exercícios do Capítulo 1**""")
    return


@app.cell
def _(mo):
    mo.md(r"""1. How many seconds are there in 42 minutes 42 seconds?""")
    return


@app.cell
def _():
    seconds = 42
    minutes = 42
    seconds = seconds + minutes * 60
    seconds
    return minutes, seconds


@app.cell
def _(mo):
    mo.md(r"""2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.""")
    return


@app.cell
def _():
    miles = 10/1.61
    miles
    return (miles,)


@app.cell
def _(mo):
    mo.md(r"""3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?""")
    return


@app.cell
def _(miles, seconds):
    avg_pace = seconds/miles
    avg_pace
    return (avg_pace,)


@app.cell
def _(mo):
    mo.md(r"""4. What is your average pace in minutes and seconds per mile?""")
    return


@app.cell
def _(miles, seconds):
    avg_pace_min_sec = (seconds/60)/miles
    avg_pace_min_sec
    return (avg_pace_min_sec,)


@app.cell
def _(mo):
    mo.md(r"""5. What is your average speed in miles per hour?""")
    return


@app.cell
def _(miles):
    avg_speed = miles/((42 + 42/60)/60)
    avg_speed
    return (avg_speed,)


if __name__ == "__main__":
    app.run()
