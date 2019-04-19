from urllib.parse import quote
from urllib.parse import unquote
import requests
from selenium import webdriver

import y_log

w2l = y_log.clog(__name__ == "__main__")

class chunqiu_air:
    '''春秋'''
    def __init__(self):
        pass

    def _city_list(self):
        pass

    def tickets(self, city_from, city_to):
        url = 'https://flights.ch.com/WUH-NRT.html?Departure=%E6%AD%A6%E6%B1%89&Arrival=%E4%B8%9C%E4%BA%AC(%E6%88%90%E7%94%B0)&FDate=2019-04-21&ANum=1&CNum=0&INum=0&IfRet=false&SType=01&MType=0&IsNew=1'
        browser = webdriver.Firefox()
        browser.get(url)
        #print(browser.page_source)
        with open('web.html', 'wt', encoding='utf-8') as f:
            f.write(browser.page_source)
        browser.close()
        #print(unquote(url))
        #r = requests.get(url)
        #print(r.text)

def run_entry():
    w2l.info("{0} run.".format(__name__))

def module_entry():
    w2l.info("{0} module run.".format(__name__))

if __name__ == "__main__":
    run_entry()
else:
    module_entry()