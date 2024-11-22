from selenium.webdriver.common.by import By
from dummy.dummy_data.dummy import obj_loct, base_data


def auto_login(browser):
    browser.find_element(*obj_loct.inpt_vld_email).send_keys(base_data.vld_email)
    browser.find_element(*obj_loct.inpt_vld_pass).send_keys(base_data.vld_pass)
    browser.find_element(*obj_loct.btn_login).click()