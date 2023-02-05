import os
import pandas as pd

pd_encoding = 'unicode_escape'

class CsvFile():
    file_path = ''


    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = self.import_csv()

    def import_csv(self):
        file_path = os.path.join(self.file_path)
        return pd.read_csv(file_path, encoding=pd_encoding)



