from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):  

    SEARCH = (By.XPATH, "//input[@id='q']")
