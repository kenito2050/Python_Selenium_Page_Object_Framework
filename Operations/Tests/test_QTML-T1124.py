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

# T1124 OPERATIONS PORTAL - BORROW LOAN - BORROW LOAN TOP SECURITIES panel validation
@pytest.mark.smoke
class TestCRD_T1124():
    @pytest.fixture()
    def setup(self, env, browser):
        selectBrowser(self, browser)
        self.driver.implicitly_wait(30)
        baseURL = "http://wedbush%5c"+vusername+":"+vpassword+"@"+Environments.return_environments(env)
        self.driver.get(baseURL)
        self.driver.maximize_window()

    def test_QTML_T1124(self, setup):
        tc_name = "T1124"
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
            self.driver.find_element_by_link_text(BorrowLoanPage.BorrowLoan_header).click()
            time.sleep(3)
            screenshot("pass", tc_name + "_2")
            self.driver.find_element_by_id(BorrowLoanPage.TradeDate).click()
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
            verifyheader1 = self.driver.find_element_by_xpath(BorrowLoanPage.FileDate_header_8).is_displayed()
            assert verifyheader1 == True
            filedate = self.driver.find_element_by_xpath(BorrowLoanPage.FileDate_element_8).text
            verifydate = checkvaliddateformat(filedate)
            assert verifydate == True
            verifyheader2 = self.driver.find_element_by_link_text(BorrowLoanPage.SecurityNmbr_header_8).is_displayed()
            assert verifyheader2 == True
            lengthSN = len(self.driver.find_element_by_xpath(BorrowLoanPage.SecurityNmbr_element_8).text)
            assert lengthSN == 7
            verifyheader3 = self.driver.find_element_by_link_text(BorrowLoanPage.Symbol_header_8).is_displayed()
            assert verifyheader3 == True
            verifyheader4 = self.driver.find_element_by_link_text(BorrowLoanPage.Cusip_header_8).is_displayed()
            assert verifyheader4 == True
            lengthCusip = len(self.driver.find_element_by_xpath(BorrowLoanPage.Cusip_element_8).text)
            assert lengthCusip == 9
            verifyheader5 = self.driver.find_element_by_link_text(BorrowLoanPage.NumOfDays_header_8).is_displayed()
            assert verifyheader5 == True
            lengthNumDays = len(self.driver.find_element_by_xpath(BorrowLoanPage.NumOfDays_element_8).text)
            assert lengthNumDays == 1
            verifyheader6 = self.driver.find_element_by_link_text(BorrowLoanPage.BorrowQty_header_8).is_displayed()
            assert verifyheader6 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.BorrowQty_element_8).text)
            verifyheader7 = self.driver.find_element_by_link_text(BorrowLoanPage.Price_header_8).is_displayed()
            assert verifyheader7 == True
            validatecurrencyformat(self.driver.find_element_by_xpath(BorrowLoanPage.Price_element_8).text)
            verifyheader8 = self.driver.find_element_by_link_text(BorrowLoanPage.Rate_header_8).is_displayed()
            assert verifyheader8 == True
            validatecurrencyformat(self.driver.find_element_by_xpath(BorrowLoanPage.Rate_element_8).text)
            verifyheader9 = self.driver.find_element_by_link_text(BorrowLoanPage.BorrowAmt_header_8).is_displayed()
            assert verifyheader9 == True
            validatecurrencyformat(self.driver.find_element_by_xpath(BorrowLoanPage.BorrowAmt_element_8).text)
            verifyheader10 = self.driver.find_element_by_link_text(BorrowLoanPage.Rebate_header_8).is_displayed()
            assert verifyheader10 == True
            validatecurrencyformat(self.driver.find_element_by_xpath(BorrowLoanPage.Rebate_element_8).text)
            verifyheader2 = self.driver.find_element_by_link_text(BorrowLoanPage.MinDelDate_header_8).is_displayed()
            assert verifyheader2 == True
            deliverydate = self.driver.find_element_by_xpath(BorrowLoanPage.MinDelDate_element_8).text
            verifydate = checkvaliddateformat(deliverydate)
            assert verifydate == True
            self.driver.quit()
        except:
            screenshot("fail",tc_name)
            self.driver.quit()
            raise




