from Darksky import DarkSky
from Utils import Utils
import datetime
WEEK_LENGTH = 7


class Main():

    def main(self):
        dark = DarkSky()
        util = Utils()
        location_data = util.open_file('location.csv')
        day = datetime.datetime.now()
        cursor = util.open_cnxn()
        cursor.execute('SELECT * FROM stg.WeatherForecast')
        dark_data = []
        for location in location_data:
            pos_no = location[0]
            loc_name = location[1]
            lat = location[2]
            lng = location[3]
            dark_data.append(dark.get_data(pos_no, loc_name, lat, lng, day))
            break
        for row in dark_data:
            util.write_file(util.get_date(day), row)
            util.send_data(cursor, row)

        cursor.commit()
if __name__ == '__main__':
    main = Main()
    main.main()
