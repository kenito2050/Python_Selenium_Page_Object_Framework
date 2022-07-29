import sys
import pyautogui

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from Tests.TestBase import *
from Tests.Config import *
from ScreenObjects.LoginPage import *
from Tests.Environments import *
from Tests.Browsers import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

# T1115 OPERATIONS PORTAL - Accessibility - Log into application
@pytest.mark.smoke
class TestCRD_T1115():
    @pytest.fixture()
    def setup(self, env, browser):
        selectBrowser(self, browser)
        self.driver.implicitly_wait(30)
        baseURL = "http://wedbush%5c"+vusername+":"+vpassword+"@"+Environments.return_environments(env)
        self.driver.get(baseURL)
        time.sleep(2)
        if browser == "FIREFOX":
            alert = Alert(self.driver)
            alert.dismiss()
        print("baseURL = ", baseURL)
        self.driver.maximize_window()

    def test_QTML_T1115(self, setup):
        tc_name = "T1115"
        time.sleep(3)
        try:
            verifyheader = self.driver.find_element_by_xpath(LoginPage.header).is_displayed()
            assert verifyheader == True
            verifyheader1 = self.driver.find_element_by_link_text(LoginPage.borrowloan_header).is_displayed()
            assert verifyheader1 == True
            verifyheader2 = self.driver.find_element_by_link_text(LoginPage.Sttlement_header).is_displayed()
            assert verifyheader2 == True
            verifyheader3 = self.driver.find_element_by_link_text(LoginPage.CSDOperations_header).is_displayed()
            assert verifyheader3 == True
            verifyheader4 = self.driver.find_element_by_link_text(LoginPage.FPL_header).is_displayed()
            assert verifyheader4 == True
            verifyheader5 = self.driver.find_element_by_link_text(LoginPage.Phase3_header).is_displayed()
            assert verifyheader5 == True
            verifyheader6 = self.driver.find_element_by_link_text(LoginPage.Compliance_header).is_displayed()
            assert verifyheader6 == True
            verifyheader7 = self.driver.find_element_by_link_text(LoginPage.Credit_header).is_displayed()
            assert verifyheader7 == True
            verifyheader8 = self.driver.find_element_by_link_text(LoginPage.Accounting_header).is_displayed()
            assert verifyheader8 == True
            verifyheader9 = self.driver.find_element_by_link_text(LoginPage.Phase3FIX_header).is_displayed()
            assert verifyheader9 == True
            verifyheader10 = self.driver.find_element_by_link_text(LoginPage.NewAccounts_header).is_displayed()
            assert verifyheader10 == True
            verifyheader11 = self.driver.find_element_by_link_text(LoginPage.WealthMgmt_header).is_displayed()
            assert verifyheader11 == True
            verifyheader12 = self.driver.find_element_by_link_text(LoginPage.Treasury_header).is_displayed()
            assert verifyheader12 == True
            screenshot("pass",tc_name + "_1")
            self.driver.close()
        except:
            screenshot("fail",tc_name)
            self.driver.close()
            raise




