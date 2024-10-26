# Simple Simplifier API

**Simply Simplify German Language -- API Version**

This is a simplified version of our [Language Simplification Tool](https://github.com/machinelearningZH/simply-simplify-language).

With this version you can pip install the core functionality and use language simplification via GPT-4o as a package. The API is built with [FastAPI](https://fastapi.tiangolo.com/) and can be used to simplify German language text in production environments where you want to integrate programmatically with other services.

## Table of Contents

- [Usage](#usage)
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

**Test the API**

- Open the notebook `simple-simplifier.ipynb` and follow the instructions.

## License

`simple-simplifier` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
