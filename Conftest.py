from appium.webdriver.common.appiumby import AppiumBy
import appium
import pytest

android_caps = {
    "appium:deviceName": "Vivo V23e",
    "platformName": "Android",
    "appium:app": "/Users/firuzkhodjaev/Downloads/app.apk",
    "appium:noReset": True,
    "appium:automationName": "UiAutomator2",
    "appium:ensureWebViewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
}

appium_server_url = 'http://127.0.0.1:4723/wd/hub'


@pytest.fixture()
def mobile_driver():
    driver = appium.webdriver.Remote(appium_server_url, android_caps)
    yield driver
    driver.quit()
