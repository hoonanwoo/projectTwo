import os

def func( path = None ):
    if path == None:
        path = os.getcwd()
        return [ x for x in os.listdir(path) if os.path.isfile(x) if x.endswith('.pyc') ]
  

