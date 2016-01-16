# coding: utf-8


from include import loadairports
import os, csv

STATIONSPATH = os.getcwd() + '/data/stations.csv'
HISTORYPATH = os.getcwd() + '/out/history/'
SUMSTATESPATH = os.getcwd() + '/out/sumstates/'

#load all ICAO airports codes for all states in all countries
adata = loadairports.load_airports(STATIONSPATH)
for country in adata:
    for state in adata[country]:
        maxtemp = {}
        mintemp = {}
        humidity = {}
        precip = {}
        date = []
        for icao in adata[country][state]:
            date = []
            rows = csv.reader(open(HISTORYPATH + icao + '.csv', 'r'), delimiter=';')
            for row in rows:
                dt = row[0]
                date.append(dt)

                if row[1] != '':
                    if not (dt in maxtemp):
                        maxtemp[dt] = [int(row[1])]
                    else:
                        maxtemp[dt].append(int(row[1]))
                else:
                    if not (dt in maxtemp):
                        maxtemp[dt] = []

                if row[2] != '':
                    if not (dt in mintemp):
                        mintemp[dt] = [int(row[2])]
                    else:
                        mintemp[dt].append(int(row[1]))
                else:
                    if not (dt in mintemp):
                        mintemp[dt] = []

                if row[3] != '':
                    if not (dt in humidity):
                        humidity[dt] = [int(row[3])]
                    else:
                        humidity[dt].append(int(row[3]))
                else:
                    if not (dt in humidity):
                        humidity[dt] = []

                if row[4] != '':
                    if not (dt in precip):
                        precip[dt] = [float(row[4])]
                    else:
                        precip[dt].append(float(row[4]))
                else:
                    if not (dt in precip):
                        precip[dt] = []

        _writer = csv.writer(open(SUMSTATESPATH + country.replace(' ', '_') + '-' + state.replace(' ', '_') + '.csv' , 'w'), delimiter=';', lineterminator='\n')
        for idx in range(len(date)):
            maxt = '_-.-_'
            mint = '_-.-_'
            hum = '_-.-_'
            prec = '_-.-_'
            if len(maxtemp[date[idx]]) > 0:
                maxt = '{:.2f}'.format(sum(maxtemp[date[idx]]) / len(maxtemp[date[idx]]))
            if len(mintemp[date[idx]]) > 0:
                mint = '{:.2f}'.format(sum(mintemp[date[idx]]) / len(mintemp[date[idx]]))
            if len(humidity[date[idx]]) > 0:
                hum = '{:.2f}'.format(sum(humidity[date[idx]]) / len(humidity[date[idx]]))
            if len(precip[date[idx]]) > 0:
                prec = '{:.2f}'.format(sum(precip[date[idx]]) / len(precip[date[idx]]))
            outrow = [date[idx], maxt, mint, hum, prec]
            _writer.writerow(outrow)
