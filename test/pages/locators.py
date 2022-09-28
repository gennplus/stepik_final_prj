from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")


class BookPageLocators:
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    TITLE = (By.CSS_SELECTOR, "div.product_main h1")
    NOTIFICATIONS = (By.CSS_SELECTOR, "div.alertinner")
    BASKET_NOTIFICATION = (By.CSS_SELECTOR, "div.btn-add-to-basket")
