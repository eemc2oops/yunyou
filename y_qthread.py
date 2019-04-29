import threading
import y_log

w2l = y_log.clog(__name__ == "__main__")

class query_thread(threading.Thread):
    def __init__(self, obj_intf, city_from, city_to):
        self.obj_intf = obj_intf
        self.city_from = city_from
        self.city_to = city_to

    def run(self):
        for ticket in self.obj_intf.tickets(city_from, city_to):
            print('from {} to {} at {},{} price {} type {} fly time {} no {} time {} - {} refer {} {} airline {}'.format(ticket['from'], ticket['to'], ticket['date'], ticket['week'], ticket['price'], ticket['airtype'], ticket['flytime'], ticket['flyno'], ticket['departuretime'], ticket['arrivaltime'], ticket['refer'], ticket['url'], ticket['airline']))
        
def run_entry():
    w2l.info('{} run.'.format(__name__))

def module_entry():
    w2l.info('{} module run'.format(__name__))

if __name__ == '__main__':
    run_entry()
else:
    module_entry()
