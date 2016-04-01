# Effort Analysis
Estimates time taken for each student on an exam v. time expected to write solutions

# Installation

Clone the repository.

```
git clone git@github.com:CS70/effortanalysis
```

If Homebrew is not already installed, install package manager [Homebrew](brew.sh)

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Using brew, install Tesseract

```
brew install tesseract
```

Setup your virtual environment. The following will create a new environment called `effortanalysis`.

```
conda create -n effortanalysis python=3.4
```

Activate your virtual environment, and install all dependencies from `requirements.txt`.

```
source activate cs70
pip install -r requirements.txt
```

At this point, you may exit your virtual environment

```
source deactivate
```

Installation complete. See "How to Use" to get started.

# How to Use

Make sure to activate your virtual environment, if you haven't already. (If you are in the environment, your prompt will be prefixed by `(effortanalysis)`)

```
source activate effortanalysis
```

Here is usage information.

```
Usage:
  effort.py (solution | submission | template) <path> [--scope=NAME] [--type=TYPE] [--output=FILE]

Options:
  -h --help       Show this screen
  --scope=NAME    Name of scope to operate in [default: global]
  --type=TYPE     Type of file [default: tex]
  --output=FILE   Type of output [default: console]
```
