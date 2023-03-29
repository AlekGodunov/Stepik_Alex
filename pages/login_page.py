import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Login_page(Base):

    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    enter1_loc = "//div[@class='user-profile__login']"
    enter2_loc = "//*[@id='header-search']/div/div[3]/div[2]/div/div/div[3]/div/div[2]/div/div[1]/button/span"
    enter_with_password_loc = "//div[@class='block-other-login-methods__password-caption']"
    send_user_name_loc = "//input[@autocomplete='username']"
    send_password_loc = "//input[@autocomplete='current-password']"
    enter3_loc = "//button[@class='base-ui-button-v2_big base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2']"


    #Getters
    def get_enter1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter1_loc)))
    def get_enter2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter2_loc)))
    def get_enter3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter3_loc)))
    def get_enter_with_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_with_password_loc)))
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.send_user_name_loc)))
    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.send_password_loc)))

    #Actions
    def click_enter1(self):
        self.get_enter1().click()
        print("Нажато Войти")

    def click_enter2(self):
        self.get_enter2().click()
        print("Нажато Войти 2")

    def click_enter_with_password(self):
        self.get_enter_with_password().click()
        print("Нажато Войти с паролем")

    def send_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Введен логин")

    def send_password(self, password):
        self.get_password().send_keys(password)
        print("Введен пароль")

    def click_enter3(self):
        self.get_enter3().click()
        print("Нажато Войти 3")

    #Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_enter1()
        self.click_enter2()
        self.click_enter_with_password()
        self.send_user_name("godun007@mail.ru")
        self.send_password("silenthill5")
        self.click_enter3()
        time.sleep(2)










