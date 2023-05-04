import csv
import os


class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []

    def __enter__(self):
        if self.__check_args():
            try:
                f = open(self.filename, mode='r')
            except:
                return None
            else:
                reader = csv.reader(f, delimiter=self.sep)
                for i, row in enumerate(reader):
                    if not all(val.strip() for val in row):
                        return None
                    if self.header and i == 0:
                        self.header_data = [val.strip() for val in row]
                    else:
                        self.data.append([val.strip() for val in row])
                f.close()
                return self
        else:
            return None

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

    def __check_args(self):
        if not isinstance(self.filename, str) \
                or not os.path.exists(self.filename) \
                or not self.filename.endswith('.csv'):
            return False
        if not isinstance(self.sep, str):
            return False
        if not isinstance(self.header, bool):
            return False
        if not isinstance(self.skip_top, int) \
                or not isinstance(self.skip_bottom, int):
            return False
        return True


if __name__ == '__main__':
    with CsvReader('bad.csv', header=False) as manager:
        if manager is None:
            print('Empty manager... exiting...')
            exit()
        print(manager.filename)
        print(manager.getheader())
        for item in manager.getdata():
            print (item)
        #print(manager.getdata())
    # print(manager.data)
