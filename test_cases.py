from methods import UrbanRoutesPage
from locators import Localizadores
import data
from selenium import webdriver


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.methods_page = UrbanRoutesPage (cls.driver)
        cls.locators_page = Localizadores

    #Set route
    def test_set_route(self):
        from_address = data.address_from
        to_address = data.address_to
        self.methods_page.set_from(from_address)
        self.methods_page.set_to(to_address)
        assert self.methods_page.get_from() == data.address_from
        assert self.methods_page.get_to() == data.address_to


    # Select Comfort option
    def test_select_comfort_option(self):
        self.methods_page.select_comfort_option()



    # Fill in phone number
    def test_fill_in_phone_numer(self):
        self.methods_page.fill_in_phone_number()


    # Add credit card
    def test_add_credit_card(self):
        self.methods_page.add_credit_card()


    # Write a message to the driver
    def test_write_a_message(self):
        self.methods_page.write_a_message()


    # Ask for blanket and kleenex
    def test_asf_for_blanket_and_kleenex(self):
        self.methods_page.ask_for_blanket_and_kleenex()


    # Add icecream
    def test_add_icecream(self):
        self.methods_page.add_two_icecream()



    # Book taxi
    def test_book_taxi(self):
        self.methods_page.book_taxi()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
