import data
from locators import Localizadores
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import retrieve




class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = Localizadores()


#Set route
    def set_from(self, address_from):
        self.driver.find_element(*self.locators.from_field).send_keys(data.address_from)

    def set_to(self, address_to):
        self.driver.find_element(*self.locators.to_field).send_keys(data.address_to)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)


#Select comfort option
    def click_button_get_taxi(self):
        self.driver.find_element(*self.locators.button_get_taxi).click()

    def click_ride_comfort(self):
        self.driver.find_element(*self.locators.comfort_button).click()

    def active_comfort(self):
        return self.driver.find_element(*self.locators.blanket_and_tissue_elements_comfort).is_displayed()

    def select_ride_comfort(self):
        self.click_button_get_taxi()
        self.click_ride_comfort()



#Add phone number
    def click_phone_field(self):
        self.driver.find_element(*self.locators.number_field).click()

    def click_add_phone_field(self):
        self.driver.find_element(*self.locators.click_number_input).click()

    def add_phone_number(self, number):
        self.driver.find_element(*self.locators.add_phone).send_keys(number)

    def click_next_button(self):
        self.driver.find_element(*self.locators.next_button).click()

    def add_code_field(self):
        self.driver.find_element(*self.locators.add_code).send_keys(Retrieve.retrieve_phone_code(self.driver))

    def click_button_confirm(self):
        self.driver.find_element(*self.locators.button_confirm).click()

    def write_phone_number_correct(self):
        return self.driver.find_element(*self.locators.number_text).text

    def add_number_phone_field(self, number):
        self.click_phone_field()
        self.click_add_phone_field()
        self.add_phone_number(number)
        self.click_next_button()
        self.add_code_field()
        self.click_button_confirm()


#Add payment method
    def click_payment_method_field(self):
        self.driver.find_element(*self.locators.payment_method_field).click()

    def click_plus_button_card(self):
        self.driver.find_element(*self.locators.button_plus_card).click()

    def add_card_number(self, number_card):
        self.driver.find_element(*self.locators.add_number_card).send_keys(data.card_number)

    def add_card_code(self, code_card):
        self.driver.find_element(*self.locators.add_code_card).send_keys(data.card_code)

    def click_another_place_screen(self):
        self.driver.find_element(*self.locators.rectangle_colors).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.locators.button_add_card_code).click()

    def click_close_payment_method_screen(self):
        self.driver.find_element(*self.locators.button_close_payment_method).click()

    def correct_add_card(self):
        return self.driver.find_element(*self.locators.add_number_card).get_property('value')

    def correct_text_add_card(self):
        return self.driver.find_element(*self.locators.text_card).text

    def add_card_payment_method(self, number_card, code_card):
        self.click_payment_method_field()
        self.click_plus_button_card()
        self.add_card_number(number_card)
        self.add_card_code(code_card)
        self.correct_add_card()
        self.click_another_place_screen()
        self.click_add_card_button()
        self.click_close_payment_method_screen()



    def click_message_driver(self):
        self.driver.find_element(*self.locators.select_message_driver).click()

    def write_message_driver(self, message):
        self.driver.find_element(*self.locators.message_driver_field).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.locators.message_driver_field).get_property('value')

    def send_message_for_driver(self, message):
        self.click_message_driver()
        self.write_message_driver(message)




    def click_select_blanket_tissue(self):
        self.driver.find_element(*self.locators.select_blanket_and_tissue).click()

    def get_blanket_tissue(self):
        return self.driver.find_element(*self.locators.confirm_blanket_and_tissue).is_selected()


    def click_add_first_ice_cream(self):
        self.driver.find_element(*self.locators.add_ice_cream).click()

    def click_add_second_ice_cream(self):
        self.driver.find_element(*self.locators.add_ice_cream).click()

    def set_two_ice_creams(self):
        return self.driver.find_element(*self.locators.select_two_ice_creams).text

    def add_two_ice_creams(self):
        self.click_add_first_ice_cream()
        self.click_add_second_ice_cream()




    def click_search_taxi_button(self):
        self.driver.find_element(*self.locators.search_taxi_button).click()

    def open_search_taxi_screen(self):
        return self.driver.find_element(*self.locators.search_car_screen).is_displayed()

    def open_information_driver_screen(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(self.locators.img_driver))
        return self.driver.find_element(*self.locators.img_driver).is_displayed()