
from selenium import webdriver

from pages.cart_page import Cart_page
from pages.catalog_page import Catalog_page
from pages.login_page import Login_page
from pages.main_page import Main_page




def test_select_product():
    driver = webdriver.Chrome(
            executable_path='C:\\Users\\Godunov\\PycharmProjects\\pythonProject\\chromedriver.exe')


    login = Login_page(driver)
    login.authorization()
    main = Main_page(driver)
    main.cat1()
    catalog = Catalog_page(driver)
    catalog.cat2()
    cart = Cart_page(driver)
    cart.cat3()












