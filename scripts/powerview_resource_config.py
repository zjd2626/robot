#! /usr/bin/python
#coding=utf-8
#__author__='qianfen.zheng'

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import sys, os

if os.path.abspath("../lib") not in sys.path:
        sys.path.append(os.path.abspath("../lib"))
import resource_config
import driver as dr


class RSConfig(unittest.TestCase):
    driver = dr.get_driver()
    resource_config.into_resource_config(driver)

    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_disk_config(self):
        driver = self.driver
        resource_config.disk_config(driver, 20, 1000)

    def test_platform_quote(self):
        driver = self.driver
        resource_config.platform_quote(driver, 50, 50, 50)

    def test_deskpool_config(self):
        driver = self.driver
        resource_config.deskpool_config(driver, 10)

    def test_roam_config(self):
        driver = self.driver
        resource_config.roam_config(driver, 1024, "漫游文件已超过最大上限1G，请将不需要漫游的文件删除，谢谢！")


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
