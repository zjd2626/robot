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
from selenium.webdriver.common.action_chains import ActionChains

class vm1():
    @staticmethod
    def create(driver, vmName, cloneNumber, offeringName, templateName, networkName, assginIP):
        page.get_into_powerview(driver, '资源管理', '创建虚拟机')
        creatvm=driver.find_element_by_xpath(".//*[@id='content']/div[2]/div[1]")
        ActionChains(driver).move_to_element(creatvm).move_by_offset(10,10).perform()
        driver.find_element_by_xpath(".//*[@id='createTemplate']").click()
        time.sleep(1)
        driver.find_element_by_id("vmName").clear()
        driver.find_element_by_id("vmName").send_keys(vmName)
        driver.find_element_by_id("cloneNumber").clear()
        driver.find_element_by_id("cloneNumber").send_keys(cloneNumber)
        Select(driver.find_element_by_id("offeringId")).select_by_visible_text(offeringName)
        Select(driver.find_element_by_id("templateId")).select_by_visible_text(templateName)
        Select(driver.find_element_by_id("networkId")).select_by_visible_text(networkName)
        if assginIP is not None:
            driver.find_element_by_id("designIPs").clear()
            driver.find_element_by_id("designIPs").send_keys(assginIP)
        driver.find_element_by_id("create_btn").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

    @staticmethod
    def createVMbyISO(driver, vmName, offeringName, isoName, networkName, assginIP):
       page.get_into_powerview(driver, '资源管理', '创建虚拟机')
       creatvm=driver.find_element_by_xpath(".//*[@id='content']/div[2]/div[2]")
       ActionChains(driver).move_to_element(creatvm).move_by_offset(10,10).perform()
       driver.find_element_by_xpath(".//*[@id='createIso']").click()
       time.sleep(1)
       driver.find_element_by_id("vmName").clear()
       driver.find_element_by_id("vmName").send_keys(vmName)
       Select(driver.find_element_by_id("offeringId")).select_by_visible_text(offeringName)
       Select(driver.find_element_by_id("templateId")).select_by_visible_text(isoName)
       Select(driver.find_element_by_id("networkId")).select_by_visible_text(networkName)
       if assginIP is not None:
           driver.find_element_by_id("designIP").clear()
           driver.find_element_by_id("designIP").send_keys(assginIP)
       driver.find_element_by_id("create_btn").click()
       driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

class PowerviewCreatevm(unittest.TestCase):
    driver = dr.get_driver()

    def setUp(self):
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_powerview_createvm(self):
        driver = self.driver

        vmName = 'cy'
        cloneNumber = 1
        offeringName = '2c2g'
        networkName = 'daas116'
        templateNames = ["daas-win7", "daas-win7share", "daas-win2008"]
        #templateNames = ["daas-win81"]
        for templateName in templateNames:
            vm1.create(driver, vmName+templateName.replace('-',''), cloneNumber, offeringName, templateName, networkName)

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
