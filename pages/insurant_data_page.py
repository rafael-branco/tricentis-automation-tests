from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class InsurantDataPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "firstname")
        self.last_name_input = (By.ID, "lastname")
        self.date_of_birth_input = (By.ID, "birthdate")
        self.gender_male_radio = (By.XPATH, "//input[@id='gendermale']/..")
        self.street_address_input = (By.ID, "streetaddress")
        self.country_select = (By.ID, "country")
        self.zip_code_input = (By.ID, "zipcode")
        self.city_input = (By.ID, "city")
        self.occupation_select = (By.ID, "occupation")
        self.hobbies_speeding_checkbox = (By.XPATH, "//input[@id='speeding']/..")
        self.next_button = (By.ID, "nextenterproductdata")

    def fill_form(self):
        self.driver.find_element(*self.first_name_input).send_keys("John")
        self.driver.find_element(*self.last_name_input).send_keys("Wick")
        self.driver.find_element(*self.date_of_birth_input).send_keys("01/01/1990")
        self.driver.find_element(*self.gender_male_radio).click()
        self.driver.find_element(*self.street_address_input).send_keys("St ABC, 123")
        Select(self.driver.find_element(*self.country_select)).select_by_visible_text("United States")
        self.driver.find_element(*self.zip_code_input).send_keys("12345678")
        self.driver.find_element(*self.city_input).send_keys("New York")
        Select(self.driver.find_element(*self.occupation_select)).select_by_visible_text("Employee")
        self.driver.find_element(*self.hobbies_speeding_checkbox).click()

    def click_next(self):
        self.driver.find_element(*self.next_button).click()
