# coding: utf-8


def get_key(path):
    infile = open(path,'r')
    key = infile.readline().replace('\n', '')
    infile.close()
    return key


if __name__ == '__main__':
    import os
    print(get_key(os.getcwd() + '/../data/key.txt'))
