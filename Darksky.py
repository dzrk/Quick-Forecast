import urllib, json, datetime
from Utils import Utils
NOPE = ''
WEEK_LENGTH = 7
class DarkSky:
    def __init__(self):
        pass

    def get_data(self, pos_no, loc_name, lat, lng, date):
        util = Utils()
        api_key = 0 #API KEY
        url = urllib.urlopen("https://api.darksky.net/forecast/" + api_key + "/"
                             + str(lat) + "," + str(lng) + "?exclude=currently,hourly,flags&units=si")
        data = json.loads(url.read().decode('utf-8'))
        data_array = []
        for day in range(WEEK_LENGTH):
            temp_max = data['daily']['data'][day].get('temperatureMax',NOPE)
            temp_min = data['daily']['data'][day].get('temperatureMin',NOPE)
            precip_max = data['daily']['data'][day].get('precipIntensityMax', NOPE)
            cloud_cover = data['daily']['data'][day].get('cloudCover', NOPE)
            humidity = data['daily']['data'][day].get('humidity', NOPE)
            icon = data['daily']['data'][day].get('icon', NOPE)
            summary = data['daily']['data'][day].get('summary', NOPE)
            date_formatted = util.get_date(date)
            data_array.append([date_formatted, pos_no, loc_name, temp_max, temp_min, precip_max, cloud_cover, humidity, icon, summary])
            date += datetime.timedelta(days=1)
        return data_array