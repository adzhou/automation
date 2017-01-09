
from __future__ import print_function
import os
import csv
import config


class ToCSV(object):
    def __init__(self, filename=None, firstrow=None):
        self.filename = config.Csv_buildInfo_name if not filename else filename
        self.pre_csv(firstrow)
        # self.writer = csv.writer(file(filename, 'a'), dialect='excel')

    def set_filename(self, filename):
        self.filename = filename

    def create_csv(self, firstrow=None, tp='wb'):
        writer = csv.writer(file(self.filename, tp), dialect='excel')
        firstrow = firstrow if firstrow else config.Build_keys_to_save
        writer.writerow(firstrow)
        self.addwriter()

    def pre_csv(self, firstrow=None):
        # if not exist, create file and write first row.
        if not os.path.isfile(self.filename):
            self.create_csv(firstrow)

    def addwriter(self):
        # self.pre_csv()
        self.addwriter = csv.writer(file(self.filename, 'a'), dialect='excel')

    def addrow(self, row):
        self.addwriter.writerow(row)


class FromCSV(object):
    def __init__(self):
        pass