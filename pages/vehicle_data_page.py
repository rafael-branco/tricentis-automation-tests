from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta


class VehicleDataPage:

    def __init__(self, driver):
        self.driver = driver
        self.make_select = (By.ID, "make")
        self.model_select = (By.ID, "model")
        self.cylinder_capacity_input = (By.ID, "cylindercapacity")
        self.engine_performance_input = (By.ID, "engineperformance")
        self.date_of_manufacture_input = (By.ID, "dateofmanufacture")
        self.number_of_seats_select = (By.ID, "numberofseats")
        self.right_hand_drive_yes = (By.XPATH, "//input[@id='righthanddriveyes']/..")
        self.number_of_seats_motorcycle_select = (By.ID, "numberofseatsmotorcycle")
        self.fuel_type_select = (By.ID, "fuel")
        self.payload_input = (By.ID, "payload")
        self.total_weight_input = (By.ID, "totalweight")
        self.list_price_input = (By.ID, "listprice")
        self.license_plate_number_input = (By.ID, "licenseplatenumber")
        self.annual_mileage_input = (By.ID, "annualmileage")
        self.next_button = (By.ID, "nextenterinsurantdata")
        self.error_messages = (By.CLASS_NAME, "error")

    def fill_form(self):
        Select(self.driver.find_element(*self.make_select)).select_by_visible_text("Audi")
        Select(self.driver.find_element(*self.model_select)).select_by_visible_text("Scooter")
        self.driver.find_element(*self.cylinder_capacity_input).send_keys("1500")
        self.driver.find_element(*self.engine_performance_input).send_keys("1200")
        self.driver.find_element(*self.date_of_manufacture_input).send_keys("10/10/2020")
        Select(self.driver.find_element(*self.number_of_seats_select)).select_by_visible_text("4")
        self.driver.find_element(*self.right_hand_drive_yes).click()
        Select(self.driver.find_element(*self.number_of_seats_motorcycle_select)).select_by_visible_text("1")
        Select(self.driver.find_element(*self.fuel_type_select)).select_by_visible_text("Petrol")
        self.driver.find_element(*self.payload_input).send_keys("1000")
        self.driver.find_element(*self.total_weight_input).send_keys("2000")
        self.driver.find_element(*self.list_price_input).send_keys("30000")
        self.driver.find_element(*self.license_plate_number_input).send_keys("ABC1234")
        self.driver.find_element(*self.annual_mileage_input).send_keys("15000")

    def click_next(self):
        self.driver.find_element(*self.next_button).click()
