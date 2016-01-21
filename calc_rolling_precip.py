# coding: utf-8


from include import loadairports
import os, csv

STATIONSPATH = os.getcwd() + '/data/stations.csv'
SUMSTATESPATH = os.getcwd() + '/out/sumstates/'


def calc_precip(rows):
    sumprecip = 0
    for row in rows:
        sumprecip += float(row[3])
    return '{:.2f}'.format(sumprecip)

#load all ICAO airports codes for all states in all countries
adata = loadairports.load_airports(STATIONSPATH)
for country in adata:
    for state in adata[country]:
        rows = csv.reader(open(SUMSTATESPATH + country.replace(' ', '_') + '-' + state.replace(' ', '_') + '.csv', 'r'), delimiter=';')
        newrows = []
        for row in rows:
            newrows.append(row)
        for idx in range(len(newrows)):
            if idx < 29:
                newrows[idx].append('0.00')
            else:
                newrows[idx].append(calc_precip(newrows[idx-30:idx]))
        _writer = csv.writer(open(SUMSTATESPATH + country.replace(' ', '_') + '-' + state.replace(' ', '_') + '_prcp.csv' , 'w'), delimiter=';', lineterminator='\n')
        txtrow = ['Date', 'Temperature', 'Humidity', 'Precipitation', 'Precip(30)']
        _writer.writerow(txtrow)
        for row in newrows:
            _writer.writerow(row)