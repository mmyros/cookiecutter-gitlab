#! /usr/bin/env python
# Copyright (C) 2019 Uwe Schitt <uwe.schmitt@id.ethz.ch>

import os
import traceback

repo_name = "{{ cookiecutter.repo_name }}"

try:
    os.system("git init .")
    os.system("git add .")
    os.system("git commit -m 'initial commit'")
    print()
    print("initialized git repository.")
    print()
except:
    traceback.print_exc()
    raise ValueError("failed to initialize git in %s" % repo_name)
