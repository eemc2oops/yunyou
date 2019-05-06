import time
from concurrent.futures import ThreadPoolExecutor

import y_log
import y_chunqiu

w2l = y_log.clog(__name__ == "__main__")

class airticket:
    '''整合各接口查询的票务信息'''
    def __init__(self):
        self.ch = y_chunqiu.chunqiu_air()
        
        self.air_intf = []
        self.air_intf.append(self.ch)
        
        self.executor = ThreadPoolExecutor(10)

    def _ch_tickets(self, city_from, city_to):
        return self.ch.tickets(city_from, city_to)

    @staticmethod
    def get_ticket_by_thread(obj, city_from, city_to):
        return obj.gettickets(city_from, city_to)

    def tickets(self, city_from, city_to):
        '''循环获取票务信息,运行速度慢,适合爬虫使用'''
        from_list = []
        to_list = []

        #print('begin ', time.strftime("%H:%M:%S"))
        for intf in self.air_intf:
            for ticket in intf.tickets(city_from, city_to):
                yield ticket
        #print('end ', time.strftime("%H:%M:%S"))

    def tickets_by_thread(self, city_from, city_to):
        '''多线程获取票务信息,运行速度快,适合界面使用'''
        from_list = []
        to_list = []
        
        for i in range(0, len(self.air_intf)):
            from_list.append(city_from)
            to_list.append(city_to)

        tickets_result = self.executor.map(airticket.get_ticket_by_thread, self.air_intf, from_list, to_list)

        for tickets in tickets_result:
            for ticket in tickets:
                yield ticket

    def test(self):
        #print(str(self.ch))
        #print('begin ', time.strftime("%H:%M:%S"))
        #for ticket in self.tickets('上海', '东京'):
            #print('from {} to {} at {},{} price {} type {} fly time {} no {} time {} - {} refer {} {} airline {}'.format(ticket['from'], ticket['to'], ticket['date'], ticket['week'], ticket['price'], ticket['airtype'], ticket['flytime'], ticket['flyno'], ticket['departuretime'], ticket['arrivaltime'], ticket['refer'], ticket['url'], ticket['airline']))
        #    pass
        #print('end ', time.strftime("%H:%M:%S"))
        
        print('begin ', time.strftime("%H:%M:%S"))
        for ticket in self.tickets_by_thread('上海', '东京'):
            pass
        print('end ', time.strftime("%H:%M:%S"))

def run_entry():
    w2l.info('{0} run.'.format(__name__))

    air = airticket()
    air.test()

def module_entry():
    w2l.info('{0} module run.'.format(__name__))

if __name__ == '__main__':
    run_entry()
else:
    module_entry()
