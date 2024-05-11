import marimo

__generated_with = "0.5.2"
app = marimo.App(width="full", app_title="Some Project of Mine")


@app.cell
def __():
    import pyomo
    return pyomo,


@app.cell
def __():
    import pyomo.environ as pyo

    model = pyo.ConcreteModel()

    model.x = pyo.Var([1, 2], domain=pyo.NonNegativeReals)

    model.OBJ = pyo.Objective(expr=2 * model.x[1] + 3 * model.x[2])

    model.Constraint1 = pyo.Constraint(expr=3 * model.x[1] + 4 * model.x[2] >= 1)
    return model, pyo


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
