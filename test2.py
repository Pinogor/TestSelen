from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('https://calcus.ru/kreditnyj-kalkulyator-s-dosrochnym-pogasheniem')
browser.find_element_by_css_selector("[name='credit_sum']").send_keys('3700000')
browser.find_element_by_css_selector("[name='period']").send_keys('30')
browser.find_element_by_css_selector("[name='percent']").send_keys('7.2')
browser.find_element_by_css_selector("[name='date_start']").send_keys('07-09-2020')


a = {
    '12-10-2020': '500000',
    '07-01-2021': '60000',
    '07-04-2021': '130000',
}


def addpay_summa(key, value):
    browser.find_element_by_xpath('//div[1]/div[2]/div[1]/form/div[7]/div[2]/div/a').click()
    browser.find_element_by_xpath(
        '//*[@id="addPaymentModal"]/div/div/form/div[1]/div[3]/div/div[1]/input').send_keys(key)
    browser.find_element_by_xpath(
        '//*[@id="addPaymentModal"]/div/div/form/div[1]/div[4]/div[2]/div[1]/div/input').send_keys(value)
    select = Select(
        browser.find_element_by_xpath("//*[@id='addPaymentModal']/div/div/form/div[1]/div[5]/div[2]/div[1]/select"))
    select.select_by_value('2')
    browser.find_element_by_css_selector('.btn.btn-primary').click()

def addpay_srok(b):
    for i in range(0, len(b) - 1):
        browser.find_element_by_xpath('//div[1]/div[2]/div[1]/form/div[7]/div[2]/div/a').click()
        browser.find_element_by_xpath(
            '//*[@id="addPaymentModal"]/div/div/form/div[1]/div[3]/div/div[1]/input').send_keys(b[i])
        browser.find_element_by_xpath(
            '//*[@id="addPaymentModal"]/div/div/form/div[1]/div[4]/div[2]/div[1]/div/input').send_keys(b[i + 1])
        select = Select(browser.find_element_by_xpath(
            "//*[@id='addPaymentModal']/div/div/form/div[1]/div[5]/div[2]/div[1]/select"))
        select.select_by_value('1')
        browser.find_element_by_css_selector('.btn.btn-primary').click()

for key, value in a.items():
    addpay_summa(key=key, value=value)


browser.find_element_by_css_selector('.calc-submit').click()
browser.find_element_by_css_selector('.js-show-full-schedule').click()

url = browser.current_url
url1 = browser.page_source
df = pd.read_html(url1)[1]
df.to_excel('ipoteka.xlsx', index=False)
print()

time.sleep(1.5)
td = browser.find_element_by_css_selector('.result-placeholder-schedule').text
print(td)
data = open('data1.txt', 'w')
data.write(td)