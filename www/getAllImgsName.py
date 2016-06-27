import os

path = 'static/images/show/'

def getNames():
    return map(appendPath, os.listdir(path))

def appendPath(fileName):
    return path + fileName