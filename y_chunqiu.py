from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlencode
import requests
import re
import json
import string
from selenium import webdriver
import datetime

import y_log

w2l = y_log.clog(__name__ == "__main__")

#time.strftime('%Y-%m-%d',time.localtime(time.time()))

class chunqiu_air:
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
            #city = {}
            #city['code'] = k
            #city['chs'] = v[1]
            #city['eng'] = v[0]
            #city['country'] = v[4]
            
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
        return self.name + ',' + self.url

    def show_city_list(self):
        for item in self.city_list:
            print(item)

    def _get_airport(self, city):
        '''跟据城市获取机场信息'''
        for item in self.city_list:
            if item['chs'].find(city) != -1:
                yield item

    def _tickets(self, city_from, city_to):
        '''查询一年的数据'''
        data = {
            'Departure' : city_from,
            'Arrival' : city_to,
            'Active9s' : '0',
            'Currency' : '0',
            'SType' : '10',
            #'DepartureDate' : '2019-04-26',
            'DepartureDate' : (datetime.date.today() + datetime.timedelta(days=173)).strftime('%Y-%m-%d'),
            'ReturnDate' : '',
            'IsIJFlight' : 'true',
            'IsBg' : 'false',
            'IsEmployee ': 'false',
            'SeatsNum' : '1',
            'IfRet' : 'false',
            'IsShowTaxprice' : 'true',
            'IsUM' : 'false',
            'Days' : '365',
        }
        
        url = 'https://flights.ch.com/Flights/MinPriceTrends'

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        
        #print(unquote(url))
        r = requests.post(url, headers = headers, data = data)
        if r.status_code != requests.codes.ok:
            w2l.error('{0} url {1} return {2}'.format(type(self), url, r.status_code))
            return
        #with open('file.txt', 'wt', encoding='utf-8') as f:
        #    f.write(r.text)
        #print(r.text)

        #{"PriceTrends":[{"Date":"2019-04-24","DayOfWeek":"周三","Price":null,"ActPrice":null,"ActId":null},{"Date":"2019-04-25","DayOfWeek":"周四","Price":null,"ActPrice":null,"ActId":null},{"Date":"2019-04-26","DayOfWeek":"周五","Price":null,"ActPrice":null,"ActId":null}],"IsInternational":true,"IsShowTaxprice":true,"Code":"0","ErrorMessage":null,"Key":null}
        tickets_info = json.loads(r.text)
        if tickets_info['Code'] != '0' or tickets_info['ErrorMessage'] is not None:
            w2l.error('{0} url {1} return {2} {3}'.format(type(self), url, tickets_info['Code'], tickets_info['ErrorMessage']))
            return

        for item in tickets_info['PriceTrends']:
            if item['Price'] is not None:
                #{'Date': '2019-04-27', 'DayOfWeek': '周六', 'Price': 2160, 'ActPrice': None, 'ActId': None}
                yield item

    def tickets(self, city_from, city_to):
        for city1 in self._get_airport(city_from):
            for city2 in self._get_airport(city_to):
                for info in self._tickets(city1['code'], city2['code']):
                    tick = {
                        'from' : city1['chs'],
                        'to' : city2['chs'],
                        'data' : info['Date'].replace('-', ''),
                        'week' : info['DayOfWeek'],
                        'price' : info['Price'],
                        'refer' : self.name,
                        'url' : self.url,
                        'airline' : '春秋航空',
                    }
                    #print('{} to {} at {},{}  price {}'.format(city1['chs'], city2['chs'], info['Date'], info['DayOfWeek'], info['Price']))
                    yield tick
                    

    def test(self):
        #self._city_list()
        #self.show_city_list()
        for ticket in self.tickets('上海', '东京'):
            print('from {} to {} at {},{} price {} refer {} {} airline {}'.format(ticket['from'], ticket['to'], ticket['data'], ticket['week'], ticket['price'], ticket['refer'], ticket['url'], ticket['airline']))

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