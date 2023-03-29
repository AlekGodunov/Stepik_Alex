import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    category = "//*[@id='homepage-catalog-submenu']/div/div[1]/div[1]/a[4]"
    catalog = "//span[@class='header-bottom__catalog-spoiler']"

    #Getters
    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog)))
    def get_category(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.category)))

    #Actions
    def click_catalog(self):
        self.get_catalog().click()
        print("Открыт каталог")


    def click_category(self):
        self.get_category().click()
        print("Выбран раздел")

    #Methods

    def cat1(self):
        self.click_catalog()
        self.click_category()
        time.sleep(2)
