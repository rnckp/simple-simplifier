# Simple Simplifier API

**Simply Simplify German Language -- API Version**

This is a simplified version of our [Language Simplification Tool](https://github.com/machinelearningZH/simply-simplify-language).

With this version you can pip install the core functionality and use language simplification via GPT-4o as a package. The API is built with [FastAPI](https://fastapi.tiangolo.com/) and can be used to simplify German language text in production environments where you want to integrate programmatically with other services.

## Usage

- Create a [Conda](https://docs.anaconda.com/miniconda/) environment: `conda create -n simplifier python=3.9`
- Activate the environment: `conda activate simplifier`
- Clone this repository. Change into the project directory.
- Install the requirements: `pip install -r requirements.txt`
- Export the OpenAI API key as an environment variable: `export OPENAI_API_KEY=your-api-key`

**Install the Simplifier as a package**

- `pip install git+https://github.com/rnckp/simple-simplifier`
- Alternatively invoke from the cloned project directory: `python -m pip install .`

**Start the FastAPI server**

- `uvicorn fastapi_app:app --reload`

**Test the API**

- Open the notebook `simple-simplifier.ipynb` and follow the instructions.

## License

`simple-simplifier` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
