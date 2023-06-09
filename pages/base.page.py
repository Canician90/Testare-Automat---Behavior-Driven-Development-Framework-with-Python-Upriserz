from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import unittest




class BasePage (Browser, unittest.TestCase):

    def wait_for_elem(self, xpath_selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(By.XPATH, selector))

        def browser_back(self):
            self.driver.back()
        def alert_ok(self):
            sleep(2)
            self.driver.switch_to.alert.accept()

            def refresh_page(self):
                sleep( 2 )
                self.driver.refresh()



