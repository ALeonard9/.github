"""Deliberately dangerous code. See README.md in this directory.

Nothing imports or runs this; it exists so semgrep has a known finding.
"""

import subprocess


def run_whatever_the_user_typed(user_input):
    # Command injection: the whole point of this file.
    subprocess.call(user_input, shell=True)


def evaluate_whatever_the_user_typed(user_input):
    # Arbitrary code execution: likewise.
    return eval(user_input)
