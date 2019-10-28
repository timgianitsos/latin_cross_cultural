# Latin Genre classifier

## Setup

1. Ensure you have `python` version 3.6 installed

1. Ensure you have `git` at least version 1.9 installed<sup id="a1">[1](#f1)</sup>

1. Ensure you have `pipenv` installed

1. Clone this repository:
	```bash
	git clone <url of this repo>
	```

1. Navigate inside the project folder:
	```bash
	cd <the project folder you just cloned>
	```

1. Create virtual environment<sup id="a2">[2](#f2)</sup>:
	```bash
	PIPENV_VENV_IN_PROJECT=true pipenv --python 3.6
	```

1. Enter virtual environment:
	```bash
	pipenv shell
	```

1. Install dependencies to the virtual environment:
	```bash
	pipenv install --dev
	```

To leave virtual environment, use `exit`. To enter virtual environment again, ensure you are in the project directory and run `pipenv shell`

## Analysis

1. Run feature extraction:
	```bash
	python run_feature_extraction.py feature_data.pickle
	```

1. Generate a csv from the data
	```bash
	python generate_csv.py
	```

## Reference

Features: https://github.com/qcrit/DSH-2018-LatinProseVerse/blob/459458b028e2ff3a234faa2496a279144a758cc8/stylometry/imports/api/stylometry.js

Data: https://github.com/qcrit/DSH-2018-LatinProseVerse/blob/459458b028e2ff3a234faa2496a279144a758cc8/stylometry_data_final.csv

## Footnotes
<b id="f1">1)</b> The project uses the `git` protocol to obtain the corpus. The corpus contains many more files than we will make use of, so we make use of `git`'s sparse checkout and shallow clone features to only download what we need (this is done automatically in the code). We must have [at least version 1.9 to perform a sparse checkout and shallow clone](https://stackoverflow.com/a/28039894/7102572).[↩](#a1)

<b id="f2">2)</b> The `pipenv` tool works by making project-specific directories (called virtual environments) that hold the dependencies for that project. Setting the `PIPENV_VENV_IN_PROJECT` environment variable will indicate to `pipenv` to make this virtual environment within the same directory as the project so that all the files corresponding to a project can be in the same place. This is [not default behavior](https://github.com/pypa/pipenv/issues/1382) (e.g. on Mac, the environments will normally be placed in `~/.local/share/virtualenvs/`). [↩](#a2)
