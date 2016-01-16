# coding: utf-8


from include import forecast, loadairports, key
import os

STATIONSPATH = os.getcwd() + '/data/stations.csv'
KEYPATH = os.getcwd() + '/data/key.txt'
FORECASTPATH = os.getcwd() + '/out/forecast/'
HISTORYPATH = os.getcwd() + '/out/history/'

#load all ICAO airports codes for all states in all countries
adata = loadairports.load_airports(STATIONSPATH)
#load key for wunderground API
key = key.get_key(KEYPATH)
#request forecast10day for all ICAO airports and save sata in forecastpath
forecast.saveforecast(FORECASTPATH, adata, key)
