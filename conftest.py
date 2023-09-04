import pytest
import selenium

from selenium import webdriver

@pytest.fixture(params =["chrome","ChromiumEdge"])
def setup_and_teardown(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "ChromiumEdge":
        driver = webdriver.ChromiumEdge()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()