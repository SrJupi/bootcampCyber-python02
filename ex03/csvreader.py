import csv


class CsvReader(object):
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []

    def __enter__(self):
        with open(self.filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=self.sep)
            for i, row in enumerate(reader):
                if self.header and i == 0:
                    self.header_data = row
                else:
                    self.data.append(row)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
Return:
    nested list (list(list, list, ...)) representing the data.
"""

        return self.data[self.skip_top:(len(self.data) - self.skip_bottom)]

    def getheader(self):
        """ Retrieves the header from csv file.
Returns:
    list: representing the data (when self.header is True).
    None: (when self.header is False).
"""
        return self.header_data if self.header else None
