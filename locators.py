from selenium.webdriver.common.by import By


class Localizadores:
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")

    #Select Comfort option
    button_get_taxi = (By.CSS_SELECTOR, ".button.round")
    comfort_button = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg" and @alt="Comfort"]')

    #Fill in phone number
    number_field = (By.CSS_SELECTOR, ".np-button")
    click_number_input = (By.CSS_SELECTOR, ".np-input")
    add_phone = (By.ID, "phone")
    next_button = (By.XPATH, '//*[text()="Siguiente"]')
    code_field = (By.XPATH, '//label[@for="code"]')
    add_code = (By.ID, "code")
    button_confirm = (By.XPATH, '//*[text()="Confirmar"]')
    number_text = (By.CSS_SELECTOR, '.np-text')


    #Add credit card
    payment_method_field = (By.CSS_SELECTOR, ".pp-text")
    button_plus_card = (By.CLASS_NAME, "pp-plus-container")
    add_number_card = (By.ID, "number")
    add_code_card = (By.NAME, "code")
    rectangle_colors = (By.CSS_SELECTOR, ".plc")
    button_add_card_code = (By.XPATH, '//*[text()="Agregar"]')
    button_close_payment_method = (
    By.XPATH, '//div[@class="payment-picker open"]/div[@class="modal"]/div[@class="section active"]/button')
    text_card = (By.CLASS_NAME, "pp-value-text")


    #Write a message to the driver
    select_message_driver = (By.XPATH, '//label[@for="comment" and @class="label"]')
    message_driver_field = (By.ID, "comment")


    #Ask for blanket and kleenex
    blanket_and_tissue_elements_comfort = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]')
    select_blanket_and_tissue = (By.CLASS_NAME, 'r-sw')
    confirm_blanket_and_tissue = (By.CSS_SELECTOR, '.r-sw > div >input')


    #Add icecream
    add_ice_cream = (By.CSS_SELECTOR, '.r-group-items>:nth-child(1)>div>.r-counter>div>.counter-plus')
    select_two_ice_creams = (By.CSS_SELECTOR, '.r-group-items>:nth-child(1)>div>.r-counter>div>.counter-value')


    #Book taxi
    search_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")
    search_car_screen = (By.CSS_SELECTOR, ".order-header-title")
    img_driver = (By.XPATH, '//img[@src="/static/media/bender.e90e5089.svg"]')