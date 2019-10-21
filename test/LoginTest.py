from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from Page.LoginPage import LoginPage
from Page.HomePage import HomePage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.clcik_logout()



        # self.driver.maximize_window()
        # self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        # self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        # self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()
        # self.driver.find_element_by_xpath("//a[@id='welcome']").click()
        # self.driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()















