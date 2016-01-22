# coding: utf-8


from include import loadairports
import os, csv

CONFIGPATH = os.getcwd() + '/data/hddcdd.txt'
STATIONSPATH = os.getcwd() + '/data/stations.csv'
SUMSTATESPATH = os.getcwd() + '/out/sumstates/'


def loadconf(configpath):
    infile = open(configpath, 'r')
    lines = infile.readlines()
    conf = {}
    for line in lines:
        splitted = line.replace('\n', '').split(';')
        conf[splitted[0]] = [splitted[1], splitted[2]]
    return conf

def calc_hddcdd(adata, name, HDD, CDD):
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
            _writer = csv.writer(open(SUMSTATESPATH + name + '_' + country.replace(' ', '_') + '-' + state.replace(' ', '_') + '_HDDCDD.csv' , 'w'), delimiter=';', lineterminator='\n')
            txtrow = ['Date', 'Temperature', 'Humidity', 'Precipitation', 'HDD', 'CDD']
            _writer.writerow(txtrow)
            for row in newrows:
                _writer.writerow(row)

#load HDDCDD params for different coffee types
conf = loadconf(CONFIGPATH)
#load all ICAO airports codes for all states in all countries
adata = loadairports.load_airports(STATIONSPATH)

for idx in range(len(conf['name'])):
    calc_hddcdd(adata, conf['name'][idx], float(conf['HDD'][idx]), float(conf['CDD'][idx]))

