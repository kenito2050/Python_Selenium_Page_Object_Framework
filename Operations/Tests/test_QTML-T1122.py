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

# T1122 OPERATIONS PORTAL - BORROW LOAN - LOAN SUMMARY BY CONTRA PARTY panel validation
@pytest.mark.smoke
class TestCRD_T1122():
    @pytest.fixture()
    def setup(self, env, browser):
        selectBrowser(self, browser)
        self.driver.implicitly_wait(30)
        baseURL = "http://wedbush%5c"+vusername+":"+vpassword+"@"+Environments.return_environments(env)
        self.driver.get(baseURL)
        self.driver.maximize_window()

    def test_QTML_T1122(self, setup):
        tc_name = "T1122"
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
            self.driver.find_element_by_link_text(BorrowLoanPage.LoanSummary_header).click()
            time.sleep(3)
            screenshot("pass", tc_name + "_2")
            self.driver.find_element_by_id(BorrowLoanPage.ReportDate).click()
            self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            self.driver.find_element_by_link_text("9").click()
            self.driver.find_element_by_id(BorrowLoanPage.SearchButton).click()
            time.sleep(12)
            screenshot("pass",tc_name + "_3")
            verifyheader1 = self.driver.find_element_by_id(BorrowLoanPage.ReportDate_header_6).is_displayed()
            assert verifyheader1 == True
            reportdate = self.driver.find_element_by_id(BorrowLoanPage.ReportDate_element_6).text
            verifydate = checkvaliddateformat(reportdate)
            assert verifydate == True
            verifyheader2 = self.driver.find_element_by_id(BorrowLoanPage.Account_header_6).is_displayed()
            assert verifyheader2 == True
            lengthDTC = len(self.driver.find_element_by_id(BorrowLoanPage.Account_element_6).text)
            assert lengthDTC == 4
            verifyheader3 = self.driver.find_element_by_id(BorrowLoanPage.ContraParty_header_6).is_displayed()
            assert verifyheader3 == True
            verifyheader4 = self.driver.find_element_by_id(BorrowLoanPage.LoanCount_header_6).is_displayed()
            assert verifyheader4 == True
            validatenumericformat(self.driver.find_element_by_id(BorrowLoanPage.LoanCount_element_6).text)
            verifyheader5 = self.driver.find_element_by_id(BorrowLoanPage.ContractAmmount_header_6).is_displayed()
            assert verifyheader5 == True
            validatecurrencyformat(self.driver.find_element_by_id(BorrowLoanPage.ContractAmmount_element_6).text)
            verifyheader6 = self.driver.find_element_by_id(BorrowLoanPage.LoanRebate_header_6).is_displayed()
            assert verifyheader6 == True
            validatecurrencyformat(self.driver.find_element_by_id(BorrowLoanPage.LoanRebate_element_6).text)
            verifyheader7 = self.driver.find_element_by_id(BorrowLoanPage.AvgRate_header_6).is_displayed()
            assert verifyheader7 == True
            validatepercentageformat(self.driver.find_element_by_id(BorrowLoanPage.AvgRate_element_6).text)
            verifyheader8 = self.driver.find_element_by_id(BorrowLoanPage.MaxRate_header_6).is_displayed()
            assert verifyheader8 == True
            validatepercentageformat(self.driver.find_element_by_id(BorrowLoanPage.MaxRate_element_6).text)
            verifyheader9 = self.driver.find_element_by_id(BorrowLoanPage.MinRate_header_6).is_displayed()
            assert verifyheader9 == True
            validatepercentageformat(self.driver.find_element_by_id(BorrowLoanPage.MinRate_element_6).text)
            self.driver.quit()
        except:
            screenshot("fail",tc_name)
            self.driver.quit()
            raise




