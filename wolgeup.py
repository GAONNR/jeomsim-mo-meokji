import requests
import datetime
import jandiurl

today = datetime.date.today()
wolgeupnal = datetime.date(1, 1, 1)
if today.day <= 24:
    wolgeupnal = datetime.date(today.year, today.month, 24)
else:
    if today.month < 12:
        wolgeupnal = datetime.date(today.year, today.month + 1, 24)
    else:
        wolgeupnal = datetime.date(today.year + 1, 1, 24)

headers = {'Accept': 'application/vnd.tosslab.jandi-v2+json',
           'Content-Type': 'application/json; charset=utf-8'}
data = '''
{
    "body" : "Vade!",
    "connectColor" : "#e91e63",
    "connectInfo": [{
        "title" : "Gladiator opera stipendio",
        "description" : "**%d** diebus, usque payday"
    }]
}
''' % (wolgeupnal - today).days

if (wolgeupnal - today).days == 1:
    data = '''
{
    "body" : "Vade!",
    "connectColor" : "#e91e63",
    "connectInfo": [{
        "title" : "Pecuniam cras",
        "description" : "Veni, vidi, accepit"
    }]
}
'''

r = requests.post(jandiurl.url, data=data.encode('utf-8'), headers=headers)
