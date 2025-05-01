from selenium.webdriver.common.by import By

from Pages.base_page import Page

class LogInPage(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD =(By.ID, 'field')
    CONTINUO_FIELD=(By.CSS_SELECTOR,"a[wized='loginButton']")

    def log_in(self,email,password):
        self.input_text(email,*self.EMAIL_FIELD)
        self.input_text(password,*self.PASSWORD_FIELD)
        self.click(*self.CONTINUO_FIELD)
        print('email',email)
        print('password',password)