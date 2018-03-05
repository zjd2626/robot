# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

import sys, os
libpath = os.path.abspath("../lib")
if libpath not in sys.path:
    sys.path.append(libpath)

import constant
import page
import driver as dr
import time

class pool():

    @staticmethod
    def __search_pool(driver, poolName):
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(poolName)
        driver.find_element_by_xpath("//form[@id='queryForm']//button[contains(text(),'查询')]").click()
        time.sleep(1)

    @staticmethod
    def add(driver, poolName, networkName, poolType2, vmNames):
        page.get_into_powerview(driver, '资源管理', '桌面池管理')
        driver.find_element_by_xpath("//a[@id='dialog-link-desktop-pool-add']").click()
        driver.find_element_by_id("desktoppoolName").clear()
        driver.find_element_by_id("desktoppoolName").send_keys(poolName)
        Select(driver.find_element_by_id("netWorkId")).select_by_visible_text(networkName)
        driver.find_element_by_xpath("//*[@id='createDesktopPoolForm']//label[text()='"+poolType2.value+"']/preceding-sibling::input[1]").click()

        for vmName in vmNames:
            driver.find_element_by_name("addVmBtnJS").click()
            driver.find_element_by_name("vmName").clear()
            driver.find_element_by_name("vmName").send_keys(vmName)
            driver.find_element_by_xpath("//*[@id='noDesktop']//button[contains(text(),'查询')]").click()
            time.sleep(1)
            driver.find_element_by_xpath("//span[contains(text(),'添加虚拟机')]/../..//span[@title='"+vmName+"']/ancestor::tr[1]//input").click()
            driver.find_element_by_xpath("//span[contains(text(),'添加虚拟机')]/../..//button[text()='确定']").click()

        driver.find_element_by_xpath("//span[contains(text(),'创建桌面池')]/../..//button[text()='确定']").click()
        #self.assertTrue(self.is_element_present(By.XPATH, "//span[@id='infoMessage' and contains(text(),'成功')]"))
        driver.find_element_by_xpath("//span[@id='infoMessage']/../../..//button[text()='确定']").click()

    @staticmethod
    def addvm(driver, poolName, vmName):
        page.get_into_powerview(driver, '资源管理', '桌面池管理')
        pool.__search_pool(driver, poolName)
        driver.find_element_by_link_text(poolName).click()
        time.sleep(1)
        driver.find_element_by_link_text("虚拟机").click()
        driver.find_element_by_name("addVmBtnJava").click()
        driver.find_element_by_name("vmName").clear()
        driver.find_element_by_name("vmName").send_keys(vmName)
        driver.find_element_by_xpath(constant.QUERYBUTTONPATH).click()
        driver.find_element_by_xpath(
            "//span[contains(text(),'添加虚拟机')]/../..//span[@title='" + vmName + "']/ancestor::tr[1]//input").click()
        driver.find_element_by_xpath(constant.OKBUTTONPATH).click()

    @staticmethod
    def removevm(driver, poolName, vmName):
        page.get_into_powerview(driver, '资源管理', '桌面池管理')
        pool.__search_pool(driver, poolName)
        driver.find_element_by_link_text(poolName).click()
        time.sleep(1)
        driver.find_element_by_link_text("虚拟机").click()
        driver.find_element_by_xpath("//table[@id='vmList']//td[text()='"+vmName+"']/ancestor::tr[1]//input").click()
        driver.find_element_by_name("delVmBtn").click()
        driver.find_element_by_xpath(constant.OKBUTTONPATH).click()

    @staticmethod
    def delete(driver, poolName):
        page.get_into_powerview(driver, '资源管理', '桌面池管理')
        pool.__search_pool(driver, poolName)
        driver.find_element_by_xpath(
            "//table[@id='stretch-table']//a[text()='"+poolName+"']/ancestor::tr[1]//a[text()='删除']").click()
        driver.find_element_by_xpath(constant.OKBUTTONPATH).click()


class Powerview_pool(unittest.TestCase):

    driver = dr.get_driver()

    def setUp(self):
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    poolName = 'cypool1'
    tempvmName = 'wx2c2g-1'

    def test_01_powerview_adddesktoppool(self):
        driver = self.driver
        pool.add(driver, self.poolName, 'daas116', constant.poolType2.staticOnly, ['wx2c2g-10'])

    def test_02_powerview_addvmintopool(self):
        driver = self.driver
        pool.addvm(driver, self.poolName, self.tempvmName)

    def test_03_powerview_removevmfromdesktop(self):
        driver = self.driver
        pool.removevm(driver, self.poolName, self.tempvmName)

    def test_04_powerview_deletedesktoppool(self):
        driver = self.driver
        pool.delete(driver, self.poolName)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
