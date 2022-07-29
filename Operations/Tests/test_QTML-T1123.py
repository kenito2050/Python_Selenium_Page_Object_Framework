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

# T1123 OPERATIONS PORTAL - BORROW LOAN - BORROW SUMMARY BY CONTRA PARTY panel validation
@pytest.mark.smoke
class TestCRD_T1123():
    @pytest.fixture()
    def setup(self, env, browser):
        selectBrowser(self, browser)
        self.driver.implicitly_wait(30)
        baseURL = "http://wedbush%5c"+vusername+":"+vpassword+"@"+Environments.return_environments(env)
        self.driver.get(baseURL)
        self.driver.maximize_window()

    def test_QTML_T1123(self, setup):
        tc_name = "T1123"
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
            self.driver.find_element_by_link_text(BorrowLoanPage.BorrowSummary_header).click()
            time.sleep(3)
            screenshot("pass", tc_name + "_2")
            self.driver.find_element_by_id(BorrowLoanPage.ReportDate).click()
            self.driver.find_element_by_id(BorrowLoanPage.ReportDate).clear()
            self.driver.find_element_by_id(BorrowLoanPage.ReportDate).send_keys("01/01/2022")
            self.driver.find_element_by_id(BorrowLoanPage.ReportDate).send_keys(Keys.TAB)
            # self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            # self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            # self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            # self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            # self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            # self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            # self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            # self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            # self.driver.find_element_by_link_text("9").click()
            self.driver.find_element_by_id(BorrowLoanPage.SearchButton).click()
            time.sleep(50)
            screenshot("pass",tc_name + "_3")
            verifyheader1 = self.driver.find_element_by_id(BorrowLoanPage.ReportDate_header_7).is_displayed()
            assert verifyheader1 == True
            reportdate = self.driver.find_element_by_id(BorrowLoanPage.ReportDate_element_7).text
            verifydate = checkvaliddateformat(reportdate)
            assert verifydate == True
            verifyheader2 = self.driver.find_element_by_id(BorrowLoanPage.Account_header_7).is_displayed()
            assert verifyheader2 == True
            lengthDTC = len(self.driver.find_element_by_id(BorrowLoanPage.Account_element_7).text)
            assert lengthDTC == 4
            verifyheader3 = self.driver.find_element_by_id(BorrowLoanPage.ContraParty_header_7).is_displayed()
            assert verifyheader3 == True
            verifyheader4 = self.driver.find_element_by_id(BorrowLoanPage.BorrowCount_header_7).is_displayed()
            assert verifyheader4 == True
            validatenumericformat(self.driver.find_element_by_id(BorrowLoanPage.BorrowCount_element_7).text)
            verifyheader5 = self.driver.find_element_by_id(BorrowLoanPage.ContractAmmount_header_7).is_displayed()
            assert verifyheader5 == True
            validatecurrencyformat(self.driver.find_element_by_id(BorrowLoanPage.ContractAmmount_element_7).text)
            verifyheader6 = self.driver.find_element_by_id(BorrowLoanPage.BorrowCharges_header_7).is_displayed()
            assert verifyheader6 == True
            validatecurrencyformat(self.driver.find_element_by_id(BorrowLoanPage.BorrowCharges_element_7).text)
            verifyheader7 = self.driver.find_element_by_id(BorrowLoanPage.AvgRate_header_7).is_displayed()
            assert verifyheader7 == True
            validatepercentageformat(self.driver.find_element_by_id(BorrowLoanPage.AvgRate_element_7).text)
            verifyheader8 = self.driver.find_element_by_id(BorrowLoanPage.MaxRate_header_7).is_displayed()
            assert verifyheader8 == True
            validatepercentageformat(self.driver.find_element_by_id(BorrowLoanPage.MaxRate_element_7).text)
            verifyheader9 = self.driver.find_element_by_id(BorrowLoanPage.MinRate_header_7).is_displayed()
            assert verifyheader9 == True
            validatepercentageformat(self.driver.find_element_by_id(BorrowLoanPage.MinRate_element_7).text)
            self.driver.quit()
        except:
            screenshot("fail",tc_name)
            self.driver.quit()
            raise




