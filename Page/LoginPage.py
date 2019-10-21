class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_xpath = "//input[@id='txtUsername']"
        self.pasword_xpath = "//input[@id='txtPassword']"
        self.login_button_xpath = "//input[@id='btnLogin']"

    def enter_username(self,username):
        self.driver.find_element_by_xpath(self.username_xpath).clear()
        self.driver.find_element_by_xpath(self.username_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.pasword_xpath).clear()
        self.driver.find_element_by_xpath(self.pasword_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

