# Machine Learning

[Back to root README](../README.md)

Notebooks and helpers for the DeepLearning.AI Machine Learning Specialization, as a `uv` project.

## Structure

```text
machine-learning/
|-- pyproject.toml              # project + dependencies (numpy, pandas, scikit-learn, matplotlib, ipywidgets)
|-- uv.lock
|-- .python-version             # 3.13
`-- src/
    `-- machine_learning/       # installed package (editable), importable from notebooks
        |-- __init__.py
        |-- lab_utils_uni.py    # recreated course plotting helpers (single variable)
        `-- notebooks/
            `-- 01-cost-function.ipynb   # C1 W1 Lab03: cost function
```

## Contents

- `src/machine_learning/lab_utils_uni.py` - the course doesn't ship its plotting utilities, so this recreates them:
  - `plt_intuition(x, y)` - slider over `w` (b fixed): model fit + cost vs. `w`.
  - `plt_stationary(x, y)` - model fit + cost contour + 3D cost surface, with `w` / `b` / `rotate` sliders.
  - `soup_bowl()` - convex `J(w,b)` bowl.
  - Plots render into an ipywidgets `Image` (no ipympl) so they show once in VS Code, Colab and Jupyter.
  - Self-check: `uv run python -m machine_learning.lab_utils_uni`.
- `src/machine_learning/notebooks/` - one notebook per lab: the course's markdown, plus your own code.

## Setup

```sh
uv sync   # creates .venv and installs the package in editable mode
```

Then pick the `.venv` kernel in VS Code / Jupyter. Notebooks import helpers as
`from machine_learning.lab_utils_uni import ...`.

On a Colab kernel, the notebook downloads `lab_utils_uni.py` from GitHub, so push changes to it first.

## Guidelines

- New lab: add `notebooks/NN-topic.ipynb`; put reusable plotting in `lab_utils_*.py` next to `lab_utils_uni.py`.
- Add dependencies with `uv add <pkg>`.
