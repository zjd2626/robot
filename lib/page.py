#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constant
import time

from read_conf import login_url
def get_into_powerview(driver, menu1, menu2):
        driver.get(login_url + "/home.do")
        driver.find_element_by_xpath("//span[contains(text(),'PowerView')]").click()
        driver.find_element_by_css_selector("a.ha-max").click()
        driver.switch_to.frame("ifr_appId_5")
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='mCSB_1_container']//span[contains(text(),'"+menu1+"')]/..")))
        driver.find_element_by_xpath("//div[@id='mCSB_1_container']//span[contains(text(),'"+menu1+"')]/..").click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='mCSB_1_container']//span[text()='"+menu2+"']")))
        driver.find_element_by_xpath("//div[@id='mCSB_1_container']//span[text()='"+menu2+"']").click()
        time.sleep(1)
