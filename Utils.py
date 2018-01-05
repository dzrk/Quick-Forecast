import csv, pyodbc, sys
from dateutil import parser
# csv format
# date pos loc high low rain cloud hum ico sum

class Utils():

    def get_date(self,date):
        return date.strftime("%Y-%m-%d")

    def write_file(self, file_name, data):
        with open(file_name + '.csv','wb') as fout:
            writer = csv.writer(fout)
            for row in data:
                writer.writerow(row)

    def open_file(self, file_name):
        csv_data = []
        path = 'C:\\Users\\derrickp\\PycharmProjects\\QuickForecast\\'
        with open(path + file_name, 'rb') as fin:
            reader = csv.reader(fin)
            for row in reader:
                csv_data.append(row) # saves all rows from csv
        fin.close()
        return csv_data

    def open_cnxn(self):
        cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};"
                              "Server=SVRSUNAPPS01;"
                              "Database=SSDATAMART;"
                              "Trusted_Connection=yes;")
        return cnxn.cursor()

    def send_data(self,cursor, data):
        f = lambda x: x if x is not '' else None
        for row in data:
            date_obj = parser.parse(row[0])
            try:
                cursor.execute("INSERT INTO [SSDATAMART].[stg].[WeatherForecast]("
                               "[Pos_Location]"
                               ", [Date]"
                               ", [Max_temp]"
                               ", [Min_temp]"
                               ", [Max_Precipitation]"
                               ", [Cloud_Cover]"
                               ", [Humidity]"
                               ", [Summary_Icon]"
                               ", [Summary]) "
                               "values(?,?,?,?,?,?,?,?,?)",
                               row[1], date_obj,
                               row[3], row[4],
                               f(row[5]), f(row[6]),
                               row[7], row[8],
                               row[9])
            except pyodbc.ProgrammingError as e:
                print e.args
                return sys.exit()