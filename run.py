#!/usr/bin/env python

import sys, os

# update sys.path so Python finds the myapp package
# sys.path.append(os.path.join(os.getcwd(), 'labsite'))
# print(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# grab the application object
from myapp import application

if __name__ == "__main__":
    application.run()
