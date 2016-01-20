# coding: utf-8


try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
# url example for monthly history
# http://www.wunderground.com/history/airport/SBIL/2015/11/1/MonthlyHistory.html?format=1


def getmonthhistory(icao, year, month):
    outlist = []
    url = 'http://www.wunderground.com/history/airport/' + icao + '/' + str(year) + '/' + str(month) + \
          '/1/MonthlyHistory.html?format=1'
    request = urllib2.urlopen(url)
    data = request.readlines()
    for idx in range(2, len(data)):
        splitted = data[idx].decode("utf-8").replace(u'<br />\n', '').split(',')
        outlist.append([splitted[0], splitted[1], splitted[3], splitted[8], splitted[-4]])
    return outlist


if __name__ == '__main__':
#    print(getmonthhistory('SBIL', 2015, 1))
    import time, datetime, os.path
    from include import loadairports
    adata = loadairports.load_airports(os.getcwd() + '/data/stations.csv')
    for country in adata:
        for state in adata[country]:
            for icao in adata[country][state]:
                print('Loading history for ' + icao)
                file_path = os.getcwd() + '/out/history/' + icao + '.csv'
                if os.path.exists(file_path):
                    outfile = open(file_path, 'r')
                    lastdate = outfile.readlines()[-1].split(';')[0]
                    outfile.close()
                else:
                    lastdate = '2010-1-1'
                startyear = int(lastdate.split('-')[0])
                startmonth = int(lastdate.split('-')[1])
                outfile = open(file_path, 'a')
                for year in range(startyear, datetime.datetime.now().year + 1):
                    print(year)
                    if year == startyear:
                        currmonth = startmonth
                    else:
                        currmonth = 1
                    if year == datetime.datetime.now().year:
                        lastmonth = datetime.datetime.now().month + 1
                    else:
                        lastmonth = 13
                    for month in range(currmonth, lastmonth):
                        outlist = getmonthhistory(icao, year, month)
                        for elem in outlist:
                            if time.strptime(lastdate, '%Y-%m-%d') < time.strptime(elem[0], '%Y-%m-%d') < \
                                    time.strptime(str(datetime.datetime.now().year) + \
                             '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day),'%Y-%m-%d'):
                                outfile.write(elem[0] + ';' + elem[1] + ';' + elem[2] + ';' + elem[3] + ';' + elem[4] + '\n')
                outfile.close()
