import telebot
from selenium import webdriver
import time
import os

token = '1790070240:AAH4qSR3T2gbh-HCEH9ZR1FXNjL812W6-qU'
bot = telebot.TeleBot(token=token)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options, port=os.environ.get("PORT", 5000))

spisok_pik = ['https://www.pik.ru/search/sev-kuchino/commercial', 'https://www.pik.ru/search/kk15/commercial', 'https://www.pik.ru/search/i-les/commercial',
              'https://www.pik.ru/search/amur/commercial', 'https://www.pik.ru/search/luga/commercial', 'https://www.pik.ru/search/kuzminskyles/commercial',
              'https://www.pik.ru/search/bd/commercial','https://www.pik.ru/search/mkr-vostochnoe-butovo/commercial', 'https://www.pik.ru/search/lyubpark/commercial',
              'https://www.pik.ru/search/park/commercial', 'https://www.pik.ru/search/rk11/commercial', 'https://www.pik.ru/search/zhiloi-raion-yaroslavskii/commercial',
              'https://www.pik.ru/search/bp2/commercial', 'https://www.pik.ru/search/raion-levoberezhnyi/commercial', 'https://www.pik.ru/search/mles/commercial',
              'https://www.pik.ru/search/mf/commercial', 'https://www.pik.ru/search/mkrn-putilkovo/commercial', 'https://www.pik.ru/search/sp/commercial']

spisok_ingrad = ['https://www.ingrad.ru/projects/mihaylova/select/commercial/all', 'https://www.ingrad.ru/projects/odingrad/select/commercial/all',
                 'https://www.ingrad.ru/projects/odingrad_family/select/commercial/all','https://www.ingrad.ru/projects/preobrazhenie/select/commercial/all',
                 'https://www.ingrad.ru/projects/novo17/select/commercial/all', 'https://www.ingrad.ru/projects/pushkino/select/commercial/all',
                 'https://www.ingrad.ru/projects/medved/select/commercial/all', 'https://www.ingrad.ru/projects/vesna/select/commercial/all',
                 'https://www.ingrad.ru/projects/aventin/select/commercial/all', 'https://www.ingrad.ru/projects/gusbal/select/commercial/all']

spisok_samolyot = ['https://samolet.ru/commercial/project/sputnik/', 'https://samolet.ru/commercial/project/alhimovo/',
                   'https://samolet.ru/commercial/project/tomilino/', 'https://samolet.ru/commercial/project/ostafevo/',
                   'https://samolet.ru/commercial/project/bolshoe-putilkovo/', 'https://samolet.ru/commercial/project/lyubercy/',
                   'https://samolet.ru/commercial/project/prigorod-lesnoe/', 'https://samolet.ru/commercial/project/nekrasovka/']

spisok_samolyot_auction = ['https://auction.samolet.ru/catalog/3441', 'https://auction.samolet.ru/catalog/3440', 'https://auction.samolet.ru/catalog/3439']

spisok_fsk = ['https://fsk.ru/kommercheskaya-nedvizhimost/nastroenie','https://fsk.ru/kommercheskaya-nedvizhimost/1-lermontovskij',
              'https://fsk.ru/kommercheskaya-nedvizhimost/rimskiy','https://fsk.ru/kommercheskaya-nedvizhimost/datskij-kvartal',
              'https://fsk.ru/consent-personal-data','https://fsk.ru/consent-to-communication',
              'https://fsk.ru/kommercheskaya-nedvizhimost/skolkovskiy','https://fsk.ru/kommercheskaya-nedvizhimost/pokolenie',
              'https://fsk.ru/kommercheskaya-nedvizhimost/skandinavskiy','https://fsk.ru/kommercheskaya-nedvizhimost/novogireevskii',
              'https://fsk.ru/kommercheskaya-nedvizhimost/nekrasovka']
#,'https://fsk.ru/kommercheskaya-nedvizhimost/pervyj-andreevskij'

spisok_lsr = ['https://www.lsr.ru/msk/zhilye-kompleksy/zilart/', 'https://www.lsr.ru/msk/zhilye-kompleksy/leningradka-58/', 'https://www.lsr.ru/msk/zhilye-kompleksy/luchi/',
              'https://www.lsr.ru/msk/zhilye-kompleksy/n-nahabino/', 'https://www.lsr.ru/msk/zhilye-kompleksy/nakhabino-yasnoe/', 'https://www.lsr.ru/msk/zhilye-kompleksy/grunevald/',
              'https://www.lsr.ru/msk/zhilye-kompleksy/new-domodedovo/', 'https://www.lsr.ru/msk/zhilye-kompleksy/donskoy-olimp/']
#, 'https://www.lsr.ru/msk/biznes-tsentry/novyj-balchug/'
driver.get('https://www.pik.ru/projects/commercial')
time.sleep(5)
links = driver.find_element_by_class_name('cmHIDI').find_elements_by_tag_name('a')
array_of_links = []
new_link = None
for i in links:
    array_of_links.append(i.get_attribute('href'))
if len(array_of_links) > len(spisok_pik):
    for i in array_of_links:
        if i not in spisok_pik:
            new_link = i
spisok_pik = array_of_links
if new_link != None:
    print(new_link)
    bot.send_message(719274325, 'Пополнение в ПИК\n'
                                'Ссылка: {}'.format(new_link))
driver.quit()
time.sleep(10)

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options, port=os.environ.get("PORT", 5002))
driver.get('https://www.ingrad.ru/commercial/')
time.sleep(5)
array_of_links = []
blocks = driver.find_element_by_class_name('project-list').find_elements_by_class_name('col')
new_link = None
for i in blocks:
    array_of_links.append(i.find_element_by_tag_name('a').get_attribute('href'))
if len(array_of_links) > len(spisok_ingrad):
    for i in array_of_links:
        if i not in spisok_ingrad:
            new_link = i
spisok_ingrad = array_of_links
if new_link != None:
    bot.send_message(719274325, 'Пополнение в ИНГРАД\n'
                                'Ссылка: {}'.format(new_link))
driver.quit()
time.sleep(10)


driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options, port=os.environ.get("PORT", 5003))
driver.get('https://samolet.ru/commercial/')
time.sleep(5)
array_of_links = []
new_link = None
links = driver.find_element_by_class_name('projects-list__container').find_elements_by_tag_name('a')
for i in links:
    array_of_links.append(i.get_attribute('href'))
if len(array_of_links) > len(spisok_samolyot):
    for i in array_of_links:
        if i not in spisok_samolyot:
            new_link = i
spisok_samolyot = array_of_links
if new_link != None:
    bot.send_message(719274325, 'Пополнение в Самолёт\n'
                                 'Ссылка: {}'.format(new_link))
driver.quit()
time.sleep(5)


driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options, port=os.environ.get("PORT", 5004))
driver.get('https://auction.samolet.ru/catalog')
time.sleep(5)
array_of_links = []
new_link = None
links = driver.find_element_by_class_name('LotsList_ru0LU').find_elements_by_tag_name('a')
for i in links:
    array_of_links.append(i.get_attribute('href'))
if len(array_of_links) > len(spisok_samolyot_auction):
    for i in array_of_links:
        if i not in spisok_samolyot_auction:
            new_link = i
spisok_samolyot_auction = array_of_links
if new_link != None:
    bot.send_message(719274325, 'Пополнение в Самолет - аукцион\n'
                                'Ссылка: {}'.format(new_link))
driver.quit()
time.sleep(5)


driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options, port=os.environ.get("PORT", 5005))
driver.get('https://fsk.ru/kommercheskaya-nedvizhimost')
time.sleep(5)
array_of_links = []
new_link = None
links = driver.find_element_by_class_name('complex-list').find_elements_by_tag_name('a')
for i in links:
    array_of_links.append(i.get_attribute('href'))
if len(array_of_links) > len(spisok_fsk):
    for i in array_of_links:
        if i not in spisok_fsk:
            new_link = i
spisok_fsk = array_of_links
if new_link != None:
    bot.send_message(719274325, 'Пополнение в ФСК\n'
                                'Ссылка: {}'.format(new_link))
driver.quit()
time.sleep(5)


driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options, port=os.environ.get("PORT", 5006))
driver.get('https://www.lsr.ru/msk/')
time.sleep(5)
array_of_links = []
new_link = None
blocks = driver.find_elements_by_class_name('b-build-card__inner')
for i in blocks:
    array_of_links.append(i.find_element_by_tag_name('a').get_attribute('href'))
if len(array_of_links) > len(spisok_lsr):
    for i in array_of_links:
        if i not in spisok_lsr:
            new_link = i
spisok_lsr = array_of_links
if new_link != None:
    bot.send_message(719274325, 'Пополнение в ЛСР\n'
                                 'Ссылка: {}'.format(new_link))
driver.quit() 
time.sleep(10)
