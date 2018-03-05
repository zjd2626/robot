# -*- coding: utf-8 -*-
#__author__='qianfen.zheng'
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import os

if os.path.abspath("../lib") not in sys.path:
        sys.path.append(os.path.abspath("../lib"))

import common_utils
import log


'''桌面策略配置相关操作'''

# 配置项总数
CONFIG_NUM = 8


def into_desktop_policy(driver):
    """进入桌面策略模块
    """

    WebDriverWait(driver, 180).until(EC.element_to_be_clickable(
        (By.XPATH, u'//div[@id="mCSB_1_container"]/li/span[contains(text(),"资源管理")]'))).click()
    WebDriverWait(driver, 6).until(EC.visibility_of(driver.find_element(
        by=By.XPATH, value=".//*[@id='mCSB_1_container']//ul//li/a/span[contains(text(),'桌面策略')]"))).click()
    time.sleep(3)


def create_policy(driver, name, description, delivery, configs=()):
    """创建桌面策略
    configs - 传入一个元组，　用于设置驱动器、剪贴板等项的启停。 顺序为先上下，后左右。可选参数，默认不做设置，即还是页面原先的默认值
    　　　　　　对于只有启动和停止的选项的项，使用０表示停止、１表示启动
    　　　　　　对于’音频质量‘，使用１表示动态，２表示中，３表示高
    """
    log.logger.info("－－－－－－－－开始创建桌面策略－－－－－－－－－－－－－－")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, u'.//*[@id="content"]//div/a/span[contains(text(), "创建")]'))).click()

    driver.find_element_by_id('name').send_keys(name)
    driver.find_element_by_id('description').send_keys(description)
    driver.find_element_by_id('deliveryGroupId').send_keys(delivery)

    if configs and len(configs) == CONFIG_NUM:
        __config(driver, configs)

    driver.find_element_by_id("submit_but").click()
    msg = get_msg(driver, 20, "创建桌面策略")
    if u"超时" not in msg:
        driver.find_element_by_xpath(
            u'//div[contains(@style,"display: block;")]//div[@class="ui-dialog-buttonset"]/button[contains(text(),"确定")]').click()
    log.logger.info(msg)

    log.logger.info("－－－－－－－－创建桌面策略结束－－－－－－－－－－－－－－")


def search_policy_by_name(driver, name):
    """根据策略名关键字搜索策略
    """

    name_input = driver.find_element_by_xpath('.//input[@name="name"]')
    name_input.clear()
    name_input.send_keys(name)

    driver.find_element_by_xpath(".//*[@id='search']/input").click()


def search_policy_by_delivery_name(driver, delivery):
    """ 根据策略名关键字搜索策略
    """

    name_input = driver.find_element_by_xpath('.//input[@name="groupName"]')
    name_input.clear()
    name_input.send_keys(delivery)

    driver.find_element_by_xpath(".//*[@id='search']/input").click()


def update_policy(driver, name, description, configs=()):
    """修改桌面策略
    """

    log.logger.info("－－－－－－－－开始修改桌面策略－－－－－－－－－－－－－－")
    # 由于要修改的策略可能不在第一页，所以先通过搜索使它展现在第一页，方便定位
    search_policy_by_name(driver, name)
    driver.find_element_by_xpath(
        u".//*[@id='content']/div[2]/table[2]/tbody/tr/td[text()='%s']/../td/a[contains(text(), '修改')]" % name).click()

    time.sleep(2)
    driver.find_element_by_id('description').send_keys(description)

    if configs and len(configs) == CONFIG_NUM:
        __config(driver, configs)

    driver.find_element_by_id("submit_but").click()
    msg = get_msg(driver, 20, "修改桌面策略")
    if u"超时" not in msg:
        driver.find_element_by_xpath(
            u'//div[contains(@style,"display: block;")]//div[@class="ui-dialog-buttonset"]/button[contains(text(),"确定")]').click()
    log.logger.info(msg)

    log.logger.info("－－－－－－－－修改桌面策略结束－－－－－－－－－－－－－－")


def delete_policy(driver, name):
    """删除桌面策略
    """

    log.logger.info("－－－－－－－－开始删除桌面策略－－－－－－－－－－－－－－")

    # 由于要修改的策略可能不在第一页，所以先通过搜索使它展现在第一页，方便定位
    search_policy_by_name(driver, name)
    driver.find_element_by_xpath(
        u".//*[@id='content']/div[2]/table[2]/tbody/tr/td[text()='%s']/../td/a[contains(text(), '删除')]" % name).click()
    driver.find_element_by_xpath(
        u'//div[contains(@style,"display: block;")]//div[@class="ui-dialog-buttonset"]/button[contains(text(),"确定")]').click()

    msg = common_utils.get_info_msg(driver, 20, "删除桌面策略")
    if u"超时" not in msg:
        driver.find_element_by_xpath(
            u'//div[contains(@style,"display: block;")]//div[@class="ui-dialog-buttonset"]/button[contains(text(),"确定")]').click()
    log.logger.info(msg)

    log.logger.info("－－－－－－－－删除桌面策略结束－－－－－－－－－－－－－－")


def gen_policy_name(prefix='policy'):
    """生成策略名
    """

    t = time.strftime("%m%d%H%M%S", time.localtime())
    policy_name = prefix + t
    return policy_name


def __config(driver, configs):
    # 驱动器
    if configs[0] == 1:
        driver.find_element_by_id('driver1').click()
    else:
        driver.find_element_by_id('driver2').click()

    # 剪贴板
    if configs[1] == 1:
        driver.find_element_by_id('clipboard1').click()
    else:
        driver.find_element_by_id('clipboard2').click()

    # 智能卡
    if configs[2] == 1:
        driver.find_element_by_id('smartcard1').click()
    else:
        driver.find_element_by_id('smartcard2').click()

    # 打印机
    if configs[3] == 1:
        driver.find_element_by_id('printer1').click()
    else:
        driver.find_element_by_id('printer2').click()

    # USB设备
    if configs[4] == 1:
        driver.find_element_by_id('plugandplaydevice1').click()
    else:

        driver.find_element_by_id('plugandplaydevice2').click()

    # 音频录制
    if configs[5] == 1:
        driver.find_element_by_id('audiorecord1').click()
    else:
        driver.find_element_by_id('audiorecord2').click()

    # 音频播放
    if configs[6] == 1:
        driver.find_element_by_id('audioplay1').click()
    else:
        driver.find_element_by_id('audioplay2').click()

    # 音频质量
    if configs[7] == 1:
        driver.find_element_by_id('audioquality1').click()
    elif configs[7] == 2:
        driver.find_element_by_id('audioquality2').click()
    else:
        driver.find_element_by_id('audioquality3').click()


def get_msg(driver, timeout, action):
    try:
        time.sleep(2)
        msg = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((
                By.XPATH, u'.//div[contains(@style,"display: block;")]//div[@class="ui-dialog-content ui-widget-content" and contains(@style, "display: block;")]'))).get_attribute('textContent')
        return msg
    except BaseException:
        return action + u"超时"
