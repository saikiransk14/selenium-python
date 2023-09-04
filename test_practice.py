import time

import pytest
import selenium
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")

class Testpractice:

    def test_search_valid_product(self):
        self.driver.find_element(By.NAME,"search").send_keys("hp")
        self.driver.find_element(By.XPATH,"//*[@id='search']/span").click()
        assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(),name="test_search_valid_product",attachment_type=AttachmentType.PNG)
