import pyautogui
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, re
import datetime
from Tests.Config import *


def login(driver, user, passw):
    try:
        if driver.find_element_by_id("account"):
            driver.find_element_by_id("account").click()
            driver.find_element_by_id("account").clear()
            driver.find_element_by_id("account").send_keys(user)
        if driver.find_element_by_id("password"):
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys(passw)
    except:
        myScreenshot = pyautogui.screenshot()
        screenshot_name = "FAIL_login.png"
        #screenshot_path = r'C:\CRDLogs\'' + screenshot_name
        screenshot_path = "..\\Logs\\" + screenshot_name
        myScreenshot.save(screenshot_path)
        driver.close()
        raise

def click_login_button(driver):
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(3)

def logout(driver):
    driver.find_element_by_xpath("//span/div").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div/div/div/div/div/div/div/button").click()
    time.sleep(2)
    try:
        headlogout = driver.find_element_by_xpath("//h4/div").text
        assert headlogout == "Welcome"
    except:
        myScreenshot = pyautogui.screenshot()
        screenshot_name = "FAIL_logout.png"
        #screenshot_path = r'C:\CRDLogs\'' + screenshot_name
        screenshot_path = "..\\Logs\\" + screenshot_name
        myScreenshot.save(screenshot_path)
        driver.close()
        raise


def screenshot(result, tc_name):
    myScreenshot = pyautogui.screenshot()
    if result == "pass":
        screenshot_name = "PASSED" + "_" + tc_name + ".png"
    else:
        screenshot_name = "FAILED" + "_" + tc_name + ".png"
    #screenshot_path = r'C:\CRDLogs\'' + screenshot_name
    screenshot_path = "..\\Logs\\" + screenshot_name
    myScreenshot.save(screenshot_path)

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def clear_text(element):
    length = len(element.get_attribute('value'))
    element.send_keys(length * Keys.BACKSPACE)

def checkvaliddateformat(datestr):

  month,day,year = datestr.split('/')
  isValidDate = True
  try :
       datetime.datetime(int(year),int(month),int(day))
  except ValueError :
       isValidDate = False

  if(isValidDate) :
      return True
  else :
      return False

def checkvaliddateformat2(datestr):

  day,month,year = datestr.split('-')
  isValidDate = True
  try :
       datetime.datetime(int(year),int(month),int(day))
  except ValueError :
       isValidDate = False

  if(isValidDate) :
      return True
  else :
      return False

def checkvaliddateformat3(datestr):

  month,day,year = datestr.split('-')
  isValidDate = True
  try :
       datetime.datetime(int(year),int(month),int(day))
  except ValueError :
       isValidDate = False

  if(isValidDate) :
      return True
  else :
      return False

def checkvaliddateformat4(datestr):

  year,month,day = datestr.split('/')
  isValidDate = True
  try :
       datetime.datetime(int(year),int(month),int(day))
  except ValueError :
       isValidDate = False

  if(isValidDate) :
      return True
  else :
      return False

def validatenumericformat(element):
    matched = re.search("[0-9]+(,[0-9]+)*", element)
    assert bool(matched) == True

def validatedecimalformat(element):
    matched = re.search("[0-9]+(.[0-9]+)*", element)
    assert bool(matched) == True

def validatedecimalformatcurr(element):
    matched = re.search("\D[0-9]+(.[0-9]+)*", element)
    assert bool(matched) == True

def validatecurrencyformat(element):
    matched = re.search("\D[0-9]+(,[0-9]+)*", element)
    assert bool(matched) == True

def validatepercentageformat(element):
    matched = re.search("[0-9]+(.[0-9]+)\s\D", element)
    assert bool(matched) == True

def validatepercentageformat2(element):
    matched = re.search("[0-9]+(.[0-9]+)\D", element)
    assert bool(matched) == True

def validatepercentageformat3(element):
    matched = re.search("[0-9]+(.[0-9][0-9]+)\D", element)
    assert bool(matched) == True

def selectBrowser(self, browser):
    if browser == "CHROME":
        self.driver = webdriver.Chrome(executable_path=pathchrome)
        #self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    if browser == "EDGE":
        self.driver = webdriver.Edge(executable_path=pathedge)
    if browser == "FIREFOX":
        self.driver = webdriver.Firefox(executable_path=pathfirefox)
        #profile = webdriver.FirefoxProfile()
        #profile.set_preference('network.http.phishy-userpass-length', 255)
        #profile.set_preference("network.automatic-ntlm-auth.trusted-uris", "operations.wedbush.com")
        #self.driver = webdriver.Firefox(executable_path=pathfirefox, firefox_profile=profile)
    if browser == "IE":
        options = webdriver.IeOptions()
        options.file_upload_dialog_timeout = 2000
        options.native_events = False
        options.ignore_protected_mode_settings = True
        options.ignore_zoom_level = True
        options.add_argument('-private')
        self.driver = webdriver.Ie(options=options, executable_path=pathie)
    return self

