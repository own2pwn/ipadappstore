# original script by Kyle Bareis
# rewritten by John Canniff

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

# add the ability to search by url, auto detect the url else name

loop = True

def applejacks(app_name, num):
    m = requests.get(
        'http://volume.itunes.apple.com/search?term=%s&entity='
        'iPadSoftware&attribute=allTrackTerm&limit=%s' % (app_name, num))
    data_string = json.loads(m.text)
    results = data_string.get('resultCount')
    return results, data_string

while loop == True:
    print(" ")
    app_name = input('Please enter the name of the '
                     'app you would like to search for: ').lower().replace(" ", "+")
    print(" ")

    num = input('Please enter the number of results (defaults 5): ') or 5
    results, data_string = applejacks(app_name, num)

    for count in range(results):
        print(" ")
        print("App Name:", data_string['results'][count]['trackName'])
        print("App Developer:", data_string['results'][count]['artistName'])
        print("Price:", data_string['results'][count]['formattedPrice'])
        print("Url:", data_string['results'][count]['trackViewUrl'])
        print("Device Based Licensing Enabled:", data_string['results'][count]['isVppDeviceBasedLicensingEnabled'])

    query = input("continue?")

    if query.lower() not in "yyes":
        loop = False
        break
