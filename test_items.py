import time
from selenium.common.exceptions import NoSuchElementException


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_availability_purchase_button(browser):
    browser.get(link)
    try:
        btns = browser.find_elements_by_css_selector("#add_to_basket_form > button")
        assert len(btns) > 0, "button not found"
        print(btns[0].text)

        # test click if button exist
        btns[0].click()

    except NoSuchElementException:
        print('requested element not found')

    time.sleep(30)