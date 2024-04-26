import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    ignoreHiddenApiPolicyError= "true",
    noReset="true"



)

appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def setup():
    driver=webdriver.Remote(appium_server_url,options=UiAutomator2Options().load_capabilities(capabilities))
    return driver

