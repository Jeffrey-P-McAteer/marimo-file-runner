import marimo

__generated_with = "0.5.2"
app = marimo.App()


@app.cell
def __():
    import json
    import requests
    import pandas

    return json, pandas, requests


if __name__ == "__main__":
    app.run()
