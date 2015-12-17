# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.common.exceptions import WebDriverException, NoSuchWindowException  # TimeoutException


def click(self, selector, do_not_wait=False):
    if not do_not_wait:
        element = WebDriverWait(self.browser, self._IMPLICIT_WAIT).until(
                ec.element_to_be_clickable(
                        selector
                )
        )
        element.click()
    else:
        self.browser.find_element(*selector).click()


def enter_text(self, selector, text):
    element = WebDriverWait(self.browser, self._IMPLICIT_WAIT).until(
            EC.visibility_of_element_located(selector))
    element.click()
    element.clear()
    element.send_keys(text)


def wait_for_ajax(self):
    try:
        WebDriverWait(
                self.browser,
                self._IMPLICIT_WAIT
        ).until(
                lambda s: s.execute_script("return jQuery.active == 0")
        )
    except WebDriverException:
        pass


def get_element(self, selector, multiple=False):
    if multiple:
        elements = WebDriverWait(self.browser, self._IMPLICIT_WAIT).until(
                EC.presence_of_all_elements_located(
                        selector
                )
        )
        return elements
    element = WebDriverWait(self.browser, self._IMPLICIT_WAIT).until(
            EC.presence_of_element_located(
                    selector
            )
    )
    return element


def accept_alert(self, accept=True):
    alert = WebDriverWait(
            self.browser, self._IMPLICIT_WAIT).until(
            EC.alert_is_present()
    )
    if accept:
        alert.accept()
    else:
        alert.dismiss()


def hover(self, selector):
    element = WebDriverWait(self.browser, self._IMPLICIT_WAIT).until(
            EC.presence_of_element_located(selector))
    hover = ActionChains(self.browser).move_to_element(element)
    hover.perform()


def drag_and_drop(self, src_selector, dest_selector):
    source = WebDriverWait(self.browser, self._IMPLICIT_WAIT).until(
            EC.presence_of_element_located(src_selector))
    destination = WebDriverWait(self.browser, self._IMPLICIT_WAIT).until(
            EC.presence_of_element_located(dest_selector))
    drag = ActionChains(self.browser).drag_and_drop(source, destination)
    drag.perform()


# Chrome driver issue for handling widows switches
def switch_to_iframe(self, iframe=None):
    iframe = iframe or self._iframe
    try:
        WebDriverWait(
                self.browser, self._IMPLICIT_WAIT).until(
                EC.frame_to_be_available_and_switch_to_it(iframe)
        )
    except NoSuchWindowException:
        self.browser.switch_to.window(self.browser.window_handles[-1])
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame(self.get_element(iframe))
