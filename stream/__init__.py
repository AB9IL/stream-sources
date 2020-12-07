import csv
import json
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Stream:

    '''
    A Stream is responsible for writing items to stdout and caching their URLs
    in a log file so Sources can avoid pushing duplicates.

    Multiple sources should share a stream if they contain duplicates. For
    instance Top News and World News categories from the same news source may
    contain the same articles and should share the same stream.
    '''

    # Maximum number of recent log entries to store
    LOG_SIZE = 1000
    keyfiles = ['keys_good.csv', 'keys_bad.csv']
    global wordlist
    wordlist = []
    for keycsv in keyfiles:
        with open(keycsv, 'r') as mykeys:
            reader = csv.reader(mykeys)
            for row in reader:
                key_array = []
                key_array.append(row[0])
                key_array.append(row[1])
                wordlist.append(key_array)

    def __init__(self, out=sys.stdout, log='log.txt'):
        self.out = out
        self.log = log
        self.__log = self.__load_log()

    def __load_log(self):
        ''' Load log file from log_path. '''
        try:
            return open(self.log).read().split('\n')
        except:
            pass
        return []

    def __save_log(self):
        ''' Save log file to log_path. '''
        open(self.log, 'w').write('\n'.join(self.__log))

    def __contains__(self, url):
        ''' Check if url is in log. '''
        return url in self.__log

    def push(self, item):
        ''' Push JSON encoded item to output and append URL to log. '''
        thecount = 0
        for part in wordlist:
            if part[0] in item['title'].lower():
                thecount = thecount + int(part[1])
        if thecount == 0:
            print(Style.DIM + Fore.WHITE + item['date'] + "\n" + item['title'] + "\n" + item['url'])
        elif thecount in range(-2, 0):
            print(Style.DIM + Fore.RED + item['date'] + "\n" + item['title'] + "\n" + item['url'])
        elif thecount in range(1, 3):
            print(Style.DIM + Fore.GREEN + item['date'] + "\n" + item['title'] + "\n" + item['url'])
        elif thecount in range(-100, -3):
            print(Style.BRIGHT + Fore.RED + item['date'] + "\n" + item['title'] + "\n" + item['url'])
        elif thecount in range(3, 100):
            print(Style.BRIGHT + Fore.GREEN + item['date'] + "\n" + item['title'] + "\n" + item['url'])
        self.out.write('\n')
        self.out.flush()
        self.__log.append(item['url'])
        if len(self.__log) >= self.LOG_SIZE:
            self.__log = self.__log[-self.LOG_SIZE:]
        self.__save_log()
