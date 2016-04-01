"""
Main file for Effort Analysis
---
This program attempts to estimate the time it takes to write
the solution and then the time it took to write an exam.
With a few tweaks, it then attempts to extrapolate the
amount of effort taken v. the amount of effort expected.

Usage:
  effort.py (solution | submission | template) <path> [--scope=NAME] [--type=TYPE] [--output=FILE]

Options:
  -h --help       Show this screen
  --scope=NAME    Name of scope to operate in [default: global]
  --type=TYPE     Type of file [default: tex]
  --output=FILE   Type of output [default: console]

@author: Alvin Wan
@site: alvinwan.com
"""

import sys
from docopt import docopt
from modules.solution import SolutionModule
from modules.template import TemplateModule
from modules.submission import SubmissionModule

def main(arguments, f=None):
    if arguments['--output'] != 'console':
        f = open(arguments['output'], 'w')
        sys.stdout = f
    if arguments['solution']:
        results = SolutionModule(filepath=arguments['<path>'])
    if arguments['template']:
        results = TemplateModule(filepath=arguments['<path>'])
    if arguments['submission']:
        results = SubmissionModule(filepath=arguments['<path>'])
    print(results)
    if f: f.close()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Effort Analysis 1.0')
    main(arguments)
