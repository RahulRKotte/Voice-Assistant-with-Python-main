from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service("/Users/rohankumar/Downloads/chromedriver"))

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        self.driver.maximize_window()
        search = self.driver.find_element(By.NAME, "search")
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH, "/html/body/div[3]/form/fieldset/button")
        enter.click()

