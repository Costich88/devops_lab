#!/usr/bin/python3
# python app which would monitor the your system/server

from datetime import datetime
from time import sleep
import psutil
import json
import os.path


counter = 1
line_width = 44
output = ""

dict = {
        'SNAPSHOT ': counter,
        'DATE': "timedate",
        'CPU': "0",
        'Space Usage': "0",
        'RAM Usage': "0",
        'Bytes Read': "0",
        'Bytes Write': "0",
        'Traffic': "0",
        }


def getCPU():
        return str(psutil.cpu_percent(interval=1)) + ' %'


def getSPACE():
        return str(psutil.disk_usage('/').percent) + ' %'


def getMEM():
        return str(psutil.virtual_memory().percent) + ' %'


def getIO():
        read = psutil.disk_io_counters().read_bytes / 1024**3
        read = format(read, '.2f') + ' GB'
        write = psutil.disk_io_counters().write_bytes / 1024**3
        write = format(write, '.2f') + ' GB'
        return [read, write]


def getNET():
        sebts = format((psutil.net_io_counters().bytes_sent / 1024**2))
        rebts = format((psutil.net_io_counters().bytes_recv / 1024**2))
        traffic = format(float(sebts) + float(rebts), '.2f') + ' MB'
        return traffic


def getDATE():
        date = datetime.now()
        date = str(date)[:19]
        return date


def dictupt():
        read, write = getIO()
        dict['SNAPSHOT'] = str(counter)
        dict['DATE'] = getDATE()
        dict['CPU'] = getCPU()
        dict['Space Usage'] = getSPACE()
        dict['RAM Usage'] = getMEM()
        dict['Bytes Read'] = read
        dict['Bytes Write'] = write
        dict['Traffic'] = getNET()


def outtxt():

        print("SNAPSHOT {counter}: TIMESTAMP : {date}".format
              (counter=dict['SNAPSHOT'], date=dict['DATE']), 'CPU load',
              'Space Usage', 'RAM Usage', 'Bytes Read', 'Bytes Written',
              'Traffic', sep="".ljust(10), file=open("output.txt", "a"))

        print("".ljust(line_width), dict['CPU'], dict['Space Usage'],
              dict['RAM Usage'], dict['Bytes Read'], dict['Bytes Write'],
              dict['Traffic'], sep="".ljust(13), file=open("output.txt", "a"))


def log(logformat):

        global counter

        if logformat == "txt":

                dictupt()
                outtxt()
                counter += 1

        elif logformat == "json":

                dictupt()
                jOut = json.dumps(dict)
                print(jOut, file=open("output.json", "a"))

        else:

                print("Incorrect output format")


with open("conf.json") as lines:
        conf = json.load(lines)
        sleeptime = conf['interval']
        logformat = conf['output']


while os.path.exists("conf.json"):
        log(logformat)
        sleep(sleeptime)
