import unittest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dummy.dummy_data.dummy import base_data, obj_loct

class Demowebshop(unittest.TestCase):
    def setUp(self):
        option = Options()
        option.add_experimental_option("detach", True)
        self.browser = webdriver.Edge(options=option)
        self.browser.get(base_data.URL + '/login')

    def test_L1_login_with_valid_email(self):
        browser = self.browser
        browser.find_element(*obj_loct.inpt_vld_email).send_keys(base_data.vld_email)
        browser.find_element(*obj_loct.inpt_vld_pass).send_keys(base_data.vld_pass)
        browser.find_element(*obj_loct.btn_login).click()
        get_url = browser.current_url
        self.assertEqual(get_url[:len(get_url) - 1], base_data.URL)

    def test_L2_login_with_invalid_email_format(self):
        browser = self.browser
        invalid = base_data.vld_email
        invld_email = invalid[:len(invalid) - 4]
        browser.find_element(*obj_loct.inpt_vld_email).send_keys(invld_email)
        browser.find_element(*obj_loct.inpt_vld_pass).send_keys(base_data.vld_pass)
        browser.find_element(*obj_loct.btn_login).click()
        err_msg = browser.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertEqual(err_msg, "Please enter a valid email address.")    
    
    def test_L3_login_with_empty_email(self):
        browser = self.browser
        browser.find_element(*obj_loct.inpt_vld_pass).send_keys(base_data.vld_pass)
        browser.find_element(*obj_loct.btn_login).click()
        err_msg = browser.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertIn("No customer account found",err_msg)    

    def test_L4_login_with_empty_password(self):
        browser = self.browser
        browser.find_element(*obj_loct.inpt_vld_email).send_keys(base_data.vld_email)
        browser.find_element(*obj_loct.btn_login).click()
        err_msg = browser.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertIn("The credentials provided are incorrect",err_msg)    

    def test_L5_login_with_invalid_password(self):
        browser = self.browser
        invalid = base_data.vld_pass
        invld_pass = invalid[:len(invalid) - 1]
        browser.find_element(*obj_loct.inpt_vld_email).send_keys(base_data.vld_email)
        browser.find_element(*obj_loct.inpt_vld_pass).send_keys(invld_pass)
        browser.find_element(*obj_loct.btn_login).click()
        err_msg = browser.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertIn("The credentials provided are incorrect",err_msg)    

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()