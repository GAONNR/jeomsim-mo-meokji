import requests
import chooser
import time
import jandiurl


def inside():
    return chooser.choose_my_lunch(0, False)


def outside():
    return chooser.choose_my_lunch(1, False)


def no_matter():
    return chooser.choose_my_lunch(2, False)

now = time.localtime()

headers = {'Accept': 'application/vnd.tosslab.jandi-v2+json',
           'Content-Type': 'application/json; charset=utf-8'}

data_tuple = (now.tm_mon, now.tm_mday) + \
    tuple(map(lambda x: outside(), range(3))) + \
    tuple(map(lambda x: inside(), range(3))) + \
    tuple(map(lambda x: no_matter(), range(3)))

data = '''
{
    "body" : "Quod manducare prandium? (%02d/%02d)",
    "connectColor" : "#2196f3",
    "connectInfo": [{
        "title" : "1. Ex",
        "description" : "%s | %s | %s"
    },
    {
        "title" : "2. In",
        "description" : "%s | %s | %s"
    },
    {
        "title" : "3. Non refert",
        "description" : "%s | %s | %s"
    }]
}
''' % data_tuple

r = requests.post(jandiurl.url, data=data.encode('utf-8'), headers=headers)
