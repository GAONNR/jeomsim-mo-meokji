import requests
import chooser
import time
import jandiurl


def choose_all_cases():
    return (chooser.choose_my_lunch(0, False),
            chooser.choose_my_lunch(1, False),
            chooser.choose_my_lunch(2, False))

inside, outside, no_matter = choose_all_cases()
now = time.localtime()

headers = {'Accept': 'application/vnd.tosslab.jandi-v2+json',
           'Content-Type': 'application/json; charset=utf-8'}
data = '''
{
    "body" : "☆★오늘 점심 뭐 먹지(%02d/%02d)★☆",
    "connectColor" : "#2196f3",
    "connectInfo": [{
        "title" : "1. 안에서먹",
        "description" : "%s"
    },
    {
        "title" : "2. 상관없",
        "description" : "%s"
    },
    {
        "title" : "3. 나가먹",
        "description" : "%s"
    }]
}
''' % (now.tm_mon, now.tm_mday, inside, no_matter, outside)

r = requests.post(jandiurl.url, data=data.encode('utf-8'), headers=headers)
