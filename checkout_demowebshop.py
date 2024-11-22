import unittest
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from dummy.dummy_data.dummy import base_data, obj_loct
from dummy.dummy_data.auto_login import auto_login
from selenium.common.exceptions import NoSuchElementException

def is_element_present(by, id, driver): 
    try: 
        driver.find_element(by, id) 
        return True 
    except NoSuchElementException: 
        return False

class Demowebshop(unittest.TestCase):
    def setUp(self):
        option = Options()
        option.add_experimental_option("detach", True)
        self.browser = webdriver.Edge(options=option)

    def test_check_out_product(self):
        browser = self.browser
        browser.get(base_data.URL + '/login')
        auto_login(browser)
        browser.find_element(*obj_loct.product_item_1).click()
        time.sleep(2)
        browser.find_element(*obj_loct.inpt_recipt_name).send_keys(base_data.full_name)
        browser.find_element(*obj_loct.inpt_recipt_email).send_keys(base_data.email)
        browser.find_element(*obj_loct.inpt_mssg).send_keys(base_data.mssg)        
        browser.find_element(*obj_loct.btn_add2cart).click()
        time.sleep(3)
        browser.get(base_data.URL + '/cart')
        browser.find_element(*obj_loct.chk_box_tos).click()
        browser.find_element(*obj_loct.btn_checkout).click() 
        time.sleep(2)
        if is_element_present(By.ID, "billing-address-select", browser):
            browser.find_element(*obj_loct.btn_cntinue1).click()
        else:
            browser.find_element(*obj_loct.inpt_compny).send_keys(base_data.cmpny_name)       
            Select(browser.find_element(*obj_loct.drop_dwn_country)).select_by_index(42)#select_by_value(base_data.country)
            browser.find_element(*obj_loct.inpt_city).send_keys(base_data.city)
            browser.find_element(*obj_loct.inpt_address).send_keys(base_data.Address)
            browser.find_element(*obj_loct.inpt_zip).send_keys(base_data.postal_code)
            browser.find_element(*obj_loct.inpt_phone).send_keys(base_data.Phone_number)    
            browser.find_element(*obj_loct.btn_cntinue1).click()        
        time.sleep(2)
        browser.find_element(*obj_loct.rdop_COD).click()
        browser.find_element(*obj_loct.btn_cntinue2).click()
        time.sleep(2)
        browser.find_element(*obj_loct.btn_cntinue3).click()
        time.sleep(2)
        browser.find_element(*obj_loct.btn_cntinue4).click()
        time.sleep(2)
        mssg = browser.find_element(*obj_loct.cnfrm_lyr).text
        self.assertIn("Your order has been successfully processed!", mssg) 
        time.sleep(2)
    #def tearDown(self):
        #self.browser.quit()

if __name__ == "__main__":
    unittest.main()