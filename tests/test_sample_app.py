import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.vehicle_data_page import VehicleDataPage
from pages.insurant_data_page import InsurantDataPage
from utils.screenshots import take_screenshot
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from time import sleep


class SampleAppTest(unittest.TestCase):
    
    def setUp(self):
        # Initialize the Chrome WebDriver using WebDriver Manager
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("http://sampleapp.tricentis.com/101/app.php")

    def test_fill_forms(self):
        vehicle_page = VehicleDataPage(self.driver)

        # Calculate a future date (10 days from today)
        future_date = (datetime.now() + timedelta(days=10)).strftime("%m/%d/%Y")

        # Locate the Date of Manufacture input field, clear it, and enter the future date
        date_input = vehicle_page.driver.find_element(
            *vehicle_page.date_of_manufacture_input
        )
        date_input.clear()
        date_input.send_keys(future_date)

        # Locate the parent element of the Date of Manufacture input field
        parent_element = date_input.find_element(By.XPATH, "..")

        # Get the classes of the parent element
        parent_classes = parent_element.get_attribute("class").split()

        # Assert that the parent element has the 'invalid' class and does not have the 'valid' class
        self.assertIn(
            "invalid",
            parent_classes,
            "Validation failed: The 'invalid' class is not present on the parent element.",
        )
        self.assertNotIn(
            "valid",
            parent_classes,
            "Validation failed: The 'valid' class is present on the parent element.",
        )
        
        # Take a screenshot
        take_screenshot(driver=self.driver, name="date_validation")

        # Clear the Date of Manufacture input field
        vehicle_page.driver.find_element(
            *vehicle_page.date_of_manufacture_input
        ).clear()

        # Locate the Payload input field, clear it, and enter "2000"
        payload_input = vehicle_page.driver.find_element(*vehicle_page.payload_input)
        payload_input.clear()
        payload_input.send_keys("2000")
        
        # Locate the parent element of the Payload input field
        parent_element = payload_input.find_element(By.XPATH, "..")

        # Get the classes of the parent element
        parent_classes = parent_element.get_attribute("class").split()

        # Assert that the parent element has the 'invalid' class and does not have the 'valid' class
        self.assertIn(
            "invalid",
            parent_classes,
            "Validation failed: The 'invalid' class is not present on the parent element.",
        )
        self.assertNotIn(
            "valid",
            parent_classes,
            "Validation failed: The 'valid' class is present on the parent element.",
        )
        
        # Take a screenshot
        take_screenshot(driver=self.driver, name="payload_validation")
        
        # Clear the Payload input field again, if necessary
        payload_input.clear()

        # Fill out the rest of the vehicle form and proceed to the next step
        vehicle_page.fill_form()
        
        # Take a screenshot with current datetime and 'VehicleDataPage_form_filled'
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        take_screenshot(driver=self.driver, name="VehicleDataPage_form_filled")
        
        vehicle_page.click_next()

        # Initialize the Insurant Data Page and fill out the form
        insurant_page = InsurantDataPage(self.driver)
        insurant_page.fill_form()
        
        # Take a screenshot
        take_screenshot(driver=self.driver, name="InsurantDataPage_form_filled")
        
        insurant_page.click_next()

    def tearDown(self):
        # Quit the WebDriver and close all associated windows
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
