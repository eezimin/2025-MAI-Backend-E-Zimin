import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductListTest(unittest.TestCase):
    def setUp(self):
        print("Starting browser...")
        self.driver = webdriver.Chrome()

    def tearDown(self):
        print("Closing browser...")
        self.driver.quit()

    def test_click_button(self):
        print("Opening page...")
        self.driver.get("http://localhost:8000/web/products/")

        # Ожидание загрузки страницы
        time.sleep(1)

        print("Waiting for button...")
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='View Details']")))

        print("Button found. Clicking...")
        button.click()

        # Проверка URL
        product_id = button.get_attribute("data-id")
        expected_url = f"http://localhost:8000/web/products/{product_id}/"
        self.assertEqual(self.driver.current_url, expected_url)
        print("Test passed!")

if __name__ == "__main__":
    unittest.main()