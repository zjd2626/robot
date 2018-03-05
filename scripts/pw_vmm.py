#!/usr/bin/python3
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

# import httplib


import requests




if "/home/clouder/robot/lib" not in sys.path:
    sys.path.append("/home/clouder/robot/lib")

import driver
dr=driver.get_driver()


# driver=webdriver.Firefox()
# url='http://172.28.101.22:8080'
# driver.get(url)
# driver.find_element_by_id('userName').send_keys('root')
# driver.find_element_by_id('password').send_keys('Power@1')
# driver.find_element_by_xpath('//*[@id="msg1"]').click()
# time.sleep(10)
# driver.find_element_by_xpath('//*[@id="menubar"]/ul/li[@class="z selected"]/a').click()
# driver.find_element_by_css_selector("z.selected>a").click()
#
# ele = driver.find_element_by_xpath("//*[@id='menubar']/ul/li/span[contains(text(),'系统配置')]")
# ActionChains(driver).move_to_element(ele).perform()
# driver.find_element_by_xpath("//*[@id='menubar']/ul/li/span[contains(text(),'系统配置')]").click()
# driver.find_element_by_xpath("//*[@id='menubar']/ul/li/span[contains(text(),'系统配置')]").click()
# driver.find_element_by_xpath('//*[@id="createTemplate"]').click()


# # driver.find_element_by_xpath('//*[@id="section1"]//span[contains(text(),"PowerView")]').click()
#
# WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,u'//*[@id="section1"]//span[contains(text(),"PowerView")]'))).click()
# time.sleep(5)
# WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,u'//*[@id="content"]//a[@title="最大化"]'))).click()
# driver.switch_to.frame("ifr_appId_5")
# # time.sleep(5)
# WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,u'//*[@id="mCSB_1_container"]/li[1]'))).click()
# # time.sleep(5)
# dragger = driver.find_element_by_xpath("//*[@id='mCSB_1_dragger_vertical']/div") # 被拖拽元素
# item2 = driver.find_element_by_xpath(u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"资源配置")]') # 目标
# ActionChains(driver).drag_and_drop(dragger, item2).perform() # 1.移动dragger到目标
# WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"私有网络管理")]'))).click()
# time.sleep(3)
# action.click_and_hold(dragger).release(item2).perform()

# "//*[@id='mCSB_1_dragger_vertical']/div"
# "//*[@id='mCSB_1_dragger_vertical']/div"
# "style="position: absolute; min-height: 30px; height: 188px; top: 180px; display: block; max-height: 381px;""
# WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]'))).click()
# time.sleep(10)
# WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,u'//*[@id="stretch-table"]/tbody/tr/td[1]/a[@vmName="xiang1031-1"]'))).click()
'''
driver.find_element_by_xpath(u'//*[@id="mCSB_1_container"]/ul[1]/li[1]/a/span[contains(text(),"创建虚拟机")]').click()
ele = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]')
ActionChains(driver).move_to_element(ele).move_by_offset(10,10).perform()
driver.find_element_by_xpath('//*[@id="createTemplate"]').click()
'''

# ActionChains(driver).move_to_element(ele).perform()
# ActionChains(driver).move_to_element(ele).move_by_offset(10,3).perform()

# ActionChains(driver).move_to_element(ele).perform()
# moveByOffset(10, 3).build().perform()


# driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/p').click()


# driver.find_element_by_xpath(u'//*[@id="mCSB_1_container"]/ul[1]/li[1]/a/span[contains(text(),"创建虚拟机")]').click()
#
#
# //*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]
# # //*[@id="mCSB_1_container"]/ul[1]/li[1]/a/span[contains(text(),"创建虚拟机")]

# WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,u'//*[@id="mCSB_1_container"]/li//span[contains(text(),"资源管理")]'))).click()

# vmName2 = vmName + '-1'


def entry_to_vmm(driver):
    # WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((By.XPATH, u'//*[@id="mCSB_1_container"]/li[1]'))).click()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, u'//*[@id="mCSB_1_container"]/li//span[contains(text(),"资源管理")]'))).click()
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,u'//*[@id="mCSB_1_container"]/ul[1]/li/a/span[contains(text(),"虚拟机管理")]'))).click()




def is_present_vm(driver, vmName):
    time.sleep(10)
    # WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,u'//*[@id="stretch-table"]/tbody/tr/td[1]/a[@vmName="%s]' % vmName))).click()
    all_row = driver.find_elements_by_xpath('//*[@name="dataTr"]')
    print(all_row)
    # def is_present_vm(driver,vmName):
    rownum = len(all_row)

    for i in range(rownum):
        print(all_row[i])
        name = all_row[i].find_elements_by_tag_name('td')[1].text.split("-")[0]
        name1 = all_row[i].find_elements_by_tag_name('td')[1].text
        status = all_row[i].find_elements_by_tag_name('td')[2].text
        print("vmName is %s,vmStatus is %s" % (name, status))
        if name == vmName:
            print("enter click vmname,i")
            print (i)

            # all_row[i].find_elements_by_xpath('td[1]/input')[.click()
            # # driver.find_element_by_xpath("//*[@id='stretch-table']/tbody/tr[%s]/td[3]" %i).click()
            # Select = driver.find_element_by_xpath("/*[@id='stretch-table']/tbody/tr/td[1]/input")

            driver.find_element_by_xpath("//*[@id='stretch-table']/tbody/tr['%s']/td[1]/input" %i).click()
            # driver.find_element_by_xpath("//*[@id='stretch-table']/tbody/tr[1]/td[1]/input").send_keys(Keys.SPACE)

            # if driver.find_element_by_xpath('//input/../[@displayname="%s"]',% name1).is_selected():
            if driver.find_element_by_xpath("//*[@id='stretch-table']/tbody/tr['%s']/td[1]/input" %i).is_selected():
                print('vm is selected!')
            else:
                print('vm not selected!')
            return status


def select_vm(driver, vmName):
    # number=vmName.split('-')[1]
    vmName2=vmName+'-1'
    print("vmName with number", vmName2)
    time.sleep(10)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[1]/input" % vmName2))).click()

    if driver.find_element_by_xpath("//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[1]/input" % vmName2).is_selected():
        print('vm is selected!')
    else:
        print('vm not selected!')
    status = driver.find_element_by_xpath("//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[3]" % vmName2).text
    print("status",status)
    return vmName2,status


def stop_vm(driver,vmName):
    # vmStatus=is_present_vm(driver,vmName)
    result=select_vm(driver,vmName)
    vmStatus=result[1]
    if vmStatus==u'运行':
        driver.find_element_by_xpath('//*[@id="operations"]/a[2]').click()
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, u"html/body/div[5]/div[3]/div/button[1]"))).click()
        time.sleep(20)
        vmStatus2=is_present_vm(driver,vmName)
        if vmStatus2 == u'停止':
            print("stop vm sucess")


def start_vm(driver,vmName):
    # vmStatus=is_present_vm(driver,vmName)
    result=select_vm(driver,vmName)
    vmStatus=result[1]
    if vmStatus==u'停止':
        driver.find_element_by_xpath('//*[@id="operations"]/a[1]').click()
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, u"html/body/div[5]/div[3]/div/button[1]"))).click()
        time.sleep(20)
        vmStatus2=is_present_vm(driver,vmName)
        if vmStatus2 == u'运行':
            print("start vm sucess")

def restart_vm(driver,vmName):
    # vmStatus=is_present_vm(driver,vmName)
    result=select_vm(driver,vmName)
    vmStatus=result[1]
    if vmStatus==u'运行':
        driver.find_element_by_xpath('//*[@id="operations"]/a[1]').click()
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, u"html/body/div[5]/div[3]/div/button[1]"))).click()
        time.sleep(20)
        vmStatus2=is_present_vm(driver,vmName)
        if vmStatus2 == u'运行':
            print("start vm sucess")

def delete_vm(driver,vmName):
    result=select_vm(driver,vmName)
    vmName2=result[0]
    driver.find_element_by_xpath( "//*[@id='operations']/a[5]/span").click()
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, u"html/body/div[5]/div[3]/div/button[1]"))).click()
    try:
        WebDriverWait(driver,40).until(EC.invisibility_of_element_located((By.XPATH,"//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[1]/input" % vmName2)))
        print("delete vmname '%s' success",vmName2)
    except TimeoutException:
        print("delete vmname '%s' failed",vmName2)

def isstop_vm(driver, vmName):
    # vmStatus=is_present_vm(driver,vmName)
    result = select_vm(driver, vmName)
    vmStatus = result[1]
    if vmStatus == u'停止':
        pass
    elif vmStatus == u'运行':
        stop_vm(driver,vmName)

def isstart_vm(driver, vmName):
    # vmStatus=is_present_vm(driver,vmName)
    result = select_vm(driver, vmName)
    vmStatus = result[1]
    if vmStatus == u'运行':
        pass
    elif vmStatus == u'停止':
        start_vm(driver, vmName)





# ".//*[@id='stretch-table']/tbody/tr[6]/td[10]/a[1]"
# "//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[10]/a[contains(text(),'查看云磁盘')]" % vmName2
# "//*[@id='cloudDiskForm']/div[2]/input"
def enter_clouddiskmanage(driver,vmName):
    result=select_vm(driver,vmName)
    vmName2=result[0]
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, u"//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[10]/a[contains(text(),'查看云磁盘')]" % vmName2))).click()
    try:
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, u"//*[@id='cloudDiskForm']/div[2]/input[@value='%s']" % vmName2)))
        print("check clouddisk success")
    except TimeoutException:
        print("check clouddisk failed")

def templaname_gen():
    return "testqa" + time.strftime("%H%M%S")



def copy_to_templet(driver,vmName):
    # result=select_vm(driver,vmName)
    isstop_vm(driver, vmName)
    # vmName2=result[0]
    templa_name = templaname_gen()
    driver.find_element_by_xpath("//*[@id='operations']/a/span[contains(text(),'复制为模板')]").click()
    # WebDriverWait(driver, 20).until(
    # EC.element_to_be_clickable((By.XPATH, u"//*[@id='copy_as_template_form']/div/div/input[@name='name']"))).send_ke
    # driver.find_element_by_xpath(u"//*[@id='copy_as_template_form']/div/div/input[@name='name']").clear()
    driver.find_element_by_xpath(u"//*[@id='copy_as_template_form']/div/div/input[@name='name']").send_keys(templa_name)
    driver.find_element_by_xpath(u"//*[@id='copy_as_template_form']/div/div/textarea").send_keys(templa_name)
    driver.find_element_by_xpath(u"//*[@id='submit_but']").click()
    info=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,u"//*[@id='infoMessage']"))).text
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, u"html/body//div[contains(@style,'display: block;')]/div/button"))).click()
    if info.__contains__("复制为模板任务启动成功!"):
        print ("复制为模板任务启动成功")
    else:
        print ("复制为模板任务启动failed")


def vnc_view(driver,vmName):
    isstart_vm(driver,vmName)
    vmName2 = vmName + '-1'
    vnclink=driver.find_element_by_xpath("//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[10]/a[contains(text(),'VNC访问')]" % vmName2)
    url=vnclink.get_attribute('href')
    print (url)
    r = requests.get(url, allow_redirects = False)
    print  (r.status_code)
    if r.status_code == 200:
        print ("vnc 访问成功")
    else:
        print ("vnc 访问失败")

    # pw_handle=driver.current_window_handle
    # print ('pw_handle',pw_handle)
    # WebDriverWait(driver, 40).until(
    #     EC.element_to_be_clickable((By.XPATH, u"//*[@id='stretch-table']/tbody/tr[@displayname='%s']/td[10]/a[contains(text(),'VNC访问')]" % vmName2))).click()
    # driver.find_element_by_xpath("")
    # handle=driver.current_window_handle
    # print ("handle",handle)
    # all_handles=driver.window_handles
    # for handle in all_handles:
    #     if handle != pw_handle:
    #         print ('enter to vnc page')
    #         driver.switch_to.window(handle)
    #         print ('vnc',handle,driver.title,driver.current_url)
    # print (driver.title)
    # # driver.close()
    # driver.switch_to.window(pw_handle)
    # print (driver.title,driver.current_url)



# driver.__getattribute__()

# "html/body/div[7]/div[3]/div/button"
# "html/body/div/div[contains(@style,'display: block;')]/div/button"




    # searchname=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,u"//*[@id='cloudDiskForm']/div[2]/input"))).text
    #
    # print ("searchname", searchname)
    # print ("vmName2", vmName2)
    # if searchname.__contains__(vmName2):
    #     print ("check clouddisk success")
    # else:
    #     print ("check clouddisk failed")

        # "//*[@id='cloudDiskForm']/div[2]/input[@value="cytest1030-1"]"

                    # class vm_manage(unittest.TestCase):
#


# entry_to_vmm(driver)
# # start_vm(driver,'xiang1031-1')
# # select_vm(driver,'cytest1030')
# # select_vm(driver,'spider')
# # delete_vm(driver,'xiang1102')
# #stop_vm(driver,'cytest1030')
entry_to_vmm(dr)
vnc_view(dr,'gjzvm11062')

# copy_to_templet(dr,'cytest2')
# select_vm(driver,'cytest1030')
# enter_clouddiskmanage(dr,'cytest1030')