#!/usr/bin/python
# coding = utf-8
# __author__='Yanna.Zhuang'


import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import strftime, localtime
from time import sleep
import os
import sys
from selenium.webdriver.common.action_chains import ActionChains

libpath = os.path.abspath("../lib")
if libpath not in sys.path:
    sys.path.append(libpath)

from lib import driver as dr


class TemplateManagement(unittest.TestCase):
    """
    TemplateManagement Class provide four function:
    1.create_template(): auto generate a new template name and upload
    2.hide_template(): select the first 'shown template' to be hiden
    3.show_template(): select the first 'hiden template' to be shown
    4.delete_template(template_name): delete the certain template
    """

    def setUp(self):
        self.driver = dr.get_driver()
        self.verificationErrors = []
        self.accept_next_alert = True

    def enter_menu(self):
        driver = self.driver
        WebDriverWait(driver, 120).until(ec.element_to_be_clickable(
            (By.XPATH, ".//*[@id='mCSB_1_container']/li/span[contains(text(),'资源管理')]"))).click()
        WebDriverWait(driver, 120).until(ec.element_to_be_clickable(
            (By.XPATH, ".//*[@id='mCSB_1_container']/ul/li/a/span[contains(text(),'模板管理')]"))).click()

    def create_template(self):
        # 自动生成模板名称
        template_name = "na" + strftime("%Y%m%d%H%M%S", localtime())
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='content']/div[2]//a/span[contains(text(),'创建')]").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(template_name)
        driver.find_element_by_id("description").send_keys("This is QA nana auto test")
        driver.find_element_by_id("osTypeId").send_keys("Other Linux (64-bit)")
        driver.find_element_by_id("osName").send_keys("LINUX")
        driver.find_element_by_id("templateType2").send_keys("模板")
        driver.find_element_by_xpath(".//*[@value='iaas-centos64-h0819.vhd']").click()
        driver.find_element_by_id("submit_but").click()

        # 验证异步任务是否启动成功
        message = WebDriverWait(driver, 120).until(
            ec.visibility_of_element_located((
                By.XPATH, ".//div[contains(@style,'display: block;')]//div[@class='ui-dialog-content ui-widget-content'"
                          "and contains(@style, 'display: block;')]"))).get_attribute("textContent")

        driver.find_element_by_xpath(".//div[contains(@style,'display: block;')]//div/button[contains(text(),'确定')]").click()

        if "成功" in message:
            print("创建模板 %s 异步任务启动成功！" % template_name)
            expect_remind = "模板%s创建成功" % template_name
            unexpected_remind = "模板%s创建失败" % template_name

            # 验证异步任务5分钟内是否完成
            for i in range(300):
                sleep(1)
                remind = driver.find_element_by_xpath(".//*[@class='remind']").text
                if remind == expect_remind:
                    print("第 %d 秒异步消息提示：%s" % (i, remind))
                    break
                elif remind == unexpected_remind:
                    print("第 %d 秒异步消息提示：%s" % (i, remind))
                    break
        return template_name

    def hide_template(self):
        driver = self.driver
        driver.find_element_by_id("templateType").send_keys("模板")
        driver.find_element_by_id("templateState").send_keys("显示")
        driver.find_element_by_xpath(".//*[@id='queryForm']/input").click()
        sleep(3)
        template_name = driver.find_element_by_xpath(".//*[@id='content']//table/tbody/tr[1]/td[1]/a").text.split()[0]
        print("隐藏的模板是：", template_name)
        driver.find_element_by_xpath(".//*[@id='content']/div[2]/table/tbody/tr[1]/td[8]/a[1]").click()
        driver.find_element_by_xpath(".//div[contains(@style,'display: block;')]//div/button[contains(text(),'确定')]").click()
        sleep(5)
        driver.find_element_by_id("templateType").send_keys("模板")
        driver.find_element_by_id("templateState").send_keys("隐藏")
        driver.find_element_by_xpath(".//*[@id='queryForm']/input").click()
        print("验证是否隐藏成功：",)
        driver.find_element_by_xpath("//*[@id='content']//table/tbody/tr[@displayname='%s']" % template_name)
        if driver.find_element_by_xpath("//*[@id='content']//table/tbody/tr[@displayname='%s']" % template_name):
            print("模板 %s 隐藏成功！" % template_name)
        else:
            print("模板 %s 隐藏失败！" % template_name)

    def show_template(self):
        driver = self.driver
        driver.find_element_by_id("templateType").send_keys("模板")
        driver.find_element_by_id("templateState").send_keys("隐藏")
        driver.find_element_by_xpath(".//*[@id='queryForm']/input").click()
        template_name = driver.find_element_by_xpath(".//*[@id='content']//table/tbody/tr[1]/td[1]/a").text.split()[0]
        driver.find_element_by_xpath(".//*[@id='content']/div[2]/table/tbody/tr[1]/td[8]/a[1]").click()
        driver.find_element_by_xpath(".//div[contains(@style,'display: block;')]//div/button[contains(text(),'确定')]").click()
        sleep(5)
        driver.find_element_by_id("templateType").send_keys("模板")
        driver.find_element_by_id("templateState").send_keys("显示")
        driver.find_element_by_xpath(".//*[@id='queryForm']/input").click()
        print("验证是否显示成功:")
        driver.find_element_by_xpath("//*[@id='content']//table/tbody/tr[@displayname='%s']" % template_name)
        if driver.find_element_by_xpath("//*[@id='content']//table/tbody/tr[@displayname='%s']" % template_name):
            print("模板 %s 显示成功！" % template_name)
        else:
            print("模板 %s 显示失败！" % template_name)

    def delete_template(self, template_name):
        driver = self.driver

        try:
            # 删除指定模板
            driver.find_element_by_xpath(".//*[@id='content']/div[2]/table/tbody/tr[@displayname='%s']/td[8]/a[2]" % template_name).click()
            driver.find_element_by_xpath(".//div[contains(@style,'display: block;')]//div/button[contains(text(),'确定')]").click()

        except NoSuchElementException :
            # 拖动滚动条使得前10个模板可见
            scrollbar_source = driver.find_element_by_xpath(
                ".//div[@class='rightframe ']//div[@class='mCSB_dragger']/div")
            scrollbar_target = driver.find_element_by_xpath(".//*[@id='content']//table/tbody/tr[6]")
            # scrollbar_target = driver.find_element_by_xpath(".//*[@id='content']//table/tbody/tr[4]")
            ActionChains(driver).drag_and_drop(scrollbar_source, scrollbar_target).perform()

        # 异步任务启动成功提示文本：
        message = WebDriverWait(driver, 120).until(
            ec.visibility_of_element_located((
                By.XPATH, ".//div[contains(@style,'display: block;')]//div//span[@id='infoMessage']"))).text

        driver.find_element_by_xpath(
            ".//div[contains(@style,'display: block;')]//div/button[contains(text(),'确定')]").click()

        if "成功" in message:
            print("删除模板 %s 异步任务启动成功！" % template_name)
            expect_remind = "模板%s删除成功" % template_name
            unexpected_remind = "模板%s删除失败" % template_name

            # 验证异步任务5分钟内是否完成
            for i in range(300):
                sleep(1)
                remind = driver.find_element_by_xpath(".//*[@class='remind']").text
                if remind == expect_remind:
                    print("第 %d 秒异步消息提示：%s" % (i, remind))
                    break
                elif remind == unexpected_remind:
                    print("第 %d 秒异步消息提示：%s" % (i, remind))
                    break

    def test_template(self):
        self.enter_menu()
        sleep(2)
        print("TestCase1--创建模板：")
        template_name = self.create_template()
        print (template_name)
        sleep(2)
        print("TestCase2--隐藏模板：")
        self.hide_template()
        sleep(2)
        print("TestCase3--显示模板：")
        self.show_template()
        sleep(2)
        print("TestCase4--删除模板：")
        self.delete_template(template_name)
        #self.delete_template("na20180117154304")


    def is_element_present(self, how, what):
        pass

    def is_alert_present(self):
        pass

    def close_alert_and_get_its_text(self):
        pass

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
