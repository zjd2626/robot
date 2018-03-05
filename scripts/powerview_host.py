#!/usr/bin/python
# coding = utf-8
# __author__='yanna.zhuang'

import unittest
import os
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep

libpath = os.path.abspath("../lib")
if libpath not in sys.path:
    sys.path.append(libpath)

from lib import driver as dr


class HostManagement(unittest.TestCase):
    def setUp(self):
        self.driver = dr.get_driver()
        self.verificationErrors = []
        self.accept_next_alert = True

    def enter_menu(self):
        driver = self.driver
        WebDriverWait(driver, 120).until(ec.element_to_be_clickable(
            (By.XPATH, ".//*[@id='mCSB_1_container']//span[contains(text(),'资源管理')]"))).click()
        WebDriverWait(driver, 120).until(ec.element_to_be_clickable(
            (By.XPATH, ".//*[@id='mCSB_1_container']/ul/li/a/span[contains(text(),'主机管理')]"))).click()


    def host_management(self):
        driver = self.driver
        host1 = driver.find_element_by_xpath(".//*[@id='content']/div[4]/table/tbody/tr[1]/td[1]/a").text
        driver.find_element_by_xpath(".//*[@id='content']/div[4]/table/tbody/tr[1]/td[1]/a").click()
        text = WebDriverWait(driver, 60).until(ec.visibility_of_element_located(
            (By.XPATH, ".//*[@id='monitorForm']/div[1]/select/option[@selected='selected']"))).text

        if text == host1:
            print("通过【主机】tab的主机ip跳转到【主机资源监控】页面正确")
        else:
            print("通过【主机】tab的主机ip跳转到【主机资源监控】页面错误")
        sleep(5)

        driver.find_element_by_xpath(".//*[@id='content']/div[3]/ul/li[1]/a[contains(text(),'主机')]").click()
        vm_num = driver.find_element_by_xpath(".//*[@id='content']/div[4]/table/tbody/tr[1]/td[9]/a").text
        driver.find_element_by_xpath(".//*[@id='content']//table/tbody/tr[1]/td[9]/a").click()

        WebDriverWait(driver, 60).until(ec.text_to_be_present_in_element((By.XPATH, ".//*[@id='content']/div[@class='nav-tabs']//a[@class='active']"), "虚拟机"))
        hostip_get = WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, ".//*[@id='content']//input[@class='form-control' and @name='hostIP']"))).get_attribute("value")
        vmnum_get = driver.find_element_by_xpath(".//*[@id='content']/div[4]/table/tbody/tr[21]/th/nav/div/ul[1]/span").text
        if hostip_get == host1 and vmnum_get == vm_num:
            print("通过【主机】tab的虚拟机数量跳转到【虚拟机】页面正确")
        else:
            print("通过【主机】tab的虚拟机数量跳转到【虚拟机】页面错误")
        sleep(5)

        driver.find_element_by_xpath(".//*[@id='content']/div[3]/ul/li[2]/a[contains(text(),'虚拟机')]").click()
        driver.find_element_by_xpath(".//*[@id='content']/div[4]/div/div/form/div[3]/select").send_keys(u"运行")
        driver.find_element_by_xpath(".//*[@id='content']/div[4]/div/div/form/input").click()
        host2 = driver.find_element_by_xpath(".//*[@id='content']/div[4]/table/tbody/tr[1]/td[9]/a").text
        driver.find_element_by_xpath(".//*[@id='content']/div[4]/table/tbody/tr[1]/td[9]/a").click()
        if WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, ".//*[@id='ipAddr']"))).get_attribute("value") == host2:
            print("通过【虚拟机】tab的主机ip跳转到【主机】页面正确")
        else:
            print("通过【虚拟机】tab的主机ip跳转到【主机】页面错误")
        sleep(5)

    def test_host_management(self):
        self.enter_menu()
        self.host_management()

    def is_element_present(self, how, what):
        pass

    def is_alert_present(self):
        pass

    def close_alert_and_get_its_text(self):
        pass

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == '__main__':
    unittest.main()
