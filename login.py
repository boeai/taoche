from selenium import webdriver

import time

driver=webdriver.Chrome()
driver.get("https://home.taoche.com/login/")


class login():
    #登录
    def user_login(self,driver):
        driver.find_element_xpath("//*[@id='tc_search_txtErshouche']").send_key("test")

time.sleep(5)

driver.quit()

