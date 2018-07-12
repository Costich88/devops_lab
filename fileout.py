#!/usr/bin/python3

from abc import abstractmethod
from abc import ABC
from datetime import datetime
import psutil

counter = 1


class FileOut(ABC):
        global counter

        def __init__(self, filename):
                self.filename = filename
                super(FileOut, self).__init__()

        @abstractmethod
        def out():
                """Output format"""

        dictVl = {'SNAPSHOT': counter,
                  'DATE': "timedate",
                  'CPU': "0",
                  'Space Usage': "0",
                  'RAM Usage': "0",
                  'Bytes Read': "0",
                  'Bytes Write': "0",
                  'Traffic': "0"}

        def getCPU(self):
                return str(psutil.cpu_percent(interval=1)) + ' %'

        def getSPACE(self):
                return str(psutil.disk_usage('/').percent) + ' %'

        def getMEM(self):
                return str(psutil.virtual_memory().percent) + ' %'

        def getIO(self):
                self.read = psutil.disk_io_counters().read_bytes / 2**30
                self.read = format(self.read, '.2f') + ' GB'
                self.write = psutil.disk_io_counters().write_bytes / 2**30
                self.write = format(self.write, '.2f') + ' GB'
                return [self.read, self.write]

        def getNET(self):
                self.s = format((psutil.net_io_counters().bytes_sent / 2**20))
                self.r = format((psutil.net_io_counters().bytes_recv / 2**20))
                self.traffic = format(float(self.s) +
                                      float(self.r), '.2f') + ' MB'
                return self.traffic

        def getDATE(self):
                self.date = datetime.now()
                self.date = str(self.date)[:19]
                return self.date

        def dictVlupt(self):
                self.read, self.write = self.getIO()
                self.dictVl['SNAPSHOT'] = str(counter)
                self.dictVl['DATE'] = self.getDATE()
                self.dictVl['CPU'] = self.getCPU()
                self.dictVl['Space Usage'] = self.getSPACE()
                self.dictVl['RAM Usage'] = self.getMEM()
                self.dictVl['Bytes Read'] = self.read
                self.dictVl['Bytes Write'] = self.write
                self.dictVl['Traffic'] = self.getNET()
