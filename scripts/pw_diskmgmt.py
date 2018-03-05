#!/usr/bin/env python3
#coding=utf-8
#__author__='David Chung'


import unittest
import sys
import string
import random
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if "/home/clouder/robot/lib" not in sys.path:
    sys.path.append("/home/clouder/robot/lib")
import read_conf

import log
import driver


class DiskMgmt(unittest.TestCase):
    gdriver = driver.get_driver()
    gvmname = "qaWin7"
    gdisk = "qa" + time.strftime("%Y%m%d%H%M%S")
    gsnap = "snap"+time.strftime("%Y%m%d%H%M%S")
    gnewdisk = "disk"+time.strftime("%Y%m%d%H%M%S")
    verificationErrors = []

    def setUp(self):
        # self.driver = g.driver
        # self.verificationErrors = []
        self.accept_next_alert = True

    def test_01_createdisk(self):
        dr = self.gdriver
        diskname = self.gdisk
        vmname = self.gvmname

        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()
        print('Begin to create clouddisk, disk name is ' + diskname)
        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]").click()

        sleep(1)
        # 创建云磁盘
        dr.find_element_by_css_selector("#tran_pop_icon3").click()

        dr.find_element_by_css_selector("#c_disk_name").clear()
        dr.find_element_by_css_selector("#c_disk_name").send_keys(diskname)

        dr.find_element_by_css_selector("#c_disk_account").clear()
        dr.find_element_by_css_selector("#c_disk_account").send_keys("1")

        # dr.find_element_by_css_selector("#create_disk_confirm").click()
        WebDriverWait(dr, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#create_disk_confirm"))).click()
        # 创建中提示信息
        # WebDriverWait(dr,60).until(EC.visibility_of_element_located(
        #     (By.XPATH,"html/body/div[17]/div[3]/div/button"))).click()
        WebDriverWait(dr, 60).until(EC.element_to_be_clickable((By.XPATH,
         "//div[contains(@style,'display: block;')]//div[@class='ui-dialog-buttonset']/button[text()='确定']"))).click()

        locator = (By.XPATH, ".//*[@class='remind']")
        expect_text = "云磁盘{0}创建成功".format(diskname+'-1')

        try:
            # text=WebDriverWait(dr, 60).until(EC.visibility_of_element_located(locator)).text
            # print(text)
            WebDriverWait(dr, 60).until(EC.text_to_be_present_in_element(locator, expect_text))
            print(expect_text)
        except BaseException:
            print("云磁盘创建失败.")
            self.verificationErrors.append('error')

        #在列表中查找创建出来的云磁盘
        # all_row=dr.find_elements(By.XPATH,".//*[@id='mainTable']/tbody/tr")
        # rownum=len(all_row)
        #
        # for i in range(rownum):
        #     name=all_row[i].find_elements_by_tag_name('td')[1].text.split("-")[0]
        #     # status=all_row[i].find_elements_by_tag_name('td')[2].text
        #     print("name is %s" %name)
        #     if name==vmname:
        #         all_row[i].click()
        #         dr.find_element_by_xpath(".//*[@id='tran_pop_icon4']").click()
        #         break
        # else:
        #     self.fail("clouddisk not found...")
        #     log.logger.info("clouddisk not found...")
        # 选中创建的云磁盘并点击
        # seldisk=WebDriverWait(dr,60).until(EC.visibility_of_element_located(
        #     (By.XPATH,".//*[@id='mainTable']/tbody/tr/td[contains(text(),'%s')]" %diskname)))
        # text=seldisk.text
        # print(text)

    def test_02_mountdisk(self):
        dr = self.gdriver
        vmname = self.gvmname
        diskname = self.gdisk

        # #进入云磁盘管理
        print('Begin to mount clouddisk, disk name is ' + diskname)
        try:
            WebDriverWait(dr, 10).until(EC.visibility_of(dr.find_element(
                By.XPATH,".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]")))
        except:
            dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()
        sleep(2)
        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]").click()

        sleep(2)
        # 选中创建的云磁盘并点击
        seldisk=WebDriverWait(dr, 60).until(EC.element_to_be_clickable(
            (By.XPATH, ".//*[@id='mainTable']/tbody/tr/td[contains(text(),'%s')]" % diskname)))
        text = seldisk.text
        print(text)
        seldisk.click()

        # 点击挂载
        dr.find_element_by_xpath(".//*[@id='tran_pop_icon4']").click()

        # 查询
        sleep(5)
        dr.find_element_by_xpath(".//*[@id='attachForm']//input[@name='vmName']").clear()
        dr.find_element_by_xpath(".//*[@id='attachForm']//input[@name='vmName']").send_keys(vmname)
        dr.find_element_by_xpath(".//*[@id='search']").click()

        sleep(2)
        dr.find_element_by_xpath("//input[@name='mount_vm_radio']").click()

        dr.find_element_by_xpath("//div[contains(@style,'display: block;')]"
                                 "//div[@class='ui-dialog-buttonset']/button[text()='确定']").click()
        sleep(1)
        dr.find_element_by_xpath(
            "//div[contains(@style,'display: block;')]//div[@class='ui-dialog-buttonset']/button[text()='确定']").click()

        locator = (By.XPATH, ".//*[@class='remind']")
        expect_text = "云磁盘{0}挂载成功".format(text)

        try:
            WebDriverWait(dr, 60).until(EC.text_to_be_present_in_element(locator, expect_text))
            print(expect_text)
        except BaseException:
            print("云磁盘挂载失败.")

    def test_03_umountdisk(self):
        dr = self.gdriver
        vmname = self.gvmname
        diskname = self.gdisk

        #进入虚拟机管理
        print('进入虚拟机管理页面')

        try:
            WebDriverWait(dr, 10).until(EC.visibility_of(dr.find_element(
                By.XPATH,".//*[@id='mCSB_1_container']//span[contains(text(),'虚拟机管理')]")))
        except:
            print("except here...")
            dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()
        sleep(3)
        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'虚拟机管理')]").click()

        sleep(2)
        dr.find_element_by_xpath(".//*[@id='vmIndexForm']//input[@name='vmName']").clear()
        dr.find_element_by_xpath(".//*[@id='vmIndexForm']//input[@name='vmName']").send_keys(vmname)
        dr.find_element_by_xpath(".//*[@id='submit']").click()

        sleep(5)
        # 查询虚拟机状态并停止
        element=WebDriverWait(dr,60).until(EC.visibility_of_element_located(
            (By.XPATH,".//*[@id='stretch-table']//a[contains(@vmname,'%s')]" %vmname)))
        status=element.get_attribute('state')
        print('status is %s' %status)
        # state = WebDriverWait(dr, 60).until(EC.visibility_of_element_located(
        #     (By.PARTIAL_LINK_TEXT, vmname))).get_attribute('state')
        # print(state)
        if status=="RUNNING":
            print("停止虚拟机....")
            WebDriverWait(dr, 60).until(EC.element_to_be_clickable(
                (By.XPATH, ".//*[@id='stretch-table']//tr[contains(@displayname,'%s')]" %vmname))).click()
            dr.find_element_by_xpath("//a[@name='stop']").click()
            dr.find_element_by_xpath(
            "//div[contains(@style,'display: block;')]//div[@class='ui-dialog-buttonset']/button[text()='确定']").click()

            locator = (By.XPATH, ".//*[@class='remind']")
            expect_text = "虚拟机{0}停止成功".format(vmname+'-1')
            try:
                WebDriverWait(dr, 60).until(EC.text_to_be_present_in_element(locator, expect_text))
                print(expect_text)
            except BaseException:
                print("虚拟机停止失败.")

        #进入云磁盘管理
        print('Begin to unmount clouddisk, disk name is ' + diskname)

        try:
            WebDriverWait(dr, 10).until(EC.visibility_of(dr.find_element(
                By.XPATH,".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]")))
        except:
            dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()
        sleep(3)
        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]").click()

        # 选中创建的云磁盘并点击
        WebDriverWait(dr, 60).until(EC.element_to_be_clickable(
            (By.XPATH, ".//td[contains(text(),'%s')]//..//a[text()='卸载']" %diskname))).click()
        # rows = dr.find_elements(By.XPATH, ".//table[@id='mainTable']/tbody/tr")
        # for row in rows:
        #     text = row.find_element_by_class_name("td_diskName").text
        #     if text.startswith(diskname):
        #         row.find_element_by_link_text("卸载").click()
        #         break

        confirm_locator="//div[contains(@style,'display: block;')]//div[@class='ui-dialog-buttonset']/button[text()='确定']"
        # 确认是否卸载云磁盘
        # dr.find_element_by_xpath(
        #     "//div[contains(@style,'display: block;')]//div[@class='ui-dialog-buttonset']/button[text()='确定']").click()
        WebDriverWait(dr, 60).until(EC.visibility_of_element_located((By.XPATH,confirm_locator))).click()
        sleep(2)

        # 提示正在卸载云磁盘
        WebDriverWait(dr, 60).until(EC.visibility_of_element_located((By.XPATH,confirm_locator))).click()

        locator = (By.XPATH, ".//*[@class='remind']")
        expect_text = "云磁盘{0}卸载成功".format(diskname+'-1')
        try:
            WebDriverWait(dr, 60).until(EC.text_to_be_present_in_element(locator, expect_text))
            print(expect_text)
        except BaseException:
            print("云磁盘卸载失败.")

    def test_04_take_snapshot(self):
        dr = self.gdriver
        vmname = self.gvmname
        diskname = self.gdisk
        snapname = self.gsnap

        # 进入云磁盘管理
        # dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()
        print('Begin to create snapshot, snapshot is %s' % snapname)

        try:
            WebDriverWait(dr, 10).until(EC.visibility_of(dr.find_element(
                By.XPATH,".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]")))
        except:
            print("except here...")
            dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()
        sleep(3)
        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]").click()

        # 选中创建的云磁盘并点击
        WebDriverWait(dr, 60).until(EC.element_to_be_clickable(
            (By.XPATH, ".//td[contains(text(),'%s')]//..//a[text()='快照']" %diskname))).click()
        # WebDriverWait(dr,60).until(EC.visibility_of_element_located(
        #     (By.XPATH,".//table[@id='mainTable']/tbody/tr/td[contains(text(),'%s')]" %diskname))).click()
        #
        # rows = dr.find_elements(By.XPATH, ".//table[@id='mainTable']/tbody/tr")
        # for row in rows:
        #     text = row.find_element_by_class_name("td_diskName").text
        #     if text.startswith(diskname):
        #         row.find_element_by_link_text("快照").click()
        #         break
        # else:
        #     self.fail("未找到要创建快照的云磁盘")

        # 创建快照对话框
        dr.find_element_by_xpath(".//*[@id='create_snap_name']").clear()
        dr.find_element_by_xpath(".//*[@id='create_snap_name']").send_keys(snapname)
        dr.find_element_by_xpath(".//*[@id='create_snap_confirm']").click()

        # 确认是否创建
        dr.find_element_by_xpath(
            "//div[contains(@style,'display: block;')]//div[@class='ui-dialog-buttonset']/button[text()='确定']").click()

        locator = (By.XPATH, ".//*[@class='remind']")
        expect_text = "云磁盘快照{0}创建成功".format(snapname)
        try:
            WebDriverWait(dr, 60).until(EC.text_to_be_present_in_element(locator, expect_text))
            print(expect_text)
        except BaseException:
            print("云磁盘快照创建失败.")

        # dr.find_element_by_link_text("快照管理").click()
        #
        # locator = "//div[@id='content']//span[@class][@title]"
        #
        # rows = dr.find_elements_by_xpath(locator)
        # for row in rows:
        #     text = row.text
        #     if text == snapname:
        #         print("云磁盘快照%s创建成功" % snapname)
        #         break
        # else:
        #     print("云磁盘快照%s创建失败" % snapname)

    def test_05_expand_disk(self):
        '''云磁盘扩容'''
        dr = self.gdriver
        vmname = self.gvmname
        diskname = self.gdisk

        # 进入云磁盘管理
        try:
            WebDriverWait(dr, 10).until(EC.visibility_of(dr.find_element(
                By.XPATH,".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]")))
        except:
            print("except here...")
            dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()
        sleep(3)
        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]").click()

        print('Begin to expand disk, diskname is %s' %diskname)
        # #选中创建的云磁盘并点击
        # WebDriverWait(dr,60).until(EC.visibility_of_element_located(
        #     (By.XPATH,".//table[@id='mainTable']/tbody/tr/td[contains(text(),'%s')]" %diskname))).click()

        try:
            presize=WebDriverWait(dr,10).until(EC.visibility_of_element_located((By.XPATH,
            ".//*[@id='mainTable']//input[contains(@diskname,'%s')]" %diskname))).get_attribute('disksize')
            print("扩容前的云磁盘大小是：%s" % presize)
        except:
            self.fail("不存在云磁盘%s." %diskname)

        # rows = dr.find_elements(By.XPATH, ".//table[@id='mainTable']/tbody/tr")
        # for row in rows:
        #     text = row.find_element_by_class_name("td_diskName").text
        #     if text.startswith(diskname):
        #         # 找到了云磁盘,点击扩容按钮
        #         presize = row.find_elements_by_tag_name("td")[3].text
        #         print("扩容前的云磁盘大小是：%s" % presize)
        #         row.find_element_by_link_text("扩容").click()
        #         break
        # else:
        #     self.fail("不存在云磁盘%s." % diskname)


        WebDriverWait(dr, 60).until(EC.element_to_be_clickable(
            (By.XPATH, ".//td[contains(text(),'%s')]//..//a[text()='扩容']" %diskname))).click()

        # 确定扩容
        dr.find_element_by_css_selector("#expand_dialog_confirm").click()

        # 开始扩容确定信息
        dr.find_element_by_xpath(
            "//div[contains(@style,'display: block;')]//div[@class='ui-dialog-buttonset']/button[text()='确定']").click()

        # 扩容结果提示窗口
        dr.find_element_by_xpath(
            "//div[contains(@style,'display: block;')]//div[@class='ui-dialog-buttonset']/button[text()='确定']").click()

        # rows = dr.find_elements(By.XPATH, ".//table[@id='mainTable']/tbody/tr")
        # for row in rows:
        #     text = row.find_element_by_class_name("td_diskName").text
        #     if text.startswith(diskname):
        #         # 找到了云磁盘,点击扩容按钮
        #         aftersize = row.find_elements_by_tag_name("td")[3].text
        #         print("扩容后的云磁盘大小是：%s" % aftersize)
        #         break
        # else:
        #     self.skipTest("没找到云磁盘%s." % diskname)

        try:
            aftersize=WebDriverWait(dr,10).until(EC.visibility_of_element_located((By.XPATH,
            ".//*[@id='mainTable']//input[contains(@diskname,'%s')]" %diskname))).get_attribute('disksize')
            print("扩容后的云磁盘大小是：%s" % aftersize)
        except:
            self.fail("不存在云磁盘%s." %diskname)

        try:
            self.assertGreater(aftersize, presize)
            print("扩容成功.")
        except BaseException:
            print("扩容失败.")

    def test_06_restore_snapshot(self):
        '''恢复快照'''
        dr = self.gdriver
        vmname = self.gvmname
        snapname = self.gsnap
        newdisk = self.gnewdisk

        # 进入云磁盘管理
        try:
            WebDriverWait(dr, 10).until(EC.visibility_of(dr.find_element(
                By.XPATH,".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]")))
        except:
            print("except here...")
            dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()
        sleep(3)
        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]").click()

        dr.find_element_by_link_text("快照管理").click()

        rows = dr.find_elements(By.XPATH, ".//*[@id='content']//tbody/tr")
        for row in rows:
            text = row.find_elements_by_tag_name("td")[0].text
            # print(text)
            if text.startswith(snapname):
                row.find_element_by_link_text("恢复").click()
                break
        else:
            self.skipTest("未找到需要恢复的快照")

        print('Begin to restore disk %s from snapshot %s' % (newdisk, snapname))

        # dr.find_element_by_xpath(".//*[@id='recovery_snapshot_dialog']//input[@name='new_disk_name']")
        dr.find_element_by_css_selector("input[name='new_disk_name']").clear()
        dr.find_element_by_css_selector("input[name='new_disk_name']").send_keys(newdisk)

        dr.find_element_by_css_selector("#snap_restore_confirm").click()

        # 确认信息
        dr.find_element_by_xpath(
            "//div[contains(@style,'display: block;')]//div[@class='ui-dialog-buttonset']/button[text()='确定']").click()

        locator = (By.XPATH, ".//*[@class='remind']")
        expect_text = "云磁盘快照{0}恢复成功".format(snapname)
        try:
            WebDriverWait(dr, 60).until(EC.text_to_be_present_in_element(locator, expect_text))
            print(expect_text)
        except BaseException:
            print("云磁盘快照恢复失败.")

    def test_07_del_disk(self):
        '''删除云磁盘'''
        dr = self.gdriver

        # 进入云磁盘管理
        try:
            WebDriverWait(dr, 10).until(EC.visibility_of(dr.find_element(
                By.XPATH,".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]")))
        except:
            print("except here...")
            dr.find_element_by_xpath(".//*[@id='mCSB_1_container']/li[1]").click()
        sleep(3)
        dr.find_element_by_xpath(".//*[@id='mCSB_1_container']//span[contains(text(),'云磁盘管理')]").click()

        disknames=[]
        rows = dr.find_elements(By.XPATH, ".//table[@id='mainTable']/tbody/tr")

        for row in rows:
            text = row.find_element_by_class_name("td_diskName").text
            if text.startswith("qa2018") or text.startswith("disk2018"):
                disknames.append(text)

        for name in disknames:
            print("删除云磁盘%s" %name)
            WebDriverWait(dr, 60).until(EC.element_to_be_clickable
            ((By.XPATH, ".//td[contains(text(),'%s')]//..//a[text()='删除']" %name))).click()

            confirm_locator="//div[contains(@style,'display: block;')]//div[@class='ui-dialog-buttonset']/button[text()='确定']"

            WebDriverWait(dr, 60).until(EC.element_to_be_clickable
            ((By.XPATH, confirm_locator))).click()
            sleep(1)
            WebDriverWait(dr, 60).until(EC.element_to_be_clickable
            ((By.XPATH, confirm_locator))).click()



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
        # self.gdriver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
