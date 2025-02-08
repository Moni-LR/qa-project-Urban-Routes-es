from selenium.webdriver.common.by import By


class Localizadores:
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")

    #Select Comfort option
    order_taxi_button = (By.CLASS_NAME, "button round")
    comfort_option = (By.CSS_SELECTOR,'[src="/static/media/kids.075fd8d4.svg"]')

    #Fill in phone number
    phone_number_option = (By.CLASS_NAME, "np-text")
    phone_number_field = (By.CLASS_NAME, '[for="phone"]')
    next_button_phone_number = (By.XPATH, "//*[text()='Siguiente']")
    sms_code_field = (By.XPATH, "//*[text()='Introduce el código']")
    confirm_button = (By.XPATH, "//*[text()='Confirmar']")

    #Add credit card
    payment_method_option = (By.CLASS_NAME, 'pp-text')
    add_payment_method_button = (By.CLASS_NAME, 'pp-plus-container')
    card_number_field = (By.CSS_SELECTOR, "#number")
    code_card_field = (By.CSS_SELECTOR, "input[name='code']")
    empty_rectangle = (By.CLASS_NAME,"plc")
    add_button = (By.XPATH, "//*[text()='Agregar']")
    close_window_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")

    #Write a message to the driver
    driver_message_button =  (By.XPATH, "//*[text()='Mensaje para el conductor...']")

    #Ask for blanket and kleenex
    ask_blanket_and_kleenex_slider = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")

    #Add icecream
    add_icecream_counter = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')

    #Book taxi
    book_button = (By.CLASS_NAME, "smart-button-secondary")