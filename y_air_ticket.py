import y_log
import y_chunqiu

w2l = y_log.clog(__name__ == "__main__")

class airticket:
    def __init__(self):
        pass

    def _ch_tickets(self, city_from, city_to):
        ch = y_chunqiu.chunqiu_air()
        ch.tickets(city_from, city_to)

    def tickets(self, city_from, city_to):
        self._ch_tickets(city_from, city_to)

def run_entry():
    w2l.info("{0} run.".format(__name__))

    air = airticket()
    air.tickets(['WH', 'WuHan', '武汉'], ['TK', 'CT'])

def module_entry():
    w2l.info("{0} module run.".format(__name__))

if __name__ == "__main__":
    run_entry()
else:
    module_entry()
