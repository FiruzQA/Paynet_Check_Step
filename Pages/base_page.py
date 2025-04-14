from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def open_messages(self):
        wait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "LOCATOR"))).click()

    def element_is_visible(self, locator, timeout=30):
        return wait(self._driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=10):
        return wait(self._driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=10):
        return wait(self._driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=10):
        return wait(self._driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=10):
        return wait(self._driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self._driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self._driver.execute_script("arguments[0].scrollIntoView;", element)


class GestureUtils:
    def __init__(self, driver):
        self._driver = driver
        self.finger = PointerInput(PointerInput.TOUCH, "finger")

    def _perform_scroll(self, start_x, start_y, end_x, end_y, duration=0.2):
        actions = ActionBuilder(self._driver, mouse=self.finger)
        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(duration)
        actions.pointer_action.move_to_location(end_x, end_y)
        actions.pointer_action.pointer_up()
        actions.perform()
        actions.clear_actions()

    def scroll_down(self):
        size = self._driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.7)
        end_y = int(size['height'] * 0.3)
        self._perform_scroll(start_x, start_y, start_x, end_y)

    def scroll_left(self):
        size = self._driver.get_window_size()
        start_y = size['height'] // 2
        start_x = int(size['width'] * 0.8)
        end_x = int(size['width'] * 0.2)
        self._perform_scroll(start_x, start_y, end_x, start_y)

    def scroll_right(self):
        size = self._driver.get_window_size()
        start_y = size['height'] // 2
        start_x = int(size['width'] * 0.2)
        end_x = int(size['width'] * 0.8)
        self._perform_scroll(start_x, start_y, end_x, start_y)

    def swipe_up(self):
        size = self._driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.7)
        end_y = int(size['height'] * 0.3)
        self._perform_scroll(start_x, start_y, start_x, end_y)

    def touch_scroll_down(self, element: WebElement):
        location = element.location
        size = element.size
        start_x = location['x'] + size['width'] // 2
        start_y = location['y'] + int(size['height'] * 0.8)
        end_y = location['y'] + int(size['height'] * 0.2)
        self._perform_scroll(start_x, start_y, start_x, end_y)

    def tap_element(self, element: WebElement):
        location = element.location
        size = element.size
        center_x = location['x'] + size['width'] // 2
        center_y = location['y'] + size['height'] // 2

        actions = ActionBuilder(self._driver, mouse=self.finger)
        actions.pointer_action.move_to_location(center_x, center_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(0.05)
        actions.pointer_action.pointer_up()
        actions.perform()
        actions.clear_actions()

    def long_press(self, element: WebElement, duration=1.0):
        location = element.location
        size = element.size
        center_x = location['x'] + size['width'] // 2
        center_y = location['y'] + size['height'] // 2

        actions = ActionBuilder(self._driver, mouse=self.finger)
        actions.pointer_action.move_to_location(center_x, center_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(duration)
        actions.pointer_action.pointer_up()
        actions.perform()
        actions.clear_actions()
