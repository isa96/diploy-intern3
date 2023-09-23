import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver.exe')  

    def test_1_flow_login_account(self):
        #Open Website
        browser = self.browser
        browser.get("https://app.jubelio.com/login")
        browser.maximize_window()
        time.sleep(3)

        #input email
        browser.find_element(By.NAME,"email").send_keys("qa.rakamin.jubelio@gmail.com")
        #input password
        browser.find_element(By.NAME,"password").send_keys("Jubelio123!")
        #login
        browser.find_element(By.XPATH,"//div[@id='root']/div[@class='content']/div[@class='full-height']//form[@class='login-form m-t']/button[@type='submit']").click()
        time.sleep(3)
    
        #Response message text "Dashboard" in website
        response_message = browser.find_element(By.XPATH,"//div[@id='page-wrapper']/div[2]/div[@class='col-lg-12']//h1[.='Selamat Datang']").text
        self.assertEqual(response_message, 'Selamat Datang')
        time.sleep(2)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()