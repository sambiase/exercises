#! /usr/bin/env python3
import os

__version__ = "0.1"
__author__ = "Sambiase"

lang = os.getenv("LANG")
if lang[:5] == "pt_BR":
    print("Olá")
else:
    print("Hello")
