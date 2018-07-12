#!/usr/bin/python3

import fileout


class FormTxt(fileout.FileOut):

        def out(self, filename):

                self.dictVlupt()
                dictVl = self.dictVl

                print("SNAPSHOT {counter}: TIMESTAMP : {date}".format
                      (counter=dictVl['SNAPSHOT'], date=dictVl['DATE']),
                      'CPU load', 'Space Usage', 'RAM Usage', 'Bytes Read',
                      'Bytes Written', 'Traffic', sep="".ljust(10),
                      file=open(self.filename + ".txt", "a"))

                print("".ljust(44), dictVl['CPU'], dictVl['Space Usage'],
                      dictVl['RAM Usage'], dictVl['Bytes Read'],
                      dictVl['Bytes Write'], dictVl['Traffic'],
                      sep="".ljust(13), file=open(self.filename + ".txt", "a"))
