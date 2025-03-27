#!/usr/bin/env python

# Standard Library
import os
import sys

# Third Party Stuff
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
