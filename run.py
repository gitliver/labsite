#!/usr/bin/env python

import sys, os

# update sys.path so Python finds the myapp package
sys.path.append(os.path.join(os.getcwd(), 'labsite'))

# grab the application object
from myapp import application

if __name__ == "__main__":
    application.run()
