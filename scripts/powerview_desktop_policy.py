#! /usr/bin/python
#coding=utf-8
#__author__='qianfen.zheng'

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import sys, os
if os.path.abspath("../lib") not in sys.path:
        sys.path.append(os.path.abspath("../lib"))

import driver as dr
import desktop_policy



class DesktopPolicy(unittest.TestCase):
    driver = dr.get_driver()
    desktop_policy.into_desktop_policy(driver)
    policy_name = desktop_policy.gen_policy_name('qian')

    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_policy(self):
        driver = self.driver
        desktop_policy.create_policy(driver, self.policy_name, "", 'qiandelivery', (0, 0, 0, 0, 0, 0, 0, 3))

    def test_update_policy(self):
        driver = self.driver
        desktop_policy.update_policy(driver, self.policy_name, "描述", (1, 1, 1, 1, 1, 1, 1, 1))

    def test_delete_policy(self):
        driver = self.driver
        desktop_policy.delete_policy(driver, self.policy_name)

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
