#!/usr/bin/env python3

import requests, io, bs4, sys


def pull(department):
    if department == 'police': url = 'https://www1.cityoforlando.net/opd/activecalls/activecadpolice.xml'
    elif department == 'fire': url = 'https://www1.cityoforlando.net/opd/activecalls/activecadfire.xml'
    response = requests.get(url)
    return response.text[3:]


def parse(xml):
    file = io.StringIO(xml)
    soup = bs4.BeautifulSoup(file, 'xml')
    return soup


def main():
    if len(sys.argv) != 2 or sys.argv[1] != 'police' and sys.argv[1] != 'fire': sys.exit(1)

    xml = pull(sys.argv[1])
    soup = parse(xml)
    for call in soup.CALLS:
        print('{}: {}'.format(call.DESC.contents[0], call.LOCATION.contents[0]))


if __name__ == '__main__': main()
