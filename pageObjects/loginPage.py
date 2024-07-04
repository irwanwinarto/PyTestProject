import pytest
from selenium import webdriver  # allows usage of chromedriver() exe that is installed on my local machine
from selenium.webdriver.common.by import By

# I am going to use this demo website, https://www.nopcommerce.com/en/demo, for testing purposes.


class LoginPage:

    # Keep page variables neat as class variables, because we use them throughout the page.
    # Do what you did before at t-mob, have a separate file for locators IF there are too many elements.
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"

    def __init__(self, driver): #this is the constructor of this class!
        self.driver = driver    # assign the browser driver.

    def set_username(self, username):

        # I am using a different find_element method format here.
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def set_password(self, password):

        # This is the other method format to use find_element method.
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
