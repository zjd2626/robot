# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import read_conf
import time


def get_driver():
    driver = webdriver.Firefox(firefox_binary=read_conf.firefox_bin, executable_path=read_conf.geckodriver)
    driver.set_window_size(1280,800)
    driver.maximize_window()
    driver.implicitly_wait(60)
    base_url = read_conf.login_url
    driver.get(base_url + "/")
    # driver.find_element_by_id("userName").clear()
    WebDriverWait(driver, 180).until(EC.element_to_be_clickable((By.ID, "userName"))).clear()

    # driver.find_element_by_id("userName").send_keys(read_conf.login_username)
    WebDriverWait(driver, 180).until(EC.element_to_be_clickable((By.ID, "userName"))).send_keys(read_conf.login_username)

    # driver.find_element_by_id("password").clear()
    WebDriverWait(driver, 180).until(EC.element_to_be_clickable((By.ID, "password"))).clear()

    # driver.find_element_by_id("password").send_keys(read_conf.login_password)
    WebDriverWait(driver, 180).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(
        read_conf.login_password)

    # driver.find_element_by_id("msg1").click()
    WebDriverWait(driver, 180).until(EC.element_to_be_clickable((By.ID, "msg1"))).click()

    WebDriverWait(driver, 180).until(EC.element_to_be_clickable((
        By.XPATH, u'//div[@class="desk"]//span[contains(text(),"PowerView")]'))).click()

    WebDriverWait(driver, 180).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ha-max'))).click()
    driver.switch_to.frame("ifr_appId_5")
    return driver


if __name__ == '__main__':
    get_driver()
