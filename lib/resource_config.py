# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time,sys,os

if os.path.abspath(".") not in sys.path:
        sys.path.append(os.path.abspath("."))

import common_utils, log


'''资源配置相关操作'''


def into_resource_config(driver):
    """进入资源配置模块
    """

    WebDriverWait(driver, 180).until(EC.element_to_be_clickable((
        By.XPATH, u'//div[@id="mCSB_1_container"]/li/span[contains(text(),"资源管理")]'))).click()
    WebDriverWait(driver, 6).until(EC.visibility_of(driver.find_element(
        by=By.XPATH, value=".//*[@id='mCSB_1_container']//ul//li/a/span[contains(text(),'资源配置')]"))).click()
    time.sleep(3)


def disk_config(driver, lower, upper):
    """云磁盘配置
    """

    log.logger.info("－－－－－－－－开始配置云磁盘－－－－－－－－－－－－－－")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
        By.XPATH, u'.//*[@id="content"]//div/ul/li/a[contains(text(), "云磁盘配置")]'))).click()

    min_input = driver.find_element_by_name('min')
    min_input.clear()
    min_input.send_keys(lower)
    max_input = driver.find_element_by_name('max')
    max_input.clear()
    max_input.send_keys(upper)

    driver.find_element_by_css_selector('input.btn.btn-function').click()
    msg = common_utils.get_confirm_msg(driver, 20,"保存云磁盘配置")
    if u"超时" not in msg:
       driver.find_element_by_xpath(
           u'//div[contains(@style,"display: block;")]//div[@class="ui-dialog-buttonset"]/button[contains(text(),"确定")]').click()
    log.logger.info(msg)

    log.logger.info("－－－－－－－－云磁盘配置结束－－－－－－－－－－－－－－")
        

def platform_quote(driver, vm_amount, disk_amount, host_amount):
    """平台配额
    """

    log.logger.info("－－－－－－－－开始配置平台配额－－－－－－－－－－－－－－")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
        By.XPATH, u'.//*[@id="content"]//div/ul/li/a[contains(text(), "平台配额")]'))).click()

    text_field1 = driver.find_element_by_id("textfield1")
    text_field1.clear()
    text_field1.send_keys(vm_amount)
    text_field2 = driver.find_element_by_id("textfield2")
    text_field2.clear()
    text_field2.send_keys(disk_amount)
    text_field3 = driver.find_element_by_id("textfield3")
    text_field3.clear()
    text_field3.send_keys(host_amount)
    driver.find_element_by_xpath(".//*[@id='saveButton']").click()

    msg = common_utils.get_confirm_msg(driver, 20, "保存平台配置")
    if u"超时" not in msg:
       driver.find_element_by_xpath(
           u'//div[contains(@style,"display: block;")]//div[@class="ui-dialog-buttonset"]/button[contains(text(),"确定")]').click()
    log.logger.info(msg)

    log.logger.info("－－－－－－－－平台配额配置结束－－－－－－－－－－－－－－")


def deskpool_config(driver, max_amount):
    """桌面池配置
    """

    log.logger.info("－－－－－－－－开始配置桌面池配置－－－－－－－－－－－－－－")

    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
        By.XPATH, u'.//*[@id="content"]//div/ul/li/a[contains(text(), "桌面池配置")]'))).click()

    max_user_number = driver.find_element_by_name("maxUserNumber")
    max_user_number.clear()
    max_user_number.send_keys(max_amount)
    driver.find_element_by_css_selector(".btn.btn-function").click()

    msg = common_utils.get_info_msg(driver, 20, "桌面池配置")
    if u"超时" not in msg:
        driver.find_element_by_xpath(
            u'//div[contains(@style,"display: block;")]//div[@class="ui-dialog-buttonset"]/button[contains(text(),"确定")]').click()
    log.logger.info(msg)

    log.logger.info("－－－－－－－－桌面池配置结束－－－－－－－－－－－－－－")

def roam_config(driver, max_size, quota_msg):
    """漫游配置
    """

    log.logger.info("－－－－－－－－开始漫游配置－－－－－－－－－－－－－－")

    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
        By.XPATH, u'.//*[@id="content"]//div/ul/li/a[contains(text(), "漫游配置")]'))).click()

    max_profile_size = driver.find_element_by_id("maxProfileSize")
    max_profile_size.clear()
    max_profile_size.send_keys(max_size)
    profile_quota_message = driver.find_element_by_id("profileQuotaMessage")
    profile_quota_message.clear()
    profile_quota_message.send_keys(quota_msg)
    driver.find_element_by_id("modifyRoamingSetting").click()
    driver.find_element_by_xpath(
        u'//div[contains(@style,"display: block;")]//div[@class="ui-dialog-buttonset"]/button[contains(text(),"确定")]').click()

    msg = common_utils.get_info_msg(driver, 20, "保存漫游配置")
    if u"超时" not in msg:
        driver.find_element_by_xpath(
            u'//div[contains(@style,"display: block;")]//div[@class="ui-dialog-buttonset"]/button[contains(text(),"确定")]').click()
    log.logger.info(msg)

    log.logger.info("－－－－－－－－漫游配置结束－－－－－－－－－－－－－－")