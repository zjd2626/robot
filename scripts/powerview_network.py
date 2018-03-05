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


    def test_createNetwork(self):
        dr = self.driver

        netname = "jingnetwork"
        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()

        targetBar = dr.find_element_by_xpath("//*[@id='mCSB_1_dragger_vertical']/div")
        targetPos = dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'资源配置')]")
        ActionChains(dr).drag_and_drop(targetBar, targetPos).perform()      #拖动滚动条，使私有网络管理在页面可见

        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'私有网络管理')]").click()

        dr.find_element_by_xpath(".//*[@id='add_privateNet']/span").click()

        dr.find_element_by_css_selector('#name').clear()
        dr.find_element_by_css_selector('#name').send_keys(netname)

        dr.find_element_by_css_selector('#netMask').clear()
        dr.find_element_by_css_selector('#netMask').send_keys('255.255.255.0')

        sleep(1)
        physicalNetworkId = dr.find_element_by_xpath("//select[@id='physicalNetworkId']")
        Select(physicalNetworkId).select_by_index(1)
        #Select(physicalNetworkId).select_by_visible_text("1c512M")

        dr.find_element_by_css_selector('#gateway').clear()
        dr.find_element_by_css_selector('#gateway').send_keys('192.168.206.1')

        dr.find_element_by_css_selector('#vlan').clear()
        dr.find_element_by_css_selector('#vlan').send_keys('vlan://206')

        sleep(1)
        networkOfferingId = dr.find_element_by_xpath("//select[@id='networkOfferingId']")
        Select(networkOfferingId).select_by_index(1)

        dr.find_element_by_css_selector('#startIp').clear()
        dr.find_element_by_css_selector('#startIp').send_keys('192.168.206.2')

        dr.find_element_by_css_selector('#endIp').clear()
        dr.find_element_by_css_selector('#endIp').send_keys('192.168.206.200')

        sleep(1)
        dr.find_element_by_css_selector("#submit_but").click()


        sleep(10)


    def test_deleteNetwork(self):
        dr = self.driver

        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()

        targetBar = dr.find_element_by_xpath("//*[@id='mCSB_1_dragger_vertical']/div")
        targetPos = dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'资源配置')]")
        ActionChains(dr).drag_and_drop(targetBar, targetPos).perform()  # 拖动滚动条，使私有网络管理在页面可见

        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'私有网络管理')]").click()

        sleep(2)

 #       all_row = dr.find_elements(By.XPATH, ".//tr[@netid]")
#        rownum = len(all_row)

        dr.find_element_by_xpath(u".//*[@id='content']/div[2]/table/tbody/tr[@displayname='jingnetwork']/td/a[text()='删除']").click()

        sleep(2)
        dr.find_element_by_xpath(u"//div[contains(@style,'display: block;')]//div[@class ='ui-dialog-buttonset']/button[text()='确定']").click()


        '''
        print('rownum: %s' % rownum)
        for row in all_row:
            tbname = row.find_elements_by_tag_name('td')[0].text
            tbstatus = row.find_elements_by_tag_name('td')[1].text
            print("network name: %s, status %s" % (tbname, tbstatus) )
        '''

    def test_searchNetwork(self):
        dr = self.driver

        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()

        targetBar = dr.find_element_by_xpath("//*[@id='mCSB_1_dragger_vertical']/div")
        targetPos = dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'资源配置')]")
        ActionChains(dr).drag_and_drop(targetBar, targetPos).perform()  # 拖动滚动条，使私有网络管理在页面可见

        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'私有网络管理')]").click()

        dr.find_element_by_xpath(".//*[@id='content']/div[2]/div/div[1]/form/div/input").clear()
        dr.find_element_by_xpath(".//*[@id='content']//input[@name='netName']").send_keys("jing")

        dr.find_element_by_xpath(".//*[@id='content']//input[@type='submit']").click()

        all_row = dr.find_elements(By.XPATH, ".//tr[@netid]")
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
