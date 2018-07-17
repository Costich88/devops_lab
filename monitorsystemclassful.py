#!/usr/bin/python3
# python app which would monitor the your system/server
""" In this task I've decided to dive deeper and
    try different python possibilities, such as abstract
    classes and methods, inheritance and other. Probably,
    it's not so neccessary for this exercise. But anyway,
    we are avoiding duplicate in methods by inheretance from
    the abstract. Despite it is not neccesary in Python,
    I divided classes into different files according to
    classical OOP principe.   """
import fileout
import formatjson
import formattxt
import json
import os.path
from time import sleep


def log(logformat):

        global counter

        if logformat == "txt":

                output = formattxt.FormTxt("output")
                output.out(logformat)

        elif logformat == "json":

                output = formatjson.FormJson("output")
                output.out(logformat)

        else:

                print("Incorrect output format")


with open("conf.json") as lines:
        conf = json.load(lines)
        sleeptime = conf['interval']
        logformat = conf['output']


while os.path.exists("conf.json"):
        log(logformat)
        fileout.FileOut.counter += 1
        sleep(sleeptime)
