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
import sys,os,string,random
from time import sleep

libpath=os.path.abspath("../lib")
if libpath not in sys.path:
    sys.path.append(libpath)
import read_conf

import log
import driver

class Deploy(unittest.TestCase):
    def setUp(self):
        self.driver = driver.get_driver()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_createvm(self):
        dr = self.driver
        vmname = read_conf.vmname
        # WebDriverWait(dr, 120).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='mCSB_1_container']/li[1]"))).click()
        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()
        print('Begin to deploy vm, vmname is ' + vmname)
        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'创建虚拟机')]").click()

        creatvm=dr.find_element_by_xpath(".//*[@id='content']/div[2]/div[1]")

        ActionChains(dr).move_to_element(creatvm).move_by_offset(10,10).perform()
        dr.find_element_by_xpath(".//*[@id='createTemplate']").click()
        sleep(1)

        dr.find_element_by_css_selector('#vmName').clear()
        dr.find_element_by_css_selector('#vmName').send_keys(vmname)

        dr.find_element_by_css_selector("#cloneNumber").clear()
        dr.find_element_by_css_selector("#cloneNumber").send_keys("1")


        # 选择服务套餐
        sleep(1)
        offeringId=dr.find_element_by_xpath("//select[@id='offeringId']")
        Select(offeringId).select_by_visible_text("1c512M")
        # dr.find_element_by_xpath("//select[@id='offeringId']").send_keys("1c512M")

        sleep(1)
        templateId = dr.find_element_by_xpath(".//select[@id='templateId']")
        Select(templateId).select_by_visible_text("daas-win7-i0927")
        # dr.find_element_by_xpath(".//select[@id='templateId']").send_keys("daas-win7-i0927")

        sleep(1)
        networkId=dr.find_element_by_xpath(".//*[@id='networkId']")
        Select(networkId).select_by_visible_text("public127")
        # dr.find_element_by_xpath(".//*[@id='networkId']").send_keys("public127")

        sleep(1)
        dr.find_element_by_css_selector("#create_btn").click()

        sleep(2)
        dr.find_element_by_xpath("/html/body/div[5]/div[3]/div/button").click()

        # expect_remind=u"虚拟机%s创建成功" %vmname
        # print("expect_remind is %s" %expect_remind)
        '''
        for i in range(60):
            remind=dr.find_element_by_xpath(".//*[@class='remind']").text
            print "%d seconds,remind is %s" %(i,remind)
            sleep(1)
            if expect_remind==remind:
                print "deploy vm %s success." %vmname
                break
        '''
        # locator = (By.XPATH,".//*[@class='remind']")
        # try:
        # 	WebDriverWait(dr,60).until(EC.text_to_be_present_in_element(locator,expect_remind))
        # 	print("Deploy vm %s has done." %vmname)
        # except NoSuchElementException as e:
        # 	return False

        sleep(25)


        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'虚拟机管理')]").click()

        all_row=dr.find_elements(By.XPATH,".//*[@name='dataTr']")

        for row in all_row:
            name=row.find_elements_by_tag_name('td')[1].text.split("-")[0]
            status=row.find_elements_by_tag_name('td')[2].text
            print("name is %s,status is %s" %(name,status))
            if name==vmname:
                if status!='失败' and status !='出错':
                    log.logger.info("Deploy vm %s sucess,status %s" %(name,status))
                else:
                    log.logger.info("Deploy vm %s failed,status %s" %(name,status))
                break
        else:
            log.logger.info("Deploy vm failed,not found...")


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
