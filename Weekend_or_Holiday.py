#Program to update API if it is a weekend/holiday or not
import datetime
import requests
import os

token = os.environ.get('PA_API_TOKEN')
url_api = os.environ.get('LINK_WEEKEND_OR_HOLIDAY')

#CME 2022 Holiday Schedule
H1 = '2022-01-03'
H2 = '2022-01-17'
H3 = '2022-02-21'
H4 = '2022-04-15'
H5 = '2022-05-30'
H6 = '2022-06-20'
H7 = '2022-07-04'
H8 = '2022-09-05'
H9 = '2022-11-24'
H10 = '2022-12-26'
H11 = '2023-01-02'

#Get if weekend or not
day_of_week = datetime.datetime.today().weekday()

if (day_of_week == 5) or (day_of_week == 6):
   weekend = True
else:
   weekend = False

#Get if holiday or not
today = datetime.date.today()
today = str(today)

if (today == H1) or (today == H2) or (today == H3) or (today == H4) or (today == H5) or (today == H6) or (today == H7) or (today == H8) or (today == H9) or (today == H10) or (today == H11) :
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
