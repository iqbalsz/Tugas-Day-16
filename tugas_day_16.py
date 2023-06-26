import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class tugas_day_16(unittest.TestCase):

    def setUp(self):
        # selfbrowser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  

    def test_a_success_login(self):
        #steps
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)

        #validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('Products',response_data)

    def test_add_to_cart(self):
        #steps
        driver = self.browser
        # == login == 
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # driver.get("https://www.saucedemo.com/inventory.html")
        # time.sleep(3)
        # driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(3)

        #validasi
        response_data = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
        self.assertIn('Sauce Labs Backpack',response_data)


    def test_checkout(self):
        #steps
        driver = self.browser
        # == login == 
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)

        # == add to cart ==
        # driver.get("https://www.saucedemo.com/inventory.html")
        # time.sleep(3)
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(3)

        # == checkout ==
        driver.find_element(By.ID,"checkout").click()
        time.sleep(3)
        driver.find_element(By.ID,"first-name").send_keys("Arif")
        time.sleep(1)
        driver.find_element(By.ID,"last-name").send_keys("Iqbal")
        time.sleep(1)
        driver.find_element(By.ID,"postal-code").send_keys("31414")
        time.sleep(1)
        driver.find_element(By.ID,"continue").click()
        time.sleep(3)
        driver.find_element(By.ID,"finish").click()
        time.sleep(3)

        #validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('Checkout: Complete!',response_data)

    def test_logout(self):
        #steps
        driver = self.browser
        # == login == 
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)

        # == logout==
        driver.find_element(By.ID,"react-burger-menu-btn").click()
        time.sleep(2)
        driver.find_element(By.ID,"logout_sidebar_link").click()
        time.sleep(3)

        #validasi
        response_data = driver.find_element(By.CLASS_NAME,"login_logo").text
        self.assertIn('Swag Labs',response_data)  

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()