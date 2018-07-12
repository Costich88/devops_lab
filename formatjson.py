#!/usr/bin/python3

import fileout
import json


class FormJson(fileout.FileOut):

        def out(self, filename):
                self.dictVlupt()
                dictVl = self.dictVl
                jOut = json.dumps(dictVl)
                print(jOut, file=open(self.filename+".json", "a"))
