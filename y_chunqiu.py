from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlencode
import requests
import re
from selenium import webdriver

import y_log

w2l = y_log.clog(__name__ == "__main__")

class chunqiu_air:
    '''春秋'''
    def __init__(self):
        pass

    def _city_list(self):
        url = 'https://ajax.springairlines.com/cache/js/modules/data/citydict-zh-cn.js?vs=v2019041921'
        r = requests.get(url)
        if r.status_code != requests.codes.ok:
            w2l.error('{0} url {1} return {2}'.format(type(self), url, r.status_code))
            return

        print(requests.codes.ok)
        #print(r.text)
        #fmt = re.compile('define(.*?)')
        fmt = re.compile('.*?return (.*?)}\).*?$') 
        #txt = fmt.findall(r.text)
        #for txt in fmt.findall(r.text):
        #    print('============================')
        #    print(txt)

    def _city(self, city_from, city_to):
        pass

    def tickets(self, data, city_from, city_to):
        data = {
            'Departure' : '武汉',
            'Arrival' : '东京(成田)',
            'Active9s' : '0',
            'Currency' : '0',
            'SType' : '10',
            'DepartureDate' : '2019-04-26',
            'ReturnDate' : '',
            'IsIJFlight' : 'true',
            'IsBg' : 'false',
            'IsEmployee ': 'false',
            'SeatsNum' : '1',
            'IfRet' : 'false',
            'IsShowTaxprice' : 'true',
            'IsUM' : 'false',
            'Days' : '61',
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

    def test(self):
        self._city_list()
        #ch.tickets('20190808', ['WUH'], ['TK'])

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