from queue import Queue
from threading import Thread
import time
import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
open('httpP.txt', 'w')
open('socksP.txt','w')
open('httpsP.txt', 'w')
def scraper_1():
    p_l=[]
    dr = webdriver.Chrome()
    dr.get('https://free-proxy-list.net/')
    for _ in range(1,20):
        for i in range(1,20):
            proxy = "{0}:{1}".format(dr.find_element_by_xpath(f'//*[@id="proxylisttable"]/tbody/tr[{i}]/td[1]').text,dr.find_element_by_xpath(f'//*[@id="proxylisttable"]/tbody/tr[{i}]/td[2]').text)
            print(proxy)
            open('httpP.txt','a').write(proxy+'\n')
        try:
            dr.find_element_by_xpath('//*[@id="proxylisttable_next"]/a').click()
        except:
            break
    dr.quit()
    return
def scraper_2():
    t_l=[]
    httpsproxies = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
    socksproxies = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all')
    for i in socksproxies.text.split('\n'):
        print(i)
        proxy=i.strip('\r')
        open('socksP.txt','a').write(proxy+'\n')
    for i in httpsproxies.text.split('\n'):
        print(i)
        proxy=i.strip('\r')
        open('httpP.txt','a').write(proxy+'\n')
    return


def scraper_4(key):
    def socks5():
        socks_l=[]
        try:
            with webdriver.Chrome() as d:
                d.get('https://spys.one/en/socks-proxy-list/')
                while True:
                    select = Select(d.find_element_by_xpath('//*[@id="xpp"]'))
                    select.select_by_value('5')
                    time.sleep(2)
                    try:
                        d.find_element_by_xpath(f'/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr[400]/td[1]').text
                        break
                    except:
                        continue
                for i in range(3, 503):
                    t = d.find_element_by_xpath(f'/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr[{i}]/td[1]').text
                    print(t)
                    socks_l.append(t)
        except Exception as e:
            socks5()
        for item in socks_l:
            open('socksP.txt', 'a').write(item+'\n')
        return socks_l

    def https():
        socks_l = []
        try:
            with webdriver.Chrome() as d:
                d.get('https://spys.one/en/https-ssl-proxy/')
                while True:
                    select = Select(d.find_element_by_xpath('//*[@id="xpp"]'))
                    select.select_by_value('5')
                    time.sleep(2)
                    try:
                        d.find_element_by_xpath(f'/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr[400]/td[1]').text
                        break
                    except:
                        continue
                for i in range(3, 503):
                    t = d.find_element_by_xpath(f'/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr[{i}]/td[1]').text
                    print(t)
                    socks_l.append(t)

        except Exception as e:
            print(e)
            https()
        for item in socks_l:
            open('httpsP.txt', 'a').write(item+'\n')
        return socks_l
    def http():
        http_l=[]
        try:
            with webdriver.Chrome() as d:
                d.get('https://spys.one/en/http-proxy-list/')
                while True:
                    select = Select(d.find_element_by_xpath('//*[@id="xpp"]'))
                    select.select_by_value('5')
                    time.sleep(2)
                    try:
                        d.find_element_by_xpath(f'/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr[400]/td[1]').text
                        break
                    except:
                        continue
                for i in range(3, 503):
                    t = d.find_element_by_xpath(f'/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr[{i}]/td[1]').text
                    print(t)
                    http_l.append(t)
        except Exception as e:
            print(e)
        for item in http_l:
            open('httpP.txt', 'a').write(item+'\n')
        return http_l
    if key == 'socks5':
        socks5()
    elif key == 'http':
        http()
    elif key == 'https':
        https()
    return


def main():
    t1 = Thread(target=scraper_1)
    t2 = Thread(target=scraper_2)
    t3 = Thread(target=scraper_4, args=('http',))
    t4 = Thread(target=scraper_4, args=('https',))
    t5 = Thread(target=scraper_4, args=('socks5',))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    return
q =Queue()
def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()
if __name__ == '__main__':
    main()




