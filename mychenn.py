from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
# options = Options()
# options.headless = True # Безголовый запуск
try:
    a=("[name='credit_sum']")
    # browser = webdriver.Chrome(options = options)
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://calcus.ru/kreditnyj-kalkulyator-s-dosrochnym-pogasheniem')
    browser.find_element_by_css_selector(a).send_keys('3700000')
    browser.find_element_by_css_selector("[name='period']").send_keys('30')
    browser.find_element_by_css_selector("[name='percent']").send_keys('7.2')
    browser.find_element_by_css_selector("[name='date_start']").send_keys('07-09-2020')
    def addpay():
        for i in range(0, len(a)-1):
            browser.find_element_by_xpath('//div[1]/div[2]/div[1]/form/div[7]/div[2]/div/a').click()
            browser.find_element_by_xpath('//*[@id="addPaymentModal"]/div/div/form/div[1]/div[3]/div/div[1]/input').send_keys(a[i])
            browser.find_element_by_xpath('//*[@id="addPaymentModal"]/div/div/form/div[1]/div[4]/div[2]/div[1]/div/input').send_keys(a[i+1])
            select = Select(browser.find_element_by_xpath("//*[@id='addPaymentModal']/div/div/form/div[1]/div[5]/div[2]/div[1]/select"))
            select.select_by_value('2')
            browser.find_element_by_css_selector('.btn.btn-primary').click()

    a = '12-10-2020', '500000'
    addpay()
    a = '07-01-2021', '60000'
    addpay()
    a = '07-04-2021', '130000'
    addpay()
    a = '07-06-2021', '100000'
    addpay()

    def addpay_m():
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

    b = '07-11-2020', '10000'
    addpay_m()
    b = '07-12-2020', '6500'
    addpay_m()
    b = '07-02-2021', '10000'
    addpay_m()
    b = '07-02-2021', '10000'

    browser.find_element_by_css_selector('.calc-submit').click()
    browser.find_element_by_css_selector('.js-show-full-schedule').click()
    x = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/form/div[12]/div[1]")
    y = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[12]/div[2]/div')
    time.sleep(1.5)
    td = browser.find_element_by_css_selector('.result-placeholder-schedule').text
    print(td)
    data = open('data1.txt', 'w')
    data.write(td)

finally:
    time.sleep(90)
    browser.quit()