# coding: utf-8


from include import loadairports
import os, csv

STATIONSPATH = os.getcwd() + '/data/stations.csv'
SUMSTATESPATH = os.getcwd() + '/out/sumstates/'
HDD = 18
CDD = 25

#load all ICAO airports codes for all states in all countries
adata = loadairports.load_airports(STATIONSPATH)
for country in adata:
    for state in adata[country]:
        rows = csv.reader(open(SUMSTATESPATH + country.replace(' ', '_') + '-' + state.replace(' ', '_') + '.csv', 'r'), delimiter=';')
        newrows = []
        for row in rows:
            newrows.append(row)
        for idx in range(len(newrows)):
            if newrows[idx][1] != '__.__' and float(newrows[idx][1]) < HDD:
                newrows[idx].append('{:.2f}'.format(HDD - float(newrows[idx][1])))
            else:
                newrows[idx].append('0.00')
            if newrows[idx][1] != '__.__' and float(newrows[idx][1]) > CDD:
                newrows[idx].append('{:.2f}'.format(float(newrows[idx][1]) - CDD))
            else:
                newrows[idx].append('0.00')
        _writer = csv.writer(open(SUMSTATESPATH + country.replace(' ', '_') + '-' + state.replace(' ', '_') + '_HDDCDD.csv' , 'w'), delimiter=';', lineterminator='\n')
        txtrow = ['Date', 'Temperature', 'Humidity', 'Precipitation', 'HDD', 'CDD']
        _writer.writerow(txtrow)
        for row in newrows:
            _writer.writerow(row)
