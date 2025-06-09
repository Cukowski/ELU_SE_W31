# Shopping Cart — CI Quality Assurance

![CI](https://github.com/Cukowski/ELU_SE_W31/actions/workflows/ci.yml/badge.svg)

This project calculates and displays the total price of items in a shopping cart.  
It includes **static analysis**, **unit tests**, and a **GitHub Actions CI pipeline** to maintain high code quality.


## Features

- Clean and modular Python code
- Automated testing using `unittest`
- Static analysis tools integrated:
  - `flake8` — PEP8 linter
  - `pylint` — Code quality checker
  - `bandit` — Security analyzer
- GitHub Actions CI pipeline triggered on every push


## Project Structure

- `shopping_cart.py` — core logic
- `test_shopping_cart.py` — unit tests
- `.github/workflows/ci.yml` — GitHub Actions workflow file


## How to Run

**Run the main script:**
```bash
python shopping_cart.py
```

**Run the tests:**

```bash
python test_shopping_cart.py
```


## GitHub Actions Setup

To manually create the workflow structure:

```bash
mkdir -p .github/workflows
touch .github/workflows/ci.yml
```

The `ci.yml` should be configured to run static analysis and tests.


## Fork & Attribution

Forked and improved from:
[shoklah/ELU\_SE\_W31](https://github.com/shoklah/ELU_SE_W31)


**Note:** If you fork or rename the repo, update the badge URL below:

```md
https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml/badge.svg
```
