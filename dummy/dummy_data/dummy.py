
from selenium.webdriver.common.by import By
import string
import random

def email_gen():
    name = "Jarang_Rugi0"
    domain = "@gmail.com"
    randomize = str(random.randint(1, 3))
    email = name + randomize + domain
    return email


def generate_random_string():
    length = 5
    base_name = "Jarang_rugi_"
    domain = "@google.com"
    characters = string.ascii_lowercase + string.digits
    random_str = ''.join(random.choice(characters) for _ in range(length))
    email = base_name + random_str + domain
    return email

class base_data():
    URL = 'https://demowebshop.tricentis.com'
    firstname = "Jarang"
    lastname = "Rugi"
    email = email_gen()
    new_email = generate_random_string()
    password = "QWEqwe123"
    confirm_password = password
    vld_email = email
    vld_pass = password
    full_name = firstname + " " + lastname
    mssg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    cmpny_name = "PT. Selalu Untung"
    city = "Jakarta"
    country = "Indonesia"
    Address = "Jln. Galaxy Bermuda Anggel" 
    postal_code = "51432"
    Phone_number = "088723712618"

class obj_loct():
    inpt_frstname = (By.ID, 'FirstName')
    inpt_lstname = (By.ID, 'LastName')
    inpt_email = (By.ID, 'Email')
    inpt_pw = (By.ID, 'Password')
    inpt_cnfrmpw = (By.ID, 'ConfirmPassword')
    btn_regist  = (By.ID, 'register-button')
    rbg_male = (By.ID, 'gender-male')
    rbg_female = (By.ID, 'gender-female')
    inpt_vld_email = (By.CSS_SELECTOR, "input.email")
    inpt_vld_pass = (By.CSS_SELECTOR, "input.password")
    btn_login = (By.CSS_SELECTOR, "input.button-1.login-button")
    product_item_1 = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[3]/div[2]/input")
    inpt_recipt_name = (By.ID, "giftcard_2_RecipientName")
    inpt_recipt_email = (By.CLASS_NAME, "recipient-email")
    inpt_mssg = (By.ID, "giftcard_2_Message")
    btn_add2cart = (By.CLASS_NAME, "button-1.add-to-cart-button")
    ntf_err = (By.CSS_SELECTOR, ".content") # Error saat mau klik add 2 cart
    chk_box_tos = (By.ID, "termsofservice")
    btn_checkout = (By.CLASS_NAME, "button-1.checkout-button")
    inpt_compny = (By.ID, "BillingNewAddress_Company")
    drop_dwn_country = (By.ID, "BillingNewAddress_CountryId")
    inpt_city = (By.ID, "BillingNewAddress_City")
    billing_address = (By.ID, "billing-address-select")
    inpt_address = (By.ID, "BillingNewAddress_Address1")
    inpt_zip = (By.ID, "BillingNewAddress_ZipPostalCode")
    inpt_phone = (By.ID, "BillingNewAddress_PhoneNumber")
    btn_cntinue1 = (By.CLASS_NAME, "button-1.new-address-next-step-button")
    rdop_COD = (By.ID, "paymentmethod_0")
    btn_cntinue2 = (By.CLASS_NAME, "button-1.payment-method-next-step-button")
    btn_cntinue3 = (By.CLASS_NAME, "button-1.payment-info-next-step-button")
    btn_cntinue4 = (By.CLASS_NAME, "button-1.confirm-order-next-step-button")
    cnfrm_lyr = (By.CLASS_NAME, "title")

