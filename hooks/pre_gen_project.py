#! /usr/bin/env python
# Copyright (C) 2019 Uwe Schitt <uwe.schmitt@id.ethz.ch>

import re
import sys


MODULE_REGEX = r"^([a-zA-Z]+[-_]?)*[a-zA-Z]$"

repo_name = "{{ cookiecutter.repo_name }}"

if not re.match(MODULE_REGEX, repo_name):
    print(
        "ERROR: %s is not a valid Python module name! please use only characters a-z,"
        " A-Z, _ and -. " % repo_name
    )

    sys.exit(1)
