import importlib
from multiprocessing import cpu_count as CPUcount
from multiprocessing.dummy import Lock as ThreadLock
from multiprocessing.dummy import Pool as ThreadPool
import os
import sys
import time
from stream import Stream

one_cpu = CPUcount()
two_cpu = 2 * one_cpu

class Firehose:

    '''
    A Firehose manages all stream sources. Once started it will update them
    forever, pushing out their content to any stream they're attached to.
    '''

    def __init__(self, out=sys.stdout, delay=30.0):
        # file-like object to write output to
        self.out = out
        # seconds to sleep between each update loop
        self.delay = delay
        # list of installed source objects
        self._sources = []

    def add_source(self, name, stream=None):
        ''' Add source by name (with optional log stream). '''
        module = importlib.import_module('sources.' + name)
        # If no log stream is supplied one will be created
        if stream is None:
            os.makedirs('logs', exist_ok=True)
            # Logs are shared by root module
            if '.' in name:
                name = name.split('.')[0]
            log = os.path.join('logs', name + '.txt')
            stream = Stream(out=self.out, log=log)
        source = module.Source(stream)
        self._sources.append(source)
        return source

    def update(self):
        pool = ThreadPool(two_cpu)
        lock = ThreadLock()
        ''' Update all sources. '''
        for source in self._sources:
            with lock:
                try:
                    pool.apply_async(source.update())
                except Exception as e:
                    continue
        pool.close()
        pool.join()

    def start(self):
        ''' Start the firehose. '''
        while True:
            self.update()
            time.sleep(self.delay)
