# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestOthers():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_others(self):
    print(str("country;tests_cumulative"))
    self.driver.get("https://www.health.gov.au/resources/total-covid-19-tests-conducted-and-results")
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".qv-grid-object-data-first-row > .qv-st-data-cell:nth-child(2) .ng-binding").text
    print(str("Australia;self.vars["tests"]"))
    self.driver.get("http://minzdrav.gov.by/ru/sobytiya/index.php")
    self.driver.find_element(By.CSS_SELECTOR, ".news-list-page:nth-child(1) .event-open").click()
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".paragraph:nth-child(3)").text
    print(str("Belarus;self.vars["tests"]"))
    self.driver.get("https://covid19.moph.gov.qa/EN/Pages/default.aspx#")
    self.vars["tests"] = self.driver.find_element(By.ID, "strgPeopleTested").text
    print(str("Qatar;self.vars["tests"]"))
    self.driver.get("https://covid-19.ba/")
    self.vars["tests"] = self.driver.find_element(By.ID, "total_tested_positive").text
    print(str("Bosnia and Herzegovina;self.vars["tests"]"))
    self.driver.get("https://koronavirus.gov.hu/#aktualis")
    self.vars["tests"] = self.driver.find_element(By.ID, "content-mintavetel").text
    print(str("Hungary;self.vars["tests"]"))
    self.driver.get("https://www.icmr.gov.in/")
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(1) > .single-cool-fact h2").text
    print(str("India;self.vars["tests"]"))
    self.driver.get("https://covid19.ndrrma.gov.np/")
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".styles_info-item_15P0j1vOg4bSCQmNgla5Te:nth-child(7) .number").text
    print(str("Nepal;self.vars["tests"]"))
    self.driver.get("https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases")
    self.driver.find_element(By.LINK_TEXT, "Lab testing").click()
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".table-responsive:nth-child(51) tr:nth-child(3) > td:nth-child(2)").text
    print(str("New Zealand;self.vars["tests"]"))
    self.driver.get("https://www.moh.gov.sg/covid-19")
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder_contentPlaceholder_C095_Col00 b").text
    print(str("Singapore;self.vars["tests"]"))
    self.driver.get("https://infogram.com/covid-19-izplatiba-latvija-1hzj4ozwvnzo2pw")
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".InfographicEditor-Contents-Item:nth-child(11) .igc-textual-figure > div").text
    print(str("Latvia;self.vars["tests"]"))
  
