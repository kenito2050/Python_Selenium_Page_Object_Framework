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
from ScreenObjects.BorrowLoanPage import *
from selenium.webdriver.common.action_chains import ActionChains
from Tests.Environments import *
from Tests.Browsers import *

# T1121 OPERATIONS PORTAL - BORROW LOAN - OPEN POSITIONS panel validation
@pytest.mark.smoke
class TestCRD_T1121():
    @pytest.fixture()
    def setup(self, env, browser):
        selectBrowser(self, browser)
        self.driver.implicitly_wait(30)
        baseURL = "http://wedbush%5c"+vusername+":"+vpassword+"@"+Environments.return_environments(env)
        self.driver.get(baseURL)
        self.driver.maximize_window()

    def test_QTML_T1121(self, setup):
        tc_name = "T1121"
        time.sleep(3)
        action = ActionChains(self.driver)
        try:
            verifyheader = self.driver.find_element_by_xpath(LoginPage.header).is_displayed()
            assert verifyheader == True
            verifyheader1 = self.driver.find_element_by_link_text(BorrowLoanPage.borrowloan_header).is_displayed()
            assert verifyheader1 == True
            screenshot("pass", tc_name + "_1")
            borrowLoan = self.driver.find_element_by_link_text(LoginPage.borrowloan_header)
            action.move_to_element(borrowLoan).perform()
            self.driver.find_element_by_link_text(BorrowLoanPage.OpenPositions_header).click()
            time.sleep(3)
            screenshot("pass", tc_name + "_2")
            self.driver.find_element_by_id(BorrowLoanPage.ReportDate).click()
            self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            #self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            #self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            self.driver.find_element_by_link_text("9").click()
            self.driver.find_element_by_id(BorrowLoanPage.SearchButton).click()
            time.sleep(12)
            screenshot("pass",tc_name + "_3")
            verifyheader1 = self.driver.find_element_by_xpath(BorrowLoanPage.SettleDate_header_5).is_displayed()
            assert verifyheader1 == True
            settledate = self.driver.find_element_by_xpath(BorrowLoanPage.SettleDate_element_5).text
            verifydate = checkvaliddateformat2(settledate)
            assert verifydate == True
            verifyheader2 = self.driver.find_element_by_xpath(BorrowLoanPage.DTC_header_5).is_displayed()
            assert verifyheader2 == True
            lengthDTC = len(self.driver.find_element_by_xpath(BorrowLoanPage.DTC_element_5).text)
            assert lengthDTC == 4
            verifyheader3 = self.driver.find_element_by_xpath(BorrowLoanPage.Cusip_header_5).is_displayed()
            assert verifyheader3 == True
            lengthCusip = len(self.driver.find_element_by_xpath(BorrowLoanPage.Cusip_element_5).text)
            assert lengthCusip == 9
            verifyheader4 = self.driver.find_element_by_xpath(BorrowLoanPage.SecurityNmbr_header_5).is_displayed()
            assert verifyheader4 == True
            lengthSN = len(self.driver.find_element_by_xpath(BorrowLoanPage.SecurityNmbr_element_5).text)
            assert lengthSN == 7
            verifyheader5 = self.driver.find_element_by_xpath(BorrowLoanPage.SecType_header_5).is_displayed()
            assert verifyheader5 == True
            verifyheader6 = self.driver.find_element_by_xpath(BorrowLoanPage.Description_header_5).is_displayed()
            assert verifyheader6 == True
            verifyheader7 = self.driver.find_element_by_xpath(BorrowLoanPage.Rate_header_5).is_displayed()
            assert verifyheader7 == True
            validatepercentageformat(self.driver.find_element_by_xpath(BorrowLoanPage.Rate_element_5).text)
            verifyheader8 = self.driver.find_element_by_xpath(BorrowLoanPage.Type_header_5).is_displayed()
            assert verifyheader8 == True
            verifyheader9 = self.driver.find_element_by_xpath(BorrowLoanPage.Quantity_header_5).is_displayed()
            assert verifyheader9 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.Quantity_element_5).text)
            verifyheader10 = self.driver.find_element_by_xpath(BorrowLoanPage.ContraName_header_5).is_displayed()
            assert verifyheader10 == True
            verifyheader11 = self.driver.find_element_by_xpath(BorrowLoanPage.ContraParty_header_5).is_displayed()
            assert verifyheader11 == True
            lengthContraP = len(self.driver.find_element_by_xpath(BorrowLoanPage.ContraParty_element_5).text)
            assert lengthContraP == 4
            self.driver.close()
        except:
            screenshot("fail",tc_name)
            self.driver.close()
            raise




