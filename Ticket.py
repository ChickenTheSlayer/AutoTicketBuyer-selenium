import time
from selenium import webdriver
from selenium.webdriver.common.by import By


login_url = "https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F"
target_url = "https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_1.429623e1IwIU9g&id=727777373377"
UserName = 'FillUserNameHere'
Password = 'FillPasswordHere'
# stops automation on chrome so it can't detect software
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# disables save password
prefs = {'credentials_enable_service': False, 'profile.password_manager_enabled': False}
option.add_experimental_option('prefs', prefs)
# Stops anti-python from Chrome
option.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=option)
driver.get(login_url)

try:
    driver.switch_to.frame(0)

    # login & password
    driver.find_element(By.CSS_SELECTOR, '#fm-login-id').send_keys(UserName)
    driver.find_element(By.CSS_SELECTOR, '#fm-login-password').send_keys(Password)
    time.sleep(0.5)

    slider = driver.find_element(By.CSS_SELECTOR, '#nc_1_n1z')
    slider.is_displayed()
    # Hold slider
    webdriver.ActionChains(driver).click_and_hold(on_element=slider).perform()
    # Move slider
    webdriver.ActionChains(driver).move_by_offset(xoffset=300, yoffset=0).perform()
    webdriver.ActionChains(driver).pause(0.5).release().perform()
except:
    print("No slider encountered")
# return to previous
# driver.switch_to.parent_frame()

driver.find_element(By.CSS_SELECTOR, '#login-form > div.fm-btn > button').click()

time.sleep(10)

driver.get(target_url)

# open target url (for Item)
driver.find_element(By.CSS_SELECTOR, '.buy-link').click()

# Select buyer
driver.find_element(By.CSS_SELECTOR, '.ticket-buyer-select .next-checkbox-label').click()

# Submit buy request
driver.find_element(By.CSS_SELECTOR, '.submit-wrapper .next-btn.next-btn-normal.next-btn-medium').click()
time.sleep(100)









