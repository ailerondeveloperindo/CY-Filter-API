import sys, os
# adds working path to sys.path
sys.path.insert(0,os.path.abspath('./app/'))

from main import py_app

if __name__ == "__main__":
    py_app.run()
