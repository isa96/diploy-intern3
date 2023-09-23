import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ControlStock(unittest.TestCase):
        
    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver.exe')  
    
    def test_2_Control_Inventory_Stock(self):
        #Open website 
        browser = self.browser
        browser.get("https://app.jubelio.com/login")
        browser.maximize_window()
        time.sleep(2)

        #Login Account
        browser.find_element(By.NAME,"email").send_keys("qa.rakamin.jubelio@gmail.com")
        browser.find_element(By.NAME,"password").send_keys("Jubelio123!")
        browser.find_element(By.XPATH,"//div[@id='root']/div[@class='content']/div[@class='full-height']//form[@class='login-form m-t']/button[@type='submit']").click()
        time.sleep(3)
    
        #open Barang
        browser.find_element(By.XPATH,"//div[@id='wrapper']/nav[@class='navbar-default navbar-static-side']//div[@class='metismenu nav']/ul[@class='metismenu-container']/li[2]/a[@href='#']").click()
        time.sleep(1)
        #open Persediaan
        browser.find_element(By.XPATH,"//div[@id='wrapper']/nav[@class='navbar-default navbar-static-side']//div[@class='metismenu nav']/ul[@class='metismenu-container']//ul[@class='metismenu-container visible']//a[@href='/home/inventory']/span[.='Persediaan']").click()
        time.sleep(3)

        #Select product in menu persediaan
        browser.find_element(By.XPATH,"//div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div[2]/div/div[@class='row']/div[@class='col-lg-12']/div[@class='ibox']/div[@class='ibox-content']//div[@class='react-grid-Container']/div[@class='react-grid-Main']/div[@class='react-grid-Grid']//div[@class='react-grid-Viewport']/div[@class='react-grid-Canvas']/div[2]/div[1]/div[@class='react-grid-Row react-grid-Row--even']/div[@value='false']//label[@class='react-grid-checkbox-label']").click()
        time.sleep(2)
        #Select penyesuaian persediaan button
        browser.find_element(By.XPATH,"//div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div[2]/div/div[@class='row']/div[@class='col-lg-12']/div[@class='ibox']/div[@class='ibox-content']/div[@class='row']//div[@class='pull-right']/button[2]/span[@class='ladda-label']").click()
        time.sleep(2)
        #Add stock to selected product
        browser.find_element(By.XPATH,"//div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div[2]/div/div[@class='row']/div[@class='col-lg-12']/div[@class='page-editor']//div[@class='form-horizontal']/div[2]/div[@class='col-md-12']//div[@class='react-grid-Container']/div[@class='react-grid-Main']/div[@class='react-grid-Grid']//div[@class='react-grid-Viewport']/div[@class='react-grid-Canvas']//div[@class='react-grid-Row react-grid-Row--even']/div[@value='false']//div[@class='react-grid-checkbox-container']").click()
        time.sleep(2)

        #Get element
        element = browser.find_element(By.XPATH,"//div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div[2]/div/div[@class='row']/div[@class='col-lg-12']/div[@class='page-editor']//div[@class='form-horizontal']/div[2]/div[@class='col-md-12']//div[@class='react-grid-Container']//div[@class='react-grid-Grid']//div[@class='react-grid-Viewport']/div[@class='react-grid-Canvas']/div[2]/div[1]/div/div[2]/div[@class='react-grid-Cell__value']")
        #Create action chain object
        action = ActionChains(browser)
        #Double click the item
        action.double_click(on_element = element)
        # perform the operation
        action.perform()        

        #Add 10 product to system
        browser.find_element(By.XPATH,"//body[@id='page-top']//div[@class='rdg-editor-container']/input").send_keys("10")
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div[2]/div/div[@class='row']/div[@class='col-lg-12']/div[@class='page-editor']//div[@class='form-horizontal']/div[2]/div[@class='col-md-12']//div[@class='react-grid-Container']//div[@class='react-grid-Grid']//div[@class='react-grid-Viewport']/div[@class='react-grid-Canvas']//div[@class='react-grid-Row react-grid-Row--odd']/div[2]/div[@class='react-grid-Cell__value']").click()
        time.sleep(1)

        #Save
        browser.find_element(By.XPATH,"//div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div[2]/div/div[@class='row']/div[@class='col-lg-12']/div[@class='page-editor']/div[3]/div/button[@type='button']").click()
        time.sleep(3)

        #Response message
        response_message = browser.find_element(By.XPATH,"//div[@id='root']//div[@role='alert']/li[.='Data berhasil disimpan.']").text
        self.assertEqual(response_message, 'Data berhasil disimpan.')

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()
