from .base_page import BasePage
from .locators import BookPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class BookPage(BasePage):

    def get_price(self):
        return self.browser.find_element(*BookPageLocators.PRICE).text

    def get_title(self):
        return self.browser.find_element(*BookPageLocators.TITLE).text

    def get_notification_messages(self):
        return " ".join([str(notification.text) for notification in self.browser.find_elements(*BookPageLocators.NOTIFICATIONS)])

    def add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*BookPageLocators.ADD_TO_BASKET_LINK)
        add_to_basket_link.click()
        return self

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        return self

    def should_not_be_success_message(self):
        return self.is_not_element_present(*BookPageLocators.NOTIFICATIONS)


    def should_be_disappearing_message(self):
        return self.is_disappeared(*BookPageLocators.NOTIFICATIONS)

