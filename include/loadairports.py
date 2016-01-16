# coding: utf-8


def load_airports(path):
    ''' (none) -> dict
    Opens file /data/stations.csv wich has the folowing columns:
    Country; State; Airport name; Airport icao; WebLink; Lattitude; Longitude
    :return:
    Returns dict {Country : {State : [ICAO1, ICAO2 ... ] } }
    '''

    outdata = {}
    infile = open(path, 'r')
    lines = infile.readlines()
    for idx in range(1, len(lines)):
        splitted = lines[idx].split(';')
        country = splitted[0]
        state = splitted[1]
#        airport = splitted[2]
#        weblink = splitted[3]
#        lattitude = splitted[4]
#        longitude = splitted[5]
        icao = splitted[3]
        if country in outdata:
            if state in outdata[country]:
                if icao in outdata[country][state]:
                    pass
                else:
                    outdata[country][state].append(icao)
            else:
                outdata[country][state] = [icao]
        else:
            outdata[country] = {}
            outdata[country][state] = [icao]
    infile.close()
    return outdata


if __name__ == '__main__':
    import os
    print(load_airports(os.getcwd() + '/../data/stations.csv'))
