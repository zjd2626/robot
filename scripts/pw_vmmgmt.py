#!/usr/bin/env python
#coding=utf-8
#__author__='weixiang.wang'

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *
import unittest
import time,sys
import requests


if "/home/clouder/robot/lib" not in sys.path:
    sys.path.append("/home/clouder/robot/lib")

import driver
import read_conf
# dr=driver.get_driver()

OK_BUTTON="//div[contains(@style,'display:block;') or contains(@style, 'display: block')]//button[contains(text(),'确定')]"

class vmm():

    # self.vmstatus = driver.find_element_by_xpath(
    #         "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName).text
    # vmstatus = driver.find_element_by_xpath(
    #     "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName).text
    # def get_vmStatus(self,driver, vmName):
    #     vmstatus = driver.find_element_by_xpath(
    #         "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName).text
    #     return vmstatus

    def entry_to_vmm(driver):
        time.sleep(3)
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
            (By.XPATH, u'//*[@id="mCSB_1_container"]/li//span[contains(text(),"资源管理")]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]'))).click()


    def select_vm(driver, vmName):
        # print (vmName)
        # # number=vmName.split('-')[1]
        # # vmName = vmName + '-1'
        # print("vmName with number", vmName)
        # WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        #     (By.XPATH, u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]'))).click()
        time.sleep(5)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[1]/input" % vmName))).click()

    def entry_select_vm(driver, vmName):
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
            (By.XPATH, u'//*[@id="mCSB_1_container"]/li//span[contains(text(),"资源管理")]'))).click()
        time.sleep(5)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]'))).click()
        time.sleep(15)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[1]/input" % vmName))).click()



        # if driver.find_element_by_xpath(
        #                 "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[1]/input" % vmName).is_selected():
        #     print('vm is selected!')
        # else:
        #     print('vm not selected!')
        # status = driver.find_element_by_xpath(
        #     "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName).text
        # print("status", status)
        # return vmName, status


    def stop_vm(driver, vmName):
        # vmStatus=is_present_vm(driver,vmName)
        # result = select_vm(driver, vmName)
        # vmStatus = result[1]
        # if vmStatus == u'运行':
        #     driver.find_element_by_xpath('//*[@id="operations"]/a[2]').click()
        #     WebDriverWait(driver, 40).until(
        #         EC.element_to_be_clickable((By.XPATH, u"html/body/div[5]/div[3]/div/button[1]"))).click()
        #     time.sleep(20)
        #     vmStatus2 = is_present_vm(driver, vmName)
        #     if vmStatus2 == u'停止':
        #         print("stop vm sucess")
        # WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        #     (By.XPATH, u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]'))).click()

        # time.sleep(5)
        # # driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]').click()
        # # time.sleep(5)
        # # WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        # #     (By.XPATH, "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[1]/input" % vmName))).click()
        # WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        #     (By.XPATH, u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]'))).click()

        time.sleep(5)
        status = driver.find_element_by_xpath(
            "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName).text
        # if status == '停止':
        #     self.start_vm(driver,vmName)
        #     status = driver.find_element_by_xpath("//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName).text
        # status=self.get_vmStatus(driver, vmName)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[1]/input" % vmName))).click()
        if status == '运行':
            print ("start to stop vm")
            driver.find_element_by_xpath('//*[@id="operations"]/a[2]').click()

            driver.find_element_by_xpath(OK_BUTTON).click()
            time.sleep(30)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]'))).click()
            vmstatus = driver.find_element_by_xpath(
                "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName).text
            if vmstatus == u'停止':
                print("stop vm sucess")



    def start_vm(driver, vmName):
        # vmStatus=is_present_vm(driver,vmName)
        # result = select_vm(driver, vmName)
        # vmStatus = result[1]
        # if vmStatus == u'停止':
        #     driver.find_element_by_xpath('//*[@id="operations"]/a[1]').click()
        #     WebDriverWait(driver, 40).until(
        #         EC.element_to_be_clickable((By.XPATH, u"html/body/div[5]/div[3]/div/button[1]"))).click()
        #     time.sleep(20)
        #     vmStatus2 = is_present_vm(driver, vmName)
        #     if vmStatus2 == u'运行':
        #         print("start vm sucess")

        status = driver.find_element_by_xpath(
            "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName).text
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[1]/input" % vmName))).click()
        # if status == '运行':
        #     self.stop_vm(driver,vmName)
        #     status = driver.find_element_by_xpath(
        #         "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName).text
        if status == '停止':
            print ("start to start vm")
            driver.find_element_by_xpath('//*[@id="operations"]/a[1]').click()
            driver.find_element_by_xpath(OK_BUTTON).click()
            time.sleep(30)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]'))).click()
            time.sleep(10)
            vmstatus = driver.find_element_by_xpath(
                "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName).text
            if vmstatus == u'运行':
                print("start vm sucess")


    def restart_vm(driver, vmName):
        # vmStatus=is_present_vm(driver,vmName)
        # result = select_vm(driver, vmName)
        # vmStatus = result[1]
        status = driver.find_element_by_xpath(
            "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName).text
        if status == '运行':
            print("start to restart vm")
            driver.find_element_by_xpath('//*[@id="operations"]/a[3]').click()
            time.sleep(2)
            driver.find_element_by_xpath(OK_BUTTON).click()

            time.sleep(35)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]'))).click()
            time.sleep(10)
            vmstatus = driver.find_element_by_xpath(
                "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName).text
            if vmstatus == u'运行':
                print("restart vm sucess")


    def delete_vm(driver, vmName):
        # result = select_vm(driver, vmName)
        # vmName = result[0]
        driver.find_element_by_xpath("//*[@id='operations']/a[5]/span").click()
        WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, u"html/body/div[5]/div[3]/div/button[1]"))).click()
        try:
            WebDriverWait(driver, 40).until(EC.invisibility_of_element_located(
                (By.XPATH, "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[1]/input" % vmName)))
            print("delete vmname '%s' success", vmName)
        except TimeoutException:
            print("delete vmname '%s' failed", vmName)

    def isstop_vm(driver, vmName):
        # vmStatus=is_present_vm(driver,vmName)
        result = select_vm(driver, vmName)
        vmStatus = result[1]
        if vmStatus == u'停止':
            pass
        elif vmStatus == u'运行':
            stop_vm(driver, vmName)

    def isstart_vm(driver, vmName):
        # vmStatus=is_present_vm(driver,vmName)
        result = select_vm(driver, vmName)
        vmStatus = result[1]
        if vmStatus == u'运行':
            pass
        elif vmStatus == u'停止':
            start_vm(driver, vmName)


    def enter_clouddiskmanage(driver, vmName):
        # result = select_vm(driver, vmName)
        # vmName = result[0]
        WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH,
                                        u"//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[10]/a[contains(text(),'查看云磁盘')]" % vmName))).click()
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, u"//*[@id='cloudDiskForm']/div[2]/input[@value='%s']" % vmName)))
            print("check clouddisk success")
        except TimeoutException:
            print("check clouddisk failed")

    def templaname_gen():
        return "testqa" + time.strftime("%H%M%S")

    def copy_to_templet(driver, vmName):
        # # result=select_vm(driver,vmName)
        # isstop_vm(driver, vmName)
        # # # vmName=result[0]
        # templa_name = templaname_gen()
        # self.select_vm(driver, vmName)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]'))).click()
        time.sleep(10)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[1]/input" % vmName))).click()

        templa_name = "testqa" + time.strftime("%H%M%S")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='operations']/a/span[contains(text(),'复制为模板')]").click()
        driver.find_element_by_xpath("//*[@id='copy_as_template_form']/div/div/input[@name='name']").send_keys(templa_name)
        driver.find_element_by_xpath("//*[@id='copy_as_template_form']/div/div/textarea").send_keys(templa_name)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='submit_but']").click()

        info = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, u"//*[@id='infoMessage']"))).text
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, u"html/body//div[contains(@style,'display: block;')]/div/button"))).click()
        if info.__contains__("复制为模板任务启动成功!"):
            print("复制为模板任务启动成功")
        else:
            print("复制为模板任务启动failed")

    def vnc_view(driver, vmName):
        # isstart_vm(driver, vmName)
        # vmName = vmName + '-1'
        # self.select_vm(driver, vmName)
        vnclink = driver.find_element_by_xpath(
            "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[10]/a[contains(text(),'VNC访问')]" % vmName)
        url = vnclink.get_attribute('href')
        print(url)
        r = requests.get(url, allow_redirects=False)
        print(r.status_code)
        if r.status_code == 200:
            print("vnc 访问成功")
        else:
            print("vnc 访问失败")




class pw_vmmage(unittest.TestCase):
    dr=driver.get_driver()
    def setUp(self,driver=dr):
        # self.driver = driver.get_driver()
        self.driver=driver
        self.base_url = read_conf.login_url
        self.verificationErrors = []
        self.accept_next_alert = True

    # vmName = 'gjzvm11062'

    def test_01_operatevm(self):
        driver=self.driver
        # time.sleep(10)
        # vmm.entry_to_vmm(driver)
        # vmm.select_vm(driver,vmName)
        # # vmm.vnc_view(driver, self.vmName)
    #     # vmm.select_vm(driver,vmName)
    #     # vmm.entry_select_vm(driver,vmName)
    #     # vmm.vnc_view(driver,vmName)
        vmm.entry_select_vm(driver,vmName)
        vmm.restart_vm(driver,vmName)
    #     # vmm.select_vm(driver, vmName)
    #     # vmm.stop_vm(driver,vmName)
    #     # vmm.select_vm(driver,vmName)
    #     # vmm.copy_to_templet(driver,vmName)
    #
    #     # vmm.enter_clouddiskmanage(driver,vmName)
    #     # vmm.delete_vm(driver,vmName)
    # # def test_02_viewvnc(self):
    # #     driver = self.driver
    # #     time.sleep(5)
    # #     vmm.select_vm(driver, vmName)
    # #     vmm.vnc_view(driver, vmName)
    #
    # #
    def test_02_stopvm(self):
        print("start to stop")
        driver=self.driver
        time.sleep(5)
        # vmm.select_vm(driver, vmName)
        vmm.stop_vm(driver,vmName)

    def test_03_cpvmt(self):
        print("start to copy to template")
        driver=self.driver
        time.sleep(5)
        # vmm.select_vm(driver, vmName)
        vmm.copy_to_templet(driver, vmName)

    def test_04_startvm(self):
        print("start to start")
        driver=self.driver
        time.sleep(5)
        # vmm.select_vm(driver, vmName)
        vmm.start_vm(driver,vmName)

    def test_05_viewvnc(self):
        print("start to test vnc view")
        driver = self.driver
        time.sleep(5)
        # vmm.select_vm(driver, vmName)
        vmm.vnc_view(driver, vmName)


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    Name = 'testtt'
    vmName = Name + '-1'
    print (vmName)
    unittest.main()



