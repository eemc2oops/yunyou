import y_log
import y_chunqiu

w2l = y_log.clog(__name__ == "__main__")

class airticket:
    '整合各接口查询的票务信息'
    def __init__(self):
        self.ch = y_chunqiu.chunqiu_air()

    def _ch_tickets(self, city_from, city_to):
        return self.ch.tickets(city_from, city_to)

    def tickets(self, city_from, city_to):
        for ticket in self._ch_tickets(city_from, city_to):
            yield ticket

    def test(self):
        #print(str(self.ch))
        for ticket in self.tickets('武汉', '东京'):
            print('from {} to {}, at {} {}, price {}, refer {} {}, airline {}'.format(ticket['from'], ticket['to'], ticket['data'], ticket['week'], ticket['price'], ticket['refer'], ticket['url'], ticket['airline']))

def run_entry():
    w2l.info("{0} run.".format(__name__))

    air = airticket()
    air.test()

def module_entry():
    w2l.info("{0} module run.".format(__name__))

if __name__ == "__main__":
    run_entry()
else:
    module_entry()
