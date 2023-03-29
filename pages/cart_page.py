import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    position = "//*[@class='cart-items__product-name']"
    from_sklad = "//*[@id='total-amount']/div[1]/div[2]/div/div/label/span[2]"
    arrage = "//*[@id='buy-btn-main']/span"


    #Getters
    def get_posotion(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.position)))
    def get_from_sklad(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.from_sklad)))
    def get_arrage(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.arrage)))




    #Actions
    def click_from_sklad(self):
        self.get_from_sklad().click()
        print("Со склада")

    def click_arrage(self):
        self.get_arrage().click()
        print("Переход в оформление")



    #Methods

    def cat3(self):
        self.assert_word(self.get_posotion(), "Встраиваемая микроволновая печь Bosch BEL653MW3 белый")
        time.sleep(2)
        self.click_from_sklad()
        time.sleep(3)
        self.click_arrage()
        time.sleep(5)


