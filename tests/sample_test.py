from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_coffee():
    driver = webdriver.Chrome()  # Make sure ChromeDriver is in your PATH or specify the path
    driver.get("https://coffee-cart.app/")
    assert "Coffee cart" in driver.title
    driver.quit()