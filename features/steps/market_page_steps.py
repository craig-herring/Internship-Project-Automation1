from time import sleep
from behave import When, Then
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as ec
#from time import sleep

@Then ('Go to final page using pagination')
def page_forward(context):
    for _ in range(7):
        context.app.reelly_main_page.page_forward()
        sleep(4)

@Then('Go to first page using pagination')
def page_back(context):
    for _ in range(7):
        context.app.reelly_main_page.page_back()
        sleep(4)