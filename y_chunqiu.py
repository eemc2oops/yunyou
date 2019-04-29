from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlencode
import requests
import re
import json
import string
from selenium import webdriver
import datetime
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

import y_co_if
import y_log

w2l = y_log.clog(__name__ == "__main__")

#time.strftime('%Y-%m-%d',time.localtime(time.time()))

class chunqiu_air(y_co_if.air_if):
    '''春秋'''
    def _get_city_list(self):
        url = 'https://ajax.springairlines.com/cache/js/modules/data/citydict-zh-cn.js?vs=v2019041921'
        r = requests.get(url)
        if r.status_code != requests.codes.ok:
            w2l.error('{0} url {1} return {2}'.format(type(self), url, r.status_code))
            return

        fmt = re.compile('.*?return (.*?)}\).*?$') 
        txts = fmt.findall(r.text)
        if len(txts) != 1:
            w2l.error('{0} get city list failed. {1}'.format(type(self), len(txts)))
            return

        data_list = json.loads(txts[0])

        city_list = []
        for k,v in data_list.items():
            #k,v  'FOC' , ['FuZhou', '福州', 'FZ|中国|三坊七巷|鼓山|zhongguo|sanfangqixiang|gushan', 'FOC', '中国']
            
            city = {
                'code' : k,
                'chs' : v[1],
                'eng' : v[0],
                'country' : v[4],
            }

            #print('city[%s] %s(%s) %s' % (city['code'], city['chs'], city['eng'], city['country']))

            city_list.append(city)

        if len(city_list) == 0:
            w2l.error('{0} get empty city list.'.format(type(self)))
            return

        self.city_list = city_list

    def __init__(self):
        self.city_list = []
        self._get_city_list()
        self.name = '春秋官网'
        self.url = 'www.ch.com'

    def __str__(self):
        return self.name

    def show_city_list(self):
        for item in self.city_list:
            print(item)

    def _get_airport(self, city):
        '''跟据城市获取机场信息'''
        for item in self.city_list:
            if item['chs'].find(city) != -1:
                yield item

    def _get_query_param(self, date, airport_from, airport_to):
        data = {
            'Departure' : airport_from,
            'Arrival' : airport_to,
            'FDate' : date,
            'ANum' : 1,
            'CNum' : 0,
            'INum' : 0,
            'IfRet' : 'false',
            'SType' : 0,
            'MType' : 0,
            'IsNew' : 1,
        }
        
        url = 'https://flights.ch.com/{}-{}.html'.format(airport_from, airport_to)
        
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        
        r = requests.get(url, headers = headers, data = data)
        if r.status_code != requests.codes.ok:
            w2l.error('{0} url {1} return {2} {3}'.format(type(self), url, r.status_code, date))
            return
        
        #print(r.text)
        #soup = BeautifulSoup(r.text, 'lxml')
        #print(soup)
        #print(soup.select)
        
        #with open('file.txt', 'wt', encoding='utf-8') as f:
        #    f.write(r.text)
        
        doc = pq(r.text)
        body = doc('html body')
        #searchPara = body("#searchPara")
        searchPara = body.children('div#searchPara')
        #hasvalue = searchPara.children('input[name,value]')
        hasvalue = searchPara.children('input[name][value]')
        param = {}
        for item in hasvalue.items():
            param[item.attr('name')] = item.attr('value')
            
        #print(param)
        
        return param
        

    def _get_air_plane(self, date, airport_from, airport_to):
        '''获取当日航班的详细信息'''
        '''
                            搞清楚  IsIJFlight 参数的含义
        Departure: 武汉
        Arrival: 东京(成田)
        DepartureDate: 2019-06-23
        IsIJFlight: true
        
        
        Departure: 上海
        Arrival: 东京(羽田)
        DepartureDate: 2019-04-28
        IsIJFlight: false
        '''
        param = self._get_query_param(date, airport_from, airport_to)
        data = {
            'Active9s' : None,
            'IsJC' : 'false',
            'IsShowTaxprice' : 'true',
            'Currency' : 0,
            'SType' : 0,
            'Departure' : airport_from,
            'Arrival' : airport_to,
            'DepartureDate' : date,
            #'Departure' : '武汉',
            #'Arrival' : '东京(成田)',
            #'DepartureDate' : '2019-04-27',
            'ReturnDate' : 'null',
            #'IsIJFlight' : 'true',
            'IsIJFlight' : param['isIJFlight'],
            #'IsBg' : 'false',
            'IsBg' : param['isBg'],
            #'IsEmployee' : 'false',
            'IsEmployee' : param['isEmployee'],
            'IsLittleGroupFlight' : 'false',
            'SeatsNum' : 1,
            'ActId' : 0,
            #'IfRet' : 'false',
            'IfRet' : param['ifRet'],
            'IsUM' : 'false',
            'CabinActId' : 'null',
            #'isdisplayold' : 'false',
            'isdisplayold' : param['isDisplayOld'],
        }
        
        url = 'https://flights.ch.com/Flights/SearchByTime'
        
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        
        r = requests.post(url, headers = headers, data = data)
        if r.status_code != requests.codes.ok:
            w2l.error('{0} url {1} return {2} {3}'.format(type(self), url, r.status_code, date))
            return
        
        plane_info = json.loads(r.text)
        #print(r.text)
        #print(plane_info['Route'][0][0]['Type'])
        
        if plane_info['Code'] != '0':
            w2l.error('{0} url {1} return {2} {3} {4} {5}'.format(type(self), url, plane_info['Code'], airport_from, airport_to, date))
        
        if len(plane_info['Route']) == 0:
            w2l.error('{0} url {1} empty msg {2} {3} {4}'.format(type(self), url, airport_from, airport_to, date))
        
        for items in plane_info['Route']:
            for item in items:
                plane = {
                    'airtype' : item['Type'],          # 飞机型号
                    'price' : item['MinCabinPrice'],   # 价格
                    'flytime' : item['FlightsTime'],   # 飞行时间
                    'flyno' : item['No'],     # 航班号
                    'departuretime' : item['DepartureTime'],     # 登机时间(当地时间)
                    'arrivaltime' : item['ArrivalTime'],     # 到达时间(当地时间)
                }
                yield plane
        
    def _ticketsbydate(self, date, airport_from, airport_to, days = 365):
        '''查询一年的数据'''
        data = {
            'Departure' : airport_from,
            'Arrival' : airport_to,
            'Active9s' : 0,
            'Currency' : 0,
            'SType' : 10,
            #'DepartureDate' : '2019-04-26',
            'DepartureDate' : date,
            'ReturnDate' : '',
            'IsIJFlight' : 'true',
            'IsBg' : 'false',
            'IsEmployee ': 'false',
            'SeatsNum' : 1,
            'IfRet' : 'false',
            'IsShowTaxprice' : 'true',
            'IsUM' : 'false',
            'Days' : days,
        }
        data1 = {
            'Currency' : 0,
            'DepartureDate' : date,
            'IsShowTaxprice' : 'true',
            'Departure' : airport_from,
            'Arrival' : airport_to,
            'SType' : '10',
            'IsIJFlight' : 'true',
            'Days' : days,
            'IfRet' : 'false',
            'ActId' : 0,
            'IsReturn' : 'false',
            'IsUM' : 'false',
        }
        
        url = 'https://flights.ch.com/Flights/MinPriceTrends'

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        
        #print(unquote(url))
        r = requests.post(url, headers = headers, data = data1)
        if r.status_code != requests.codes.ok:
            w2l.error('{0} url {1} return {2}  {3}'.format(type(self), url, r.status_code, date))
            return
        #with open('file.txt', 'wt', encoding='utf-8') as f:
        #    f.write(r.text)
        #print(r.text)

        #{"PriceTrends":[{"Date":"2019-04-24","DayOfWeek":"周三","Price":null,"ActPrice":null,"ActId":null},{"Date":"2019-04-25","DayOfWeek":"周四","Price":null,"ActPrice":null,"ActId":null},{"Date":"2019-04-26","DayOfWeek":"周五","Price":null,"ActPrice":null,"ActId":null}],"IsInternational":true,"IsShowTaxprice":true,"Code":"0","ErrorMessage":null,"Key":null}
        tickets_info = json.loads(r.text)
        if tickets_info['Code'] != '0' or tickets_info['ErrorMessage'] is not None:
            w2l.error('{0} url {1} return {2} {3} {4}'.format(type(self), url, tickets_info['Code'], tickets_info['ErrorMessage'], date))
            return

        for item in tickets_info['PriceTrends']:
            if item['Price'] is not None and item['Price'] > 0:
                #{'Date': '2019-04-27', 'DayOfWeek': '周六', 'Price': 2160, 'ActPrice': None, 'ActId': None}
                print(item)
                yield item
                
    def _tickets(self, airport_from, airport_to):
        '''
                                             查询一年的数据
                                            春秋的查询接口是在指定时间的前后各查一半的数据
                                            所以要查从明天起一年的数据，要从半年后开始查询
        '''
        for tick in self._ticketsbydate((datetime.date.today() + datetime.timedelta(days=173)).strftime('%Y-%m-%d'), airport_from, airport_to):
            yield tick

    def tickets(self, city_from, city_to):
        for city1 in self._get_airport(city_from):
            for city2 in self._get_airport(city_to):
                for info in self._tickets(city1['code'], city2['code']):
                    for plane in self._get_air_plane(info['Date'], city1['code'], city2['code']):
                        if info['Price'] != plane['price']:
                            w2l.debug('{}  from {} to {} date {} price {} {}'.format(type(self), city_from, city_to, info['Date'], info['Price'], plane['price']))
                        tick = {
                            'from' : city1['chs'],
                            'to' : city2['chs'],
                            'date' : info['Date'].replace('-', ''),
                            'week' : info['DayOfWeek'],
                            #'price' : info['Price'],
                            'price' : plane['price'],
                            'airtype' : plane['airtype'],          # 飞机型号
                            'flytime' : plane['flytime'],   # 飞行时间
                            'flyno' : plane['flyno'],     # 航班号
                            'departuretime' : plane['departuretime'],     # 登机时间(当地时间)
                            'arrivaltime' : plane['arrivaltime'],     # 到达时间(当地时间)
                            'refer' : self.name,  # 查询来源
                            'url' : self.url,  # 查询网站
                            'airline' : '春秋航空',  # 机票航空公司
                        }
                        #print('{} to {} at {},{}  price {}'.format(city1['chs'], city2['chs'], info['Date'], info['DayOfWeek'], info['Price']))
                        yield tick
    
    def gettickets(self, city_from, city_to):
        ticketlist = []

        for ticket in self.tickets(city_from, city_to):
            ticketlist.append(ticket)
            
        return ticketlist
    
    def ticketsbydate(self, date, city_from, city_to):
        for city1 in self._get_airport(city_from):
            for city2 in self._get_airport(city_to):
                for info in self._ticketsbydate(date, city1['code'], city2['code'], days = 1):
                    for plane in self._get_air_plane(info['Date'], city1['code'], city2['code']):
                        if info['Price'] != plane['price']:
                            w2l.debug('{}  from {} to {} date {} price {} {}'.format(type(self), city_from, city_to, info['Date'], info['Price'], plane['price']))
                        tick = {
                            'from' : city1['chs'],
                            'to' : city2['chs'],
                            'date' : info['Date'].replace('-', ''),
                            'week' : info['DayOfWeek'],
                            #'price' : info['Price'],
                            'price' : plane['price'],
                            'airtype' : plane['airtype'],          # 飞机型号
                            'flytime' : plane['flytime'],   # 飞行时间
                            'flyno' : plane['flyno'],     # 航班号
                            'departuretime' : plane['departuretime'],     # 登机时间(当地时间)
                            'arrivaltime' : plane['arrivaltime'],     # 到达时间(当地时间)
                            'refer' : self.name,  # 查询来源
                            'url' : self.url,  # 查询网站
                            'airline' : '春秋航空',  # 机票航空公司
                        }
                        #print('{} to {} at {},{}  price {}'.format(city1['chs'], city2['chs'], info['Date'], info['DayOfWeek'], info['Price']))
                        print('from {} to {} at {},{} price {} type {} fly time {} no {} time {} - {} refer {} {} airline {}'.format(tick['from'], tick['to'], tick['date'], tick['week'], tick['price'], tick['airtype'], tick['flytime'], tick['flyno'], tick['departuretime'], tick['arrivaltime'], tick['refer'], tick['url'], tick['airline']))
                        #yield tick
                        return tick
    

    def _test(self, city_from, city_to):
        for ticket in self.tickets(city_from, city_to):
            print('from {} to {} at {},{} price {} type {} fly time {} no {} time {} - {} refer {} {} airline {}'.format(ticket['from'], ticket['to'], ticket['date'], ticket['week'], ticket['price'], ticket['airtype'], ticket['flytime'], ticket['flyno'], ticket['departuretime'], ticket['arrivaltime'], ticket['refer'], ticket['url'], ticket['airline']))

    def test(self):
        #self._city_list()
        #self.show_city_list()
        #self._test('上海', '东京')
        #self._test('武汉', '东京')
        #self._test('武汉', '大阪')
        #self._test('武汉', '香港')
        self.ticketsbydate('2019-04-30', '武汉', '大阪')
        self.ticketsbydate('2019-05-05', '武汉', '东京')
        self.ticketsbydate('2019-05-07', '武汉', '大阪')
        #self._get_air_plane('2019-04-27', '武汉', '东京(成田)')
        #self._get_query_param('2019-05-27', 'SHA', 'HND')

def run_entry():

    w2l.info("{0} run.".format(__name__))

    ch = chunqiu_air()
    ch.test()

def module_entry():
    w2l.info("{0} module run.".format(__name__))

if __name__ == "__main__":
    run_entry()
else:
    module_entry()