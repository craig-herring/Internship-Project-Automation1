from time import sleep
from behave import Given, When, Then

from selenium.webdriver.common.by import By
#from selenium.webdriver.remote.webelement import WebElement
#,
#from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as ec
#from time import sleep

@Given ('Open the main page')
def open_main_page(context):
    context.app.reelly_main_page.open_main_page()
    sleep(4)

@When ("Enter username")
def username_entry(context):
    context.driver.find_element(By.NAME, 'email-2').send_keys('craigman.herring@gmail.com')

@When ("Type password")
def password_entry(context):
    context.driver.find_element(By.NAME, 'Password').send_keys('1234')
    sleep(3)

@When ("Log in to the page")
def log_in(context):
    context.app.reelly_main_page.log_in()
    sleep(3)

@When ("Click on 'market' on the left side menu")
def open_market(context):
    context.app.reelly_main_page.open_market()
    sleep(4)

@Then ('Verify the right page opens')
def check_pageloop_page(context):
    context.app.pageloop_page.check_pageloop_page()