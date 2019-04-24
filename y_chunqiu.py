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

    def show_city_list(self):
        for item in self.city_list:
            print(item)

    def _get_airport(self, city):
        '''跟据城市获取机场信息'''
        for item in self.city_list:
            if item['chs'].find(city) != -1:
                yield item

    def _tickets(self, city_from, city_to):
        '''尽可能多的获取信息'''
        data = {
            #'Departure' : '武汉',
            #'Arrival' : '东京(成田)',
            'Departure' : city_from,
            'Arrival' : city_to,
            'Active9s' : '0',
            'Currency' : '0',
            'SType' : '10',
            #'DepartureDate' : '2019-04-26',
            'DepartureDate' : (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            'ReturnDate' : '',
            'IsIJFlight' : 'true',
            'IsBg' : 'false',
            'IsEmployee ': 'false',
            'SeatsNum' : '1',
            'IfRet' : 'false',
            'IsShowTaxprice' : 'true',
            'IsUM' : 'false',
            #'Days' : '61',
            'Days' : '5',
        }
        
        url = 'https://flights.ch.com/Flights/MinPriceTrends'

        headers = {
            #'authority': 'flights.ch.com',
            #'path': '/Flights/MinPriceTrends',
            #'scheme': 'https',
            #'accept': '*/*',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            #'origin':'https://flights.ch.com',
            #'x-requested-with': 'XMLHttpRequest',
            #'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            #'accept-language': 'zh-CN,zh;q=0.9',
            #'Cookie' : 'PcPopAd_VisitWebSite=2019-04-12 15:02:30; cookie_policy=1; PcPopAd_XRL1554368800054=; s6=cd521279c3f24ebfad3fbce9d91b8528; c1=360_SEM_Bland_hexin_20170412_0001; gr_user_id=bc6f20cd-2413-411c-9628-5e20e87c4620; _ga=GA1.2.826550419.1555052516; grwng_uid=606acb96-f4f3-4bb2-9919-2054103c7ae8; preloadJs=.js%3Fvs%3Dv2019041002; IsShowTaxprice=false; hasProcessIP=1; g_refresh=0; SERVERID=7df100b0c5a941a824df718243406cad|1555895914|1555895912'
        }

        #browser = webdriver.Firefox()
        #browser.get(url)
        #print(browser.page_source)
        #with open('web.html', 'wt', encoding='utf-8') as f:
        #    f.write(browser.page_source)
        #browser.close()
        #print(unquote(url))
        r = requests.post(url, headers = headers, data = data)
        #print(r.cookies)
        #for key, value in r.cookies.items():
        #    print(key + ' = ' + value)
        print(r.text)

    def tickets(self, city_from, city_to):
        for city1 in self._get_airport(city_from):
            for city2 in self._get_airport(city_to):
                self._tickets(city1['code'], city2['code'])

    def test(self):
        #self._city_list()
        #self.show_city_list()
        self.tickets('武汉', '东京') 

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