import requests
import jandiurl
import sys
import json


def main():
    headers = {'Accept': 'application/vnd.tosslab.jandi-v2+json',
               'Content-Type': 'application/json; charset=utf-8'}
    to_send = ''

    if len(sys.argv) > 1:
        to_send = sys.argv[1]
    else:
        to_send = input('Give me a string: ')

    data = json.dumps({'body': to_send})

    r = requests.post(jandiurl.url, data=data.encode(
        'utf-8'), headers=headers)

if __name__ == '__main__':
    main()
