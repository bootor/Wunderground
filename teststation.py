# coding: utf-8


from include import forecast, key
import load_history, os

ICAO = 'SBBT'
KEYPATH = os.getcwd() + '/data/key.txt'

#load key for wunderground API
key = key.get_key(KEYPATH)

print(ICAO)
fc = forecast.get_forecast('test', key, ICAO)
print('Forecast:')
print(fc)
print('History:')
for year in range(2010, 2016, 5):
    hist = load_history.getmonthhistory(ICAO, year, 1)
    count = len(hist)
    nt = 0
    nh = 0
    np = 0
    for elem in hist:
        if len(elem[1]) > 0:
            nt += 1
        if len(elem[2]) > 0:
            nh += 1
        if len(elem[3]) > 0:
            np += 1
    print(year, 'year')
    print(hist, 'year')
    print('History temperature data:    ' + str(nt*100/count) + '%')
    print('History humidity data:       ' + str(nh*100/count) + '%')
    print('History precipitation data:  ' + str(np*100/count) + '%')

