from locators import Localizadores
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data
from retrieve import retrieve_phone_code


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = Localizadores()

    #Set route
    def set_from(self, from_address):
         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locators.from_field))
         self.driver.find_element(*self.locators.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.locators.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)


    #Select Comfort option
    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.order_taxi_button))
        self.driver.find_element(*self.locators.order_taxi_button).click()

    def click_comfort_option(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.comfort_option))
        self.driver.find_element(*self.locators.comfort_option).click()

    def select_comfort_option(self):
        self.click_order_taxi_button()
        self.click_comfort_option()



    #Fill in phone number
    def click_phone_number_option(self):
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(self.locators.phone_number_option))
        self.driver.find_element(*self.locators.phone_number_option).click()

    def add_phone_number(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locators.phone_number_field))
        self.driver.find_element(*self.locators.phone_number_field).send_keys(data.phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.locators.next_button_phone_number).click()

    def add_sms_code(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.locators.sms_code_field))
        code = retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*self.locators.sms_code_field).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.locators.confirm_button).click()

    def fill_in_phone_number(self):
        self.click_phone_number_option()
        self.add_phone_number()
        self.click_next_button()
        self.add_sms_code()
        self.click_confirm_button()


    #Add credit card
    def click_payment_method_option(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.payment_method_option))
        self.driver.find_element(*self.locators.payment_method_option).click()

    def add_payment_method_button(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.add_payment_method_button))
        self.driver.find_element(*self.locators.add_payment_method_button).click()

    def insert_card_number(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locators.card_number_field))
        self.driver.find_element(*self.locators.card_number_field).send_keys(data.card_number)

    def insert_card_code(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locators.code_card_field))
        self.driver.find_element(*self.locators.code_card_field).send_keys(data.card_code)

    def tab_empty_rectangle(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.empty_rectangle))
        self.driver.find_element(*self.locators.empty_rectangle).click()

    def click_add_button(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.add_button))
        self.driver.find_element(*self.locators.add_button).click()

    def close_window(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.close_window_button))
        self.driver.find_element(*self.locators.close_window_button).click()

    def add_credit_card(self):
        self.click_payment_method_option()
        self.add_payment_method_button()
        self.insert_card_number()
        self.insert_card_code()
        self.tab_empty_rectangle()
        self.click_add_button()
        self.close_window()


    #Write a message to the driver
    def add_message(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locators.driver_message_button))
        self.driver.find_element(*self.locators.driver_message_button).send_keys(data.message_for_driver)

    def write_a_message(self):
        self.add_message()


    #Ask for blanket and kleenex
    def ask_for_blanket_kleenex(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.ask_blanket_and_kleenex_slider))
        self.driver.find_element(*self.locators.ask_blanket_and_kleenex_slider).click()

    def ask_for_blanket_and_kleenex(self):
        self.ask_for_blanket_kleenex()


    #Add icecream
    def add_icecream(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.add_icecream_counter))
        self.driver.find_element(*self.locators.add_icecream_counter).click()

    def add_more_icecream(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.add_icecream_counter))
        self.driver.find_element(*self.locators.add_icecream_counter).click()

    def add_two_icecream(self):
        self.add_icecream()
        self.add_more_icecream()


    #Book taxi
    def click_book_taxi(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.book_button))
        self.driver.find_element(*self.locators.book_button).click()

    def book_taxi(self):
        self.click_book_taxi()