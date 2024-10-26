# Simple Simplifier

**Simply Simplify German Language**

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Usage

- Create a [Conda](https://docs.anaconda.com/miniconda/) environment: `conda create -n simplifier python=3.9`
- Activate the environment: `conda activate zix`
- Install the requirements: `pip install -r requirements.txt`

**Install the Simplifier as a package**

- `pip install git+https://github.com/rnckp/simple-simplifier`
- Alternatively clone the repo, change into the project directory and invoke: `python -m pip install .`

**Start the FastAPI server**

- `uvicorn fastapi_app:app --reload`

**Use the API**

- Open the notebook `simple-simplifier.ipynb` and follow the instructions.

## License

`simple-simplifier` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
