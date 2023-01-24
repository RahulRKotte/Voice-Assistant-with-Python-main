from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class video():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service("/Users/rohankumar/Downloads/chromedriver"))

    def play(self, query):
        self.query = query
        self.driver.get(url = "https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]")
        video.click()

