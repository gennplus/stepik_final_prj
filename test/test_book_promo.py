import time

import pytest
from .pages.book_page import BookPage


# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
links = [f"{product_base_link}/?promo=offer{index}" for index in range(10)]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    # GIVEN
    page = BookPage(browser, link)
    page.open()

    # WHEN
    book = page.get_title()
    price = page.get_price()
    page.add_to_basket() \
        .solve_quiz_and_get_code()

    # THEN
    assert page.get_notification_messages().__contains__(book) \
           and page.get_notification_messages().__contains__(price), \
        f"notifications should contains book title: {book} and price: {price}"


@pytest.mark.parametrize('link', [f"{product_base_link}/?promo=offer0"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    # GIVEN
    page = BookPage(browser, link)
    page.open()

    # WHEN
    page.add_to_basket() \
        .solve_quiz_and_get_code()

    # THEN
    assert page.should_not_be_success_message(), "Success message is presented, but should not be"


@pytest.mark.parametrize('link', [f"{product_base_link}/?promo=offer0"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    # GIVEN
    page = BookPage(browser, link)
    page.open()

    # WHEN
    page.add_to_basket() \
        .solve_quiz_and_get_code()

    # THEN
    assert page.should_be_disappearing_message(), "Success message not disappeared, but should be"


@pytest.mark.parametrize('link', [f"{product_base_link}/?promo=offer0"])
def test_guest_cant_see_success_message(browser, link):
    # GIVEN
    page = BookPage(browser, link)

    # WHEN
    page.open()

    # THEN
    assert page.should_not_be_success_message(), "Success message is presented, but should not be"
