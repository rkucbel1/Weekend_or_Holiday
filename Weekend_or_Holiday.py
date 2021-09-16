#Program to update API if it is a weekend/holiday or not
import datetime
import requests
import os

token = os.environ.get('PA_API_TOKEN')
url_api = os.environ.get('LINK_WEEKEND_OR_HOLIDAY')

#CME 2021 Holiday Schedule
H1 = '2021-01-18'
H2 = '2021-02-15'
H3 = '2021-05-31'
H4 = '2021-07-05'
H5 = '2021-11-21'
H6 = '2021-12-24'

#Get if weekend or not
day_of_week = datetime.datetime.today().weekday()

if (day_of_week == 5) or (day_of_week == 6):
   weekend = True
else:
   weekend = False

#Get if holiday or not
today = datetime.date.today()
today = str(today)

if (today == H1) or (today == H2) or (today == H3) or (today == H4) or (today == H5) or (today == H6):
   holiday = True
else:
   holiday = False

#Update date and status in database
#There is only one element in this database
id_number = 1
header = {'Authorization': token}
url = url_api + str(id_number) + '/'

if holiday or weekend:
    payload = {'date': today, 'status': 'MKT_CLOSED'}
else:
    payload = {'date': today, 'status': 'MKT_OPEN'}

resp = requests.put(url, data=payload, headers=header)
print(resp.text)
