# Latin Genre classifier

## Setup

1. Ensure you have `python` version 3.6 installed

1. Ensure you have `git` at least version 1.9 installed

1. Ensure you have `pipenv` installed

1. (Optional) Set environment variable by executing the following lines. These commands will indicate to pipenv to make the virtual environment in the same directory as the project so that all the files corresponding to a project can be in the same place. If your system uses `~/.bash_profile` (Mac for example), then run the commands with `~/.bash_profile`. If your system uses `~/.bashrc`(Linux for example), then replace `~/.bash_profile` with `~/.bashrc` in the below commands. This should only ever need to be done once on a system.
	```bash
	echo "#When pipenv makes a virtual environment, it will create it in the same directory as the project instead of ~/.local/share/virtualenv/" >> ~/.bash_profile
	echo "PIPENV_VENV_IN_PROJECT=true" >> ~/.bash_profile
	echo "export PIPENV_VENV_IN_PROJECT" >> ~/.bash_profile
	```
	Close terminal, then repoen terminal for the environment variable to take effect.

1. Clone this repository:
	```bash
	git clone <url of this repo>
	```

1. Navigate inside the project folder:
	```bash
	cd <the project folder you just cloned>
	```

1. Create virtual environment:
	```bash
	pipenv --python 3.6
	```

1. Enter virtual environment:
	```bash
	pipenv shell
	```

1. Install dependencies:
	```bash
	pipenv install --dev
	```

1. Run feature extraction:
	```bash
	python run_feature_extraction.py
	```

1. Leave virtual environment:
	```bash
	exit
	```

1. Enter virtual environment again (ensure you are in the project directory):
	```bash
	pipenv shell
	```

## Reference

Features: https://github.com/qcrit/DSH-2018-LatinProseVerse/blob/459458b028e2ff3a234faa2496a279144a758cc8/stylometry/imports/api/stylometry.js

Data: https://github.com/qcrit/DSH-2018-LatinProseVerse/blob/459458b028e2ff3a234faa2496a279144a758cc8/stylometry_data_final.csv
