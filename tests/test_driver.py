from appium import webdriver
from appium.options.android import UiAutomator2Options


def test_open_app():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    driver.quit()