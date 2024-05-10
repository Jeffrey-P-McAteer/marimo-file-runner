import marimo

__generated_with = "0.5.2"
app = marimo.App(width="full", app_title="Some Project of Mine")


@app.cell
def __():
    import json
    import requests
    import pandas
    return json, pandas, requests


@app.cell
def __(pandas):
    d = pandas.DataFrame([1, 2, 3, 4])
    return d,


@app.cell
def __(d):
    d
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
