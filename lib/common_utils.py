from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_confirm_msg(driver, timeout, action):
    try:
        msg = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((
                By.XPATH, u'//div[contains(@style,"display: block;")]//span[@id="confirmMessage"]'))).text
        return msg
    except:
        return action + u"超时"

def get_info_msg(driver, timeout, action):
    try:
        msg = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((
                By.XPATH, u'//div[contains(@style,"display: block;")]//span[@id="infoMessage"]'))).text
        return msg
    except:
        return action + u"超时"

#####待完善
def into_resource_config(driver, module, sub_module):
    """进入模块
       module - 父模块，　如资源管理
       sub_module - 子模块，　如云主机管理
    """
    WebDriverWait(driver, 180).until(EC.element_to_be_clickable((
        By.XPATH, u'//div[@id="mCSB_1_container"]/li/span[contains(text(), %s)]'% module))).click()
    WebDriverWait(driver, 6).until(EC.visibility_of(driver.find_element(
        by=By.XPATH, value=".//*[@id='mCSB_1_container']//ul//li/a/span[test()=%s]" %sub_module))).click()
