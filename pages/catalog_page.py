import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Catalog_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    filter_small_price = "/html/body/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[3]/div/div/div[1]/input"
    filter_bosh = "/html/body/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[5]/div/div/div[2]/label[3]/span[2]"
    show = "//div[@class='apply-filters-float-btn']"
    product = "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[1]/div[4]/div[4]/button[2]"
    to_cart = "/html/body/div[2]/div/div[2]/div/div[3]/div/div[1]/div[4]/div[4]/button[2]"

    #Getters
    def get_filter_small_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_small_price)))

    def get_filter_bosh(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_bosh)))

    def get_show(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.show)))

    def get_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_buy(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.to_cart)))


    #Actions
    def click_filter_bosh(self):
        self.get_filter_bosh().click()
        print("Выбран фильтр")


    def input_filter_small_price(self, small_price):
        self.get_filter_small_price().send_keys(small_price)
        print("Указана минимальная цена")


    def click_show(self):
        self.get_show().click()
        print("Нажато Показать")

    def click_product(self):
        self.get_product().click()
        print("Выбран продукт")

    def click_to_cart(self):
        self.get_buy().click()
        print("В корзине")


    #Methods

    def cat2(self):
        self.driver.execute_script("window.scrollTo(0,750)")
        time.sleep(1)
        self.input_filter_small_price("10400")
        time.sleep(1)
        self.click_filter_bosh()
        time.sleep(2)
        self.click_show()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,750)")
        time.sleep(1)
        self.click_product()
        time.sleep(3)
        self.click_to_cart()
        time.sleep(5)

