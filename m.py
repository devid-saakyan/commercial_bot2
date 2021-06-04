from bs4 import BeautifulSoup, SoupStrainer
import ssl
from requests_html import HTMLSession
import pyppdf.patch_pyppeteer
import pyppeteer
import telebot
from time import sleep
import os

token = '1790070240:AAH4qSR3T2gbh-HCEH9ZR1FXNjL812W6-qU'
bot = telebot.TeleBot(token=token)

EXEC_PATH = os.environ.get("GOOGLE_CHROME_SHIM", None)
samolyot_spisok = ['https://samolet.ru/commercial/project/', 'https://samolet.ru/commercial/project/novoe-vnukovo/', 'https://samolet.ru/commercial/project/zarechye-park/',
                   'https://samolet.ru/commercial/project/mytischi-park/', 'https://samolet.ru/commercial/project/novodanilovskaya-8/', 'https://samolet.ru/commercial/project/sputnik/',
                   'https://samolet.ru/commercial/project/ostafevo/', 'https://samolet.ru/commercial/project/prigorod-lesnoe/', 'https://samolet.ru/commercial/project/alhimovo/',
                   'https://samolet.ru/commercial/project/lyubercy/', 'https://samolet.ru/commercial/project/nekrasovka/',
                   'https://samolet.ru/commercial/project/tomilino/', 'https://samolet.ru/commercialhttps://samolet.ru/novostroyki/', 'https://samolet.ru/commercial//samolet.ru/furniture/',
                   'https://samolet.ru/commercial/parking/', 'https://samolet.ru/commercial/storage/', 'https://samolet.ru/commercial/commercial/', 'https://samolet.ru/commercial/promo/',
                   'https://samolet.ru/commercial/settlement/', 'https://samolet.ru/commercial/purchase/refinancing/', 'https://samolet.ru/commercial/purchase/concession/',
                   'https://samolet.ru/commercial/payment/offers/', 'https://samolet.ru/commercial/documents/', 'https://samolet.ru/commercial/purchase/mortgage/',
                   'https://samolet.ru/commercial/purchase/installment/', 'https://samolet.ru/commercial/purchase/netting/', 'https://samolet.ru/commercial//samolet.ru/purchase/levelup/',
                   'https://samolet.ru/commercial/purchase/military/', 'https://samolet.ru/commercial/purchase/family/', 'https://samolet.ru/commercial/purchase/mothercare/',
                   'https://samolet.ru/commercial/purchase/subsidies/', 'https://samolet.ru/commercial/purchase/insurance/', 'https://samolet.ru/commercial/purchase/appraisal/',
                   'https://samolet.ru/commercialhttps://samolet.ru/invest/', 'https://samolet.ru/commercial/company/history/', 'https://samolet.ru/commercial/company/chiefs/',
                   'https://samolet.ru/commercial/news/', 'https://samolet.ru/commercial/investors/press/', 'https://samolet.ru/commercial/infograph/', 'https://samolet.ru/commercial/investors/land/',
                   'https://samolet.ru/commercial/company/requisites/']
# 'https://samolet.ru/commercial/project/bolshoe-putilkovo/',
pik_spisok = ['https://pik.ru/search/gp/commercial', 'https://pik.ru/search/sev-kuchino/commercial', 'https://pik.ru/search/bp2/commercial',
              'https://pik.ru/search/zhulebino/commercial', 'https://pik.ru/search/i-les/commercial', 'https://pik.ru/search/luberecky/commercial',
              'https://pik.ru/search/sp/commercial', 'https://pik.ru/search/kk15/commercial', 'https://pik.ru/search/luga/commercial',
              'https://pik.ru/search/kuzminskyles/commercial', 'https://pik.ru/search/bd/commercial', 'https://pik.ru/search/mkr-vostochnoe-butovo/commercial',
              'https://pik.ru/search/lyubpark/commercial', 'https://pik.ru/search/sles/commercial', 'https://pik.ru/search/park/commercial',
              'https://pik.ru/search/rk11/commercial', 'https://pik.ru/search/zhiloi-raion-yaroslavskii/commercial', 'https://pik.ru/search/raion-levoberezhnyi/commercial',
              'https://pik.ru/search/mf/commercial', 'https://pik.ru/search/mkrn-putilkovo/commercial']

ingrad_spisok = ['https://www.ingrad.ru/projects/mihaylova/select/commercial/all', 'https://www.ingrad.ru/projects/odingrad_family/select/commercial/all',
                 'https://www.ingrad.ru/projects/preobrazhenie/select/commercial/all', 'https://www.ingrad.ru/projects/novo17/select/commercial/all',
                 'https://www.ingrad.ruhttps://www.ingrad.ru/find-apartment', 'https://www.ingrad.ru/projects/pushkino/select/commercial/all',
                 'https://www.ingrad.ru/projects/medved/select/commercial/all', 'https://www.ingrad.ru/projects/vesna/select/commercial/all',
                 'https://www.ingrad.ru/projects/aventin/select/commercial/all', 'https://www.ingrad.ru/projects/gusbal/select/commercial/all']

fsk_spisok = ['https://fsk.ru/kommercheskaya-nedvizhimost/nastroenie', 'https://fsk.ru/kommercheskaya-nedvizhimost/1-lermontovskij',
              'https://fsk.ru/kommercheskaya-nedvizhimost/rimskiy', 'https://fsk.ru/kommercheskaya-nedvizhimost/datskij-kvartal',
              'https://fsk.ru/kommercheskaya-nedvizhimost/skolkovskiy', 'https://fsk.ru/kommercheskaya-nedvizhimost/pokolenie',
              'https://fsk.ru/kommercheskaya-nedvizhimost/skandinavskiy', 'https://fsk.ru/kommercheskaya-nedvizhimost/novogireevskii',
              'https://fsk.ru/kommercheskaya-nedvizhimost/nekrasovka', 'https://fsk.ru/kommercheskaya-nedvizhimost/pervyj-andreevskij',
              'https://fsk.ru/kommercheskaya-nedvizhimost/centr-2', 'https://fsk.ru/kommercheskaya-nedvizhimost/ramenskij']
#, 'https://fsk.ru/kommercheskaya-nedvizhimost/solncevo'

lsr_spisok = ['https://samolet.ru/commercial/msk/zhilye-kompleksy/zilart/', 'https://samolet.ru/commercial/msk/zhilye-kompleksy/leningradka-58/',
              'https://samolet.ru/commercial/msk/zhilye-kompleksy/luchi/', 'https://samolet.ru/commercial/msk/zhilye-kompleksy/n-nahabino/',
              'https://samolet.ru/commercial/msk/zhilye-kompleksy/nakhabino-yasnoe/', 'https://samolet.ru/commercial/msk/zhilye-kompleksy/grunevald/',
              'https://samolet.ru/commercial/msk/zhilye-kompleksy/new-domodedovo/']
#, 'https://samolet.ru/commercial/msk/zhilye-kompleksy/donskoy-olimp/'

await pyppeteer.launch(executablePath=EXEC_PATH,
            args=[
                "--no-sandbox",
                #"--single-process",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--no-zygote",
            ],)
def pik():
    url1 = 'https://www.pik.ru/projects/commercial'
    headers = {'accept': '*/*',
                   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrodiv78.0.3904.70 Safari/537.36'}
    session = HTMLSession(verify=False)
    context = ssl.SSLContext()
    r = session.get(url=url1, headers=headers, verify=False)
    r.html.render(timeout=1000)
    content = r.html.html
    spisok = []
    soup = BeautifulSoup(content, 'html.parser')
    spisok = []
    for link in soup.find_all('a'):
        try:
            spisok.append('https://pik.ru' + str(link.get('href')))
        except:
            bot.send_message(719274325, 'Ошибка в ПИК')
    spisok = [i for i in spisok if "/commercial" in i]
    session.close()
    return spisok

def ingrad():
    url1 = 'https://www.ingrad.ru/commercial/'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrodiv78.0.3904.70 Safari/537.36'}
    session = HTMLSession(verify=False)
    context = ssl.SSLContext()
    r = session.get(url=url1, headers = headers, verify = False)
    r.html.render(timeout=1000)
    content = r.html.html
    spisok = []
    soup = BeautifulSoup(content, "html.parser").find(class_ = 'project-list')
    for link in soup.find_all('a'):
        try:
            spisok.append('https://www.ingrad.ru' + str(link.get('href')))
        except:
            bot.send_message(719274325, 'Ошибка в инград')
    session.close()
    return spisok


def samolyot():
    url1 = 'https://samolet.ru/commercial/'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrodiv78.0.3904.70 Safari/537.36'}
    session = HTMLSession(verify=False)
    r = session.get(url=url1, headers=headers, verify=False)
    r.html.render(timeout=1000)
    content = r.html.html
    #print(content)
    spisok = []
    soup = BeautifulSoup(content, 'html.parser').find_all(class_ = 'menu__link js-ga-h _regular')
    for list in soup:
        try:
            spisok.append("https://samolet.ru/commercial" + str(list.get('href')))
        except:
            bot.send_message(719274325, 'Ошибка в самолёт')
    session.close()
    return spisok

def fsk():
    url1 = 'https://fsk.ru/kommercheskaya-nedvizhimost?page=1'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrodiv78.0.3904.70 Safari/537.36'}
    session = HTMLSession(verify=False)
    r = session.get(url=url1, headers=headers, verify=False)
    r.html.render(timeout=1000)
    content = r.html.html
    spisok = []
    soup = BeautifulSoup(content, 'html.parser').find_all(class_='complex-card')
    print(soup)
    for link in soup:
        try:
            spisok.append('https://fsk.ru' + str(link.get('href')))
        except:
            bot.send_message(719274325, 'Ошибка в фск')
    session.close()
    return spisok

def lsr():
    url1 = 'https://www.lsr.ru/msk/'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrodiv78.0.3904.70 Safari/537.36'}
    session = HTMLSession(verify=False)
    r = session.get(url=url1, headers=headers, verify=False)
    r.html.render(timeout=1000)
    content = r.html.html
    spisok = []
    soup = BeautifulSoup(content, 'html.parser').find_all(class_='col-32 col-md-15 col-md-post-2 col-bg-12 col-bg-post-1 col-lg-8 '
                                                             'col-xlg-8 col-xlg-post-1 b-build-card b-tabs__content b-tabs__content is-active')
    print(soup)
    for i in soup:
        try:
            spisok.append("https://samolet.ru/commercial" + str(i.find('a').get('href')))
        except:
            bot.send_message(719274325, 'Ошибка в ЛСР')
    session.close()
    return spisok

while True:
    for i in pik():
        if i not in pik_spisok:
            bot.send_message(719274325, "Пополнение в ПИК\nСсылка: {}".format(i))
            #bot.send_message(255056634, "Пополнение в ПИК\nСсылка: {}".format(i))
    pik_spisok = pik()
    print('сделал проверку пика')

    for i in ingrad():
        if i not in ingrad_spisok:
            bot.send_message(719274325, "Пополнение в Инград\nСсылка: {}".format(i))
            #bot.send_message(255056634, "Пополнение в Инград\nСсылка: {}".format(i))
    ingrad_spisok = ingrad()
    print('сделал проверку инграда')


    for i in samolyot():
        if i not in samolyot_spisok:
            bot.send_message(719274325, "Пополнение в Самолёт\nСсылка: {}".format(i))
            #bot.send_message(255056634, "Пополнение в Самолёт\nСсылка: {}".format(i))
    samolyot_spisok = samolyot()
    print('сделал проверку самолёт')

    for i in fsk():
        if i not in fsk_spisok:
            bot.send_message(719274325, "Пополнение в ФСК\nСсылка: {}".format(i))
            #bot.send_message(255056634, "Пополнение в ФСК\nСсылка: {}".format(i))
    fsk_spisok = fsk()
    print('сделал проверку фск')

    for i in lsr():
        if i not in lsr_spisok:
            bot.send_message(719274325, "Пополнение в ЛСР\nСсылка: {}".format(i))
            #bot.send_message(255056634, "Пополнение в ЛСР\nСсылка: {}".format(i))
    lsr_spisok = lsr()
    print('сделал проверку ЛСР')
    sleep(30)
