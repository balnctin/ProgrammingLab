import csv
import datetime
from math import isnan


class ExamException(Exception):
    pass


class CSVFile():
    def __init__(self, name):
        self.name = name
        print('Name: {}'.format(self.name))
        if not isinstance(name, str):
            raise ExamException(
                'Errore: Il nome del file non é una stringa, non "{}" '.format(
                    type(name)))


class CSVTimeSeriesFile(CSVFile):
    def __init__(self, name):
        self.name = name
        print('Name: {}'.format(self.name))
        if not isinstance(name, str):
            raise ExamException(
                'Errore: Il nome del file non é una stringa, non "{}" '.format(
                    type(name)))

    def get_data(self, start=None, end=None):
        data = []
        try:
            my_file = open(self.name, 'r')
        except ExamException as e:
            print('Non posso aprire "my_file"')
            print('Non posso aprire un file non esistente'.format(e))

        if start is not None and end is not None:
                if start > end:
                    raise ExamException(
                        'Errore: start deve essere minore di end, invece ho avuto start ="{}", end ="{}"'
                        .format(start, end))
                if not isinstance(start, int):
                        raise ExamException(
                            'Errore: il parametro "start" deve essere un intero, non "{}"'
                            .format(type(start)))
                if not isinstance(end, int):
                        raise ExamException(
                            'Errore: il parametro "end" deve essere un numero intero, non "{}"'
                            .format(type(end)))
        csvreader = csv.reader(my_file)
        header = []
        header = next(csvreader)
        for row in my_file:
            row = row.split(',')
            try: row[1] = int(row[1])
            except: row[1]=0
            if isnan(row[1]): row[1] = 0
            elif row[1] < 0: row[1] = 0
            else: row[1] = int(row[1])
            data.append(row)    
        my_file.close()
        if start is None:
                    start = 0
        if end is None:
                    end = len(data)
        return data

#time_series_file = CSVTimeSeriesFile('data.csv')
#time_series = time_series_file.get_data()
#print('Dati nel file: {}'.format(time_series_file.get_data()))

def compute_avg_monthly_difference(time_series, first_year, last_year):
    time_series_file = CSVTimeSeriesFile(name=time_series)
    year = [0] * 12
    fy = int(first_year)
    ly = int(last_year)
    rows = time_series_file.get_data(fy,ly)
    print("CIAO",rows)
    if not isinstance(rows, list):
        raise ExamException("L'input non è una lista!")
    elif rows == []:
        raise ExamException("L'input contenente la serie è vuota!")
    if not isinstance(first_year, str):
        raise ExamException('Non è una stringa'.format(type(first_year)))
    if not isinstance(last_year, str):
        raise ExamException('Non è una stringa'.format(type(last_year)))
    avg_monthly_difference = []
    for idx, mese in enumerate(year):
        mese = []
        for row in rows:
            rowY=int(
            datetime.datetime.strptime(row[0], '%Y-%m').strftime("%Y"))
            rowM=int(
            datetime.datetime.strptime(row[0], '%Y-%m').strftime("%m"))
            if rowY <= ly and rowY >= fy and rowM == (idx + 1):
                mese.append(row)
        value = 0
        i = 0
        for row in mese:
          if row[1]==0: mese.remove(row)
        while i < (len(mese) - 1):
            diff = mese[i + 1][1] - mese[i][1]
            value += diff
            i += 1
        avg_monthly_difference.append((value / (len(mese)-1)))
    return avg_monthly_difference


#time_series = "data3.csv"
#print('Average monthly difference: {}'.format(
 #   compute_avg_monthly_difference(time_series, "1949", "1951")))