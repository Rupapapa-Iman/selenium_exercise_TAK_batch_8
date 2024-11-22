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
        self.browser.get( base_data.URL + '/register')

    def test_R1_Register_with_valid_data(self):
        browser = self.browser
        browser.find_element(*obj_loct.rbg_male).click()
        browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
        browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
        browser.find_element(*obj_loct.inpt_email).send_keys(base_data.new_email)
        browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
        browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(base_data.confirm_password)
        browser.find_element(*obj_loct.btn_regist).click()
        get_url = browser.current_url
        self.assertIn('/registerresult/1', get_url)

    def test_R2_Register_with_empty_username(self):
        browser = self.browser
        browser.find_element(*obj_loct.rbg_male).click()
        browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
        browser.find_element(*obj_loct.inpt_email).send_keys(base_data.email)
        browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
        browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(base_data.confirm_password)
        browser.find_element(*obj_loct.btn_regist).click()
        err_msg = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='FirstName'] > span").text
        self.assertIn("First name is required", err_msg)

    def test_R3_Register_with_empty_lastname(self):
        browser = self.browser
        browser.find_element(*obj_loct.rbg_male).click()
        browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
        browser.find_element(*obj_loct.inpt_email).send_keys(base_data.email)
        browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
        browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(base_data.confirm_password)
        browser.find_element(*obj_loct.btn_regist).click()
        err_msg = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='LastName'] > span").text
        self.assertIn("Last name is required", err_msg)

    def test_R4_Register_with_invalid_email_format(self):
        browser = self.browser
        invalid = base_data.email
        invl_email = invalid[:len(invalid) - 8]
        browser.find_element(*obj_loct.rbg_male).click()
        browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
        browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
        browser.find_element(*obj_loct.inpt_email).send_keys(invl_email)
        browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
        browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(base_data.confirm_password)
        browser.find_element(*obj_loct.btn_regist).click()
        err_msg = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='Email'] > span").text
        self.assertIn("Wrong email", err_msg)

    def test_R5_Register_with_empty_email(self):
        browser = self.browser
        browser.find_element(*obj_loct.rbg_male).click()
        browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
        browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
        browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
        browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(base_data.confirm_password)
        browser.find_element(*obj_loct.btn_regist).click()
        err_msg = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='Email'] > span").text
        self.assertIn("Email is required", err_msg)

    def test_R6_Register_with_empty_password(self):
        browser = self.browser
        browser.find_element(*obj_loct.rbg_male).click()
        browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
        browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
        browser.find_element(*obj_loct.inpt_email).send_keys(base_data.email)
        browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(base_data.confirm_password)
        browser.find_element(*obj_loct.btn_regist).click()
        err_msg1 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='Password'] > span").text
        err_msg2 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='ConfirmPassword'] > span").text
        self.assertIn("Password is required", err_msg1)
        self.assertIn("The password and confirmation password do not match", err_msg2)

    def test_R7_Register_with_empty_confirmpassword(self):
        browser = self.browser
        browser.find_element(*obj_loct.rbg_male).click()
        browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
        browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
        browser.find_element(*obj_loct.inpt_email).send_keys(base_data.email)
        browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
        browser.find_element(*obj_loct.btn_regist).click()
        err_msg = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='ConfirmPassword'] > span").text
        self.assertIn("Password is required", err_msg)

    def test_R8_Register_with_empty_unmatch_password_n_confirmpassword(self):
        browser = self.browser
        invalid = base_data.confirm_password
        invld_pw = invl_email = invalid[:len(invalid) - 1]
        browser.find_element(*obj_loct.rbg_male).click()
        browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
        browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
        browser.find_element(*obj_loct.inpt_email).send_keys(base_data.email)
        browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
        browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(invld_pw)
        browser.find_element(*obj_loct.btn_regist).click()
        err_msg = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='ConfirmPassword'] > span").text
        self.assertIn("The password and confirmation password do not match", err_msg)

    def test_R9_with_none_input_form(self):
        browser = self.browser
        browser.find_element(*obj_loct.btn_regist).click()
        err_msg1 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='FirstName'] > span").text
        err_msg2 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='LastName'] > span").text
        err_msg3 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='Email'] > span").text
        err_msg4 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='Password'] > span").text
        err_msg5 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='ConfirmPassword'] > span").text
        self.assertIn("First name is required", err_msg1)
        self.assertIn("Last name is required", err_msg2)   
        self.assertIn("Email is required", err_msg3)             
        self.assertIn("Password is required", err_msg4)  
        self.assertIn("Password is required", err_msg5)  

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()