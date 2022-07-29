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

# T1118 OPERATIONS PORTAL - BORROW LOAN - SMARTLOAN LOAN AVAILABILITY panel validation
@pytest.mark.smoke
class TestCRD_T1118():
    @pytest.fixture()
    def setup(self, env, browser):
        selectBrowser(self, browser)
        self.driver.implicitly_wait(30)
        baseURL = "http://wedbush%5c"+vusername+":"+vpassword+"@"+Environments.return_environments(env)
        self.driver.get(baseURL)
        self.driver.maximize_window()

    def test_QTML_T1118(self, setup):
        tc_name = "T1118"
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
            self.driver.find_element_by_link_text(BorrowLoanPage.SmartLoanLoan_header).click()
            time.sleep(3)
            screenshot("pass", tc_name + "_2")
            self.driver.find_element_by_id(BorrowLoanPage.SettleDate).click()
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
            verifyheader1 = self.driver.find_element_by_id(BorrowLoanPage.SettleDate_header_2).is_displayed()
            assert verifyheader1 == True
            settledate = self.driver.find_element_by_id(BorrowLoanPage.SettleDate_element_2).text
            verifydate = checkvaliddateformat(settledate)
            assert verifydate == True
            verifyheader2 = self.driver.find_element_by_id(BorrowLoanPage.Cusip_header_2).is_displayed()
            assert verifyheader2 == True
            lengthCusip = len(self.driver.find_element_by_id(BorrowLoanPage.Cusip_element_2).text)
            assert lengthCusip == 9
            verifyheader3 = self.driver.find_element_by_id(BorrowLoanPage.Symbol_header_2).is_displayed()
            assert verifyheader3 == True
            verifyheader4 = self.driver.find_element_by_id(BorrowLoanPage.SEcType_header_2).is_displayed()
            assert verifyheader4 == True
            verifyheader5 = self.driver.find_element_by_id(BorrowLoanPage.DTCQty_header_2).is_displayed()
            assert verifyheader5 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.DTCQty_element_2).text)
            verifyheader6 = self.driver.find_element_by_id(BorrowLoanPage.BetatoAvailable_header_2).is_displayed()
            assert verifyheader6 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.BetatoAvailable_element_2).text)
            verifyheader7 = self.driver.find_element_by_id(BorrowLoanPage.SLTotal_header_2).is_displayed()
            assert verifyheader7 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.SLTotal_element_2).text)
            verifyheader8 = self.driver.find_element_by_id(BorrowLoanPage.AvailableDiff_header_2).is_displayed()
            assert verifyheader8 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.AvailableDiff_element_2).text)
            verifyheader9 = self.driver.find_element_by_id(BorrowLoanPage.BetaFirm_header_2).is_displayed()
            assert verifyheader9 == True
            validatenumericformat(self.driver.find_element_by_id(BorrowLoanPage.BetaFirm_element_2).text)
            verifyheader10 = self.driver.find_element_by_id(BorrowLoanPage.BetaCustomer_header_2).is_displayed()
            assert verifyheader10 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.BetaCustomer_element_2).text)
            verifyheader11 = self.driver.find_element_by_id(BorrowLoanPage.SLFirm_header_2).is_displayed()
            assert verifyheader11 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.SLFirm_element_2).text)
            verifyheader12 = self.driver.find_element_by_id(BorrowLoanPage.SLCustomer_header_2).is_displayed()
            assert verifyheader12 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.SLCustomer_element_2).text)
            verifyheader13 = self.driver.find_element_by_id(BorrowLoanPage.SLNonCustomer_header_2).is_displayed()
            assert verifyheader13 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.SLNonCustomer_element_2).text)
            verifyheader14 = self.driver.find_element_by_id(BorrowLoanPage.SLReturn_header_2).is_displayed()
            assert verifyheader14 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.SLReturn_element_2).text)
            self.driver.quit()
        except:
            screenshot("fail",tc_name)
            self.driver.quit()
            raise




