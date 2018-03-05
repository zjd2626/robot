#!/usr/local/bin/python
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import unittest
import sys,string,random
from time import sleep

if "/home/clouder/robot/lib" not in sys.path:
    sys.path.append("/home/clouder/robot/lib")
import read_conf

import log
import driver

class NetworkMG(unittest.TestCase):
    def setUp(self):
        self.driver = driver.get_driver()
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_addService(self):
        dr = self.driver

        netname = "jingnetwork"
        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()

        targetBar = dr.find_element_by_xpath("//*[@id='mCSB_1_dragger_vertical']/div")
        targetPos = dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'资源配置')]")
        ActionChains(dr).drag_and_drop(targetBar, targetPos).perform()      #拖动滚动条，使私有网络管理在页面可见

        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'服务套餐')]").click()

        dr.find_element_by_xpath(".//*[@id='dialog-link-offering-add']/span").click()

        dr.find_element_by_xpath(".//*[@id='createOfferingForm']//input[@name='name']").clear()
        dr.find_element_by_xpath(".//*[@id='createOfferingForm']//input[@name='name']").send_keys("jingservice")

        dr.find_element_by_css_selector('#description').clear()
        dr.find_element_by_css_selector('#description').send_keys("this is a test service.")

        storageType = dr.find_element_by_css_selector("#storageType")
        Select(storageType).select_by_index(1)

        sleep(1)
        dr.find_element_by_xpath(".//*[@id='createOfferingForm']//input[@name='cpuSpeed']").clear()
        dr.find_element_by_xpath(".//*[@id='createOfferingForm']//input[@name='cpuSpeed']").send_keys("4098")

        dr.find_element_by_css_selector("#cpuNumber").clear()
        dr.find_element_by_css_selector("#cpuNumber").send_keys(2)

        dr.find_element_by_css_selector("#memory").clear()
        dr.find_element_by_css_selector("#memory").send_keys(2048)

        dr.find_element_by_css_selector("#offerHA").click()


        sleep(1)
        dr.find_element_by_css_selector("#submit_but").click()
        print("addService finished.")


    def test_deleteService(self):
        dr = self.driver

        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()

        targetBar = dr.find_element_by_xpath("//*[@id='mCSB_1_dragger_vertical']/div")
        targetPos = dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'资源配置')]")
        ActionChains(dr).drag_and_drop(targetBar, targetPos).perform()  # 拖动滚动条，使私有网络管理在页面可见

        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'服务套餐')]").click()

        sleep(2)

 #       all_row = dr.find_elements(By.XPATH, ".//tr[@netid]")
#        rownum = len(all_row)

        dr.find_element_by_xpath(".//*[@id='stretch-table']/tbody/tr[@displayname='jingservice']/td/a[text()='删除']").click()

        sleep(2)
        dr.find_element_by_xpath(u"//div[contains(@style,'display: block;')]//div[@class ='ui-dialog-buttonset']/button[text()='确定']").click()



    def test_searchService(self):
        dr = self.driver

        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()

        targetBar = dr.find_element_by_xpath("//*[@id='mCSB_1_dragger_vertical']/div")
        targetPos = dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'资源配置')]")
        ActionChains(dr).drag_and_drop(targetBar, targetPos).perform()  # 拖动滚动条，使私有网络管理在页面可见

        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'服务套餐')]").click()

        dr.find_element_by_xpath(".//*[@id='queryForm']//input[@name='offeringName']").clear()
        dr.find_element_by_xpath(".//*[@id='queryForm']//input[@name='offeringName']").send_keys("jing")

        dr.find_element_by_xpath(".//*[@id='queryForm']/button").click()

        all_row = dr.find_elements(By.XPATH, ".//tr[@offeringid]")
        rownum = len(all_row)
        print("search result: found %s records." % rownum)

    def is_element_present(self, how, what):
        pass
        '''
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
        '''

    def is_alert_present(self):
        pass
        '''
        try: self.driver.switch_to.alert()
        except NoAlertPresentException, e: return False
        return True
        '''

    def close_alert_and_get_its_text(self):
        pass
        '''
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
        '''

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
