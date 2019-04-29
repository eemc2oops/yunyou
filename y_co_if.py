from abc import ABCMeta, abstractmethod
import y_log

w2l = y_log.clog(__name__ == "__main__")

class air_if(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def tickets(self, city_from, city_to):
        pass
    
    @abstractmethod
    def gettickets(self, city_from, city_to):
        pass

def run_entry():
    w2l.info('{} run.'.format(__name__))

def module_entry():
    w2l.info('{} module run'.format(__name__))

if __name__ == '__main__':
    run_entry()
else:
    module_entry()
