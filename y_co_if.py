from abc import ABCMeta, abstractmethod
from concurrent.futures import ThreadPoolExecutor
import y_log

w2l = y_log.clog(__name__ == "__main__")

class air_if(object):
    __metaclass__ = ABCMeta
    executor = ThreadPoolExecutor(30)

    @abstractmethod
    def tickets(self, city_from, city_to):
        pass
    
    @abstractmethod
    def gettickets(self, city_from, city_to):
        pass
    
    def _ticketsarray(self, airport_from, airport_to):
        ticketarray = []
        
        for ticket in self._tickets(airport_from, airport_to)
            ticketarray.append(ticket)
            
        return ticketarray

    def _gettickets(self, from_list, to_list):
        if len(from_list) == 1:

    
def run_entry():
    w2l.info('{} run.'.format(__name__))

def module_entry():
    w2l.info('{} module run'.format(__name__))

if __name__ == '__main__':
    run_entry()
else:
    module_entry()
