# MLOps Basics

An educational Python project for the MLOps Basics course.

Implements regression metrics for evaluating pressure forecasts (in hPa):

- **RMSE** — Root Mean Squared Error
- **MAE** — Mean Absolute Error

Both functions are type-annotated and validate input lengths.

## Getting Started

Install [uv](https://docs.astral.sh/uv/), then clone the repository and install the dependencies:

```
git clone https://github.com/Svetlana88-n/MLOps-Basics.git
cd MLOps-Basics
uv sync
```

Run the project:

```
uv run mlops-basics
```

```
Pressure RMSE: 0.5874 hPa
```
## Code Quality
The project uses Ruff for linting and formatting and ty for static type checking.

```
uv run ruff check .
uv run ruff format --check .
uv run ty check
```
## Project Structure

```text
.
├── src/
│   └── mlops_basics/
│       ├── __init__.py  
│       └── __main__.py  
├── pyproject.toml       
├── uv.lock
└── README.md
```