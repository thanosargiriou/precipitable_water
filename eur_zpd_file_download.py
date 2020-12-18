"""
Retrieves the eur*.tro.Z files from the repository

https://igs.bkg.bund.de/root_ftp/EUREF/products/

LAPUP, A. Argiriou, 2020-12-13
"""
import requests

for week in range(1564, 2130):
    #    print(week)
    url = 'https://igs.bkg.bund.de/root_ftp/EUREF/products/' + str(week) + '/eur' + str(week) + '7.tro.Z'
    #    print(url)
    r = requests.get(url)
    local_file = 'eur' + str(week) + '7.tro.Z'
    with open(local_file, 'wb') as f:
        f.write(r.content)
        f.close()
