#!/usr/bin/env python

import sys, os

# get directory where this script resides
scripts = os.path.dirname(os.path.realpath(__file__)) 

# direct Flask to use this virtualenv (all its packages)
project_dir = os.path.abspath(scripts + '/../../private/mysite')
activate_this = '%s/bin/activate_this.py' % project_dir
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(project_dir)

# update sys.path so Python finds the myapp package
sys.path.append(scripts)

# grab the application object
from myapp import application

if __name__ == "__main__":
    application.run()
