"""
Opens the eur*.tro files and extracts the tropospheric zenith total delay (ZTD) data for selected GNSS stations defined
 in stations list.

LAPUP, A. Argiriou, 2020-12-15
"""

import glob
import pandas as pd
import datetime

file_list = glob.glob('eur*7.tro')
file_list = sorted(file_list)


stations = ['AUT1', 'DUTH', 'DYNG', 'LARM', 'NOA1', 'PAT0', 'TUC2']

for station in stations:
    print(station)

    output_file = station + '.tro'
    f2 = open(output_file, "w")

    for file in file_list:
        f = open(file, 'r')
        header = f.readline()
        position = header.find('EUR') + 4
        pattern = header[position:position + 2]

        for line in f:
            if ' ' + station + ' ' + pattern in line:
                f2.write(line)
        f.close()

    f2.close()

    df = pd.read_csv(output_file, header=None)

    years = []
    DoY = []
    secs_of_day = []
    ztd = []
    ztd_sigma = []
    Date_time = []

    for i in range(len(df)):
        df[0][i] = df[0][i].strip()
        years.append(int(df[0][i][5:7]) + 2000)
        DoY.append(int(df[0][i][8:11]))
        secs_of_day.append(int(df[0][i][13:17]))
        ztd.append(float(df[0][i][18:24]))
        ztd_sigma.append(float(df[0][i][26:29]))

    print('Character split completed')

    for i in range(len(df)):
        Date_time.append((datetime.datetime(years[i], 1, 1) + datetime.timedelta(DoY[i]) +
                          datetime.timedelta(seconds=secs_of_day[i])).strftime("%Y-%m-%d %H:%M:%S"))
    print('Datetime definition completed')

    df['Date_time'] = Date_time
    df['ztd'] = ztd
    df['ztd_sigma'] = ztd_sigma
    del df[0]

    df.to_csv(station + '.csv', index=False)
    del df

