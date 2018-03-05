# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

import sys
import os
libpath = os.path.abspath("../lib")
if libpath not in sys.path:
    sys.path.append(libpath)

import constant
import page
import driver as dr
import time

class delivery():

    @staticmethod
    def __search_delivery(driver, deliveryName):
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(deliveryName)
        driver.find_element_by_css_selector("input.btn.btn-function").click()
        time.sleep(1)

    @staticmethod
    def __get_into_delivery_userlist_page(driver, deliveryName):
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(deliveryName)
        driver.find_element_by_css_selector("input.btn.btn-function").click()
        driver.find_element_by_link_text(deliveryName).click()
        driver.find_element_by_id("delivery_user_index").click()
        Select(driver.find_element_by_xpath("(//select[@id='pageSize'])[2]")).select_by_visible_text("100")
        time.sleep(1)

    @staticmethod
    def add(driver, deliveryname, poolname, poolType, userNames):
        page.get_into_powerview(driver, '资源管理', '桌面交付组')
        driver.find_element_by_xpath("//*[@id='react_desk_add']").click()
        time.sleep(1)
        driver.find_element_by_id("inputName").clear()
        driver.find_element_by_id("inputName").send_keys(deliveryname)
        Select(driver.find_element_by_id("desktopPoolIds")).select_by_visible_text(poolname+"("+poolType.value+")")

        for userName in userNames:
            driver.find_element_by_link_text(u"添加").click()
            driver.find_element_by_id("userName").clear()
            driver.find_element_by_id("userName").send_keys(userName)
            driver.find_element_by_xpath(u"//*[@id='popCurrent']//input[@value='查询']").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='user_table_info']//td[text()='"+userName+"']/ancestor::tr[1]//input").click()
            driver.find_element_by_xpath(constant.OKBUTTONPATH).click()

        driver.find_element_by_id("submit_but").click()
        driver.find_element_by_xpath(constant.OKBUTTONPATH).click()

    @staticmethod
    def addusers(driver, deliveryname, userNames):
        page.get_into_powerview(driver, '资源管理', '桌面交付组')
        delivery.__search_delivery(driver, deliveryname)
        driver.find_element_by_link_text(deliveryname).click()
        driver.find_element_by_id("delivery_user_index").click()
        time.sleep(1)

        for userName in userNames:
            driver.find_element_by_link_text(u"添加用户").click()
            driver.find_element_by_id("userName").clear()
            driver.find_element_by_id("userName").send_keys(userName)
            driver.find_element_by_xpath(u"//*[@id='popCurrent']//input[@value='查询']").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='user_table_info']//td[text()='"+userName+"']/ancestor::tr[1]//input").click()
            driver.find_element_by_xpath(constant.OKBUTTONPATH).click()

    @staticmethod
    def removeusers(driver, deliveryname, userNames):
        page.get_into_powerview(driver, '资源管理', '桌面交付组')
        delivery.__search_delivery(driver, deliveryname)
        driver.find_element_by_link_text(deliveryname).click()
        driver.find_element_by_id("delivery_user_index").click()
        time.sleep(1)
        Select(driver.find_element_by_xpath("(//select[@id='pageSize'])[2]")).select_by_visible_text("100")
        time.sleep(1)

        for userName in userNames:
            driver.find_element_by_xpath("//*[@id='userList']//td[text()='"+userName+"']/ancestor::tr[1]//input").click()
            driver.find_element_by_link_text("移除用户").click()
            driver.find_element_by_xpath(constant.OKBUTTONPATH).click()

    @staticmethod
    def disconnectuseronvm(driver, deliveryname, userName):
        page.get_into_powerview(driver, '资源管理', '桌面交付组')
        delivery.__get_into_delivery_userlist_page(driver, deliveryname)
        driver.find_element_by_xpath("//*[@id='userList']//td[text()='"+userName+"']/ancestor::tr[1]//input").click()
        driver.find_element_by_link_text("断开").click()
        driver.find_element_by_xpath(constant.OKBUTTONPATH).click()

    @staticmethod
    def logouttuseronvm(driver, deliveryname, userName):
        page.get_into_powerview(driver, '资源管理', '桌面交付组')
        delivery.__get_into_delivery_userlist_page(driver, deliveryname)
        driver.find_element_by_xpath("//*[@id='userList']//td[text()='"+userName+"']/ancestor::tr[1]//input").click()
        driver.find_element_by_link_text("注销").click()
        driver.find_element_by_xpath(constant.OKBUTTONPATH).click()

    @staticmethod
    def alocatevmtouser(driver, deliveryname, vmName, userName):
        page.get_into_powerview(driver, '资源管理', '桌面交付组')
        delivery.__get_into_delivery_userlist_page(driver, deliveryname)
        driver.find_element_by_xpath("//*[@id='userList']//td[text()='"+userName+"']/ancestor::tr[1]//input").click()
        time.sleep(1)
        driver.find_element_by_link_text("指定分配").click()
        Select(driver.find_element_by_xpath("(//select[@id='pageSize'])[3]")).select_by_visible_text("100")
        driver.find_element_by_xpath("//*[@id='user_table_info']//td[text()='"+vmName+"']/ancestor::tr[1]//input").click()
        driver.find_element_by_xpath(constant.OKBUTTONPATH).click()

    @staticmethod
    def randomalocatevmtouser(driver, deliveryname, userNames):
        page.get_into_powerview(driver, '资源管理', '桌面交付组')
        delivery.__get_into_delivery_userlist_page(driver, deliveryname)
        Select(driver.find_element_by_xpath("(//select[@id='pageSize'])[3]")).select_by_visible_text("100")
        for userName in userNames:
            driver.find_element_by_xpath("//*[@id='userList']//td[text()='"+userName+"']/ancestor::tr[1]//input").click()
        time.sleep(1)
        driver.find_element_by_link_text("随机分配").click()
        driver.find_element_by_xpath(constant.OKBUTTONPATH).click()

    @staticmethod
    def dealocatevm(driver, deliveryname, userName):
        page.get_into_powerview(driver, '资源管理', '桌面交付组')
        delivery.__get_into_delivery_userlist_page(driver, deliveryname)
        driver.find_element_by_xpath("//*[@id='userList']//td[text()='"+userName+"']/ancestor::tr[1]//input").click()
        driver.find_element_by_link_text("解除分配").click()
        driver.find_element_by_xpath(constant.OKBUTTONPATH).click()

    @staticmethod
    def delete(driver, deliveryname):
        page.get_into_powerview(driver, '资源管理', '桌面交付组')
        delivery.__search_delivery(driver, deliveryname)
        driver.find_element_by_xpath(
            u"//*[@id='content']//a[contains(text(),'"+deliveryname+"')]/../..//a[text()='删除']").click()
        driver.find_element_by_xpath(constant.OKBUTTONPATH).click()


class Powerview_delivery(unittest.TestCase):
    driver = dr.get_driver()
    def setUp(self):
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    deliveryName = 'cydelivery1'
    userName = 'cytest1'
    tempuserName = 'cytest3'

    def test_01_powerview_adddesktopdelivery(self):
        driver = self.driver
        delivery.add(driver, self.deliveryName, 'cypool1', constant.poolType.staticOnly, [self.userName])
    
    def test_02_powerview_adduserintodelivery(self):
        driver = self.driver
        delivery.addusers(driver, self.deliveryName, [self.tempuserName])

    def test_03_powerview_alocatevmtouser(self):
        driver = self.driver
        delivery.alocatevmtouser(driver, self.deliveryName, 'wei2c4g-30', self.tempuserName)

    def test_03_powerview_randomalocatevmtouser(self):
        driver = self.driver
        delivery.randomalocatevmtouser(driver, self.deliveryName, [self.userName])

    def test_04_powerview_disconnectuseronvm(self):
        driver = self.driver
        print(self.userName+' get in vm ,like rdesktop -u'+self.tempuserName+'@od.com -pengine 172.28.127.104')
        time.sleep(60)
        delivery.disconnectuseronvm(driver, self.deliveryName, self.tempuserName)

    def test_05_powerview_logouttuseronvm(self):
        driver = self.driver
        print(self.userName+' get in vm ,like rdesktop -u'+self.tempuserName+'@od.com -pengine 172.28.127.104')
        #time.sleep(60)
        delivery.logouttuseronvm(driver, self.deliveryName, self.tempuserName)

    def test_06_powerview_dealocatevm(self):
        driver = self.driver
        delivery.dealocatevm(driver, self.deliveryName, self.tempuserName)

    def test_07_powerview_removeuserfromdelivery(self):
        driver = self.driver
        delivery.removeusers(driver, self.deliveryName, [self.tempuserName])

    def test_08_powerview_deletedelivery(self):
        driver = self.driver
        delivery.delete(driver, self.deliveryName)

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

    suite = unittest.TestSuite()
    #suite.addTest(Powerview_delivery("test_01_powerview_adddesktopdelivery"))
    #suite.addTest(Powerview_delivery("test_03_powerview_alocatevmtouser"))
    #suite.addTest(Powerview_delivery("test_02_powerview_adduserintodelivery"))
    #suite.addTest(Powerview_delivery("test_03_powerview_alocatevmtouser"))
    #suite.addTest(Powerview_delivery("test_03_powerview_randomalocatevmtouser"))

    #suite.addTest(Powerview_delivery("test_04_powerview_disconnectuseronvm"))
    #suite.addTest(Powerview_delivery("test_05_powerview_logouttuseronvm"))
    #suite.addTest(Powerview_delivery("test_06_powerview_dealocatevm"))
    #suite.addTest(Powerview_delivery("test_07_powerview_removeuserfromdelivery"))
    #suite.addTest(Powerview_delivery("test_08_powerview_deletedelivery"))
    #runner = unittest.TextTestRunner()
    runner.run(suite)

