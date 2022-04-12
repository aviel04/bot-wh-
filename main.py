
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:\Downloads\chromedriver')
#path to chrome web driver above

driver.get('https://web.whatsapp.com/')
wait = WebDriverWait

#enter name of the user group or phone you want to send to
target = '"Rotem Dany"'

#replace the beloww string with yout own message 
string = "message sent using python !!!"

x_arg = '//span[contains(title,' +target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
group_title.click()
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)