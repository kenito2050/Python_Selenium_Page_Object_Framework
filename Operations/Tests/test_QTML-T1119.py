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

# T1119 OPERATIONS PORTAL - BORROW LOAN - OPEN CONTRACTS panel validation
@pytest.mark.smoke
class TestCRD_T1119():
    @pytest.fixture()
    def setup(self, env, browser):
        selectBrowser(self, browser)
        self.driver.implicitly_wait(30)
        baseURL = "http://wedbush%5c"+vusername+":"+vpassword+"@"+Environments.return_environments(env)
        self.driver.get(baseURL)
        self.driver.maximize_window()

    def test_QTML_T1119(self, setup):
        tc_name = "T1119"
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
            self.driver.find_element_by_link_text(BorrowLoanPage.OpenContracts_header).click()
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
            self.driver.find_element_by_id(BorrowLoanPage.CusipTxt).click()
            self.driver.find_element_by_id(BorrowLoanPage.CusipTxt).clear()
            self.driver.find_element_by_id(BorrowLoanPage.CusipTxt).send_keys(BorrowLoanPage.CusipAAPL)
            self.driver.find_element_by_id(BorrowLoanPage.SearchButton).click()
            time.sleep(12)
            screenshot("pass",tc_name + "_3")
            verifyheader1 = self.driver.find_element_by_id(BorrowLoanPage.ReportDate_header_3).is_displayed()
            assert verifyheader1 == True
            reportdate = self.driver.find_element_by_id(BorrowLoanPage.ReportDate_element_3).text
            verifydate = checkvaliddateformat(reportdate)
            assert verifydate == True
            verifyheader2 = self.driver.find_element_by_id(BorrowLoanPage.DeliveryDate_header_3).is_displayed()
            assert verifyheader2 == True
            deliverydate = self.driver.find_element_by_id(BorrowLoanPage.DeliveryDate_element_3).text
            verifydate = checkvaliddateformat(deliverydate)
            assert verifydate == True
            verifyheader3 = self.driver.find_element_by_id(BorrowLoanPage.Type_header_3).is_displayed()
            assert verifyheader3 == True
            verifyheader4 = self.driver.find_element_by_id(BorrowLoanPage.DTC_header_3).is_displayed()
            assert verifyheader4 == True
            lengthDTC = len(self.driver.find_element_by_id(BorrowLoanPage.DTC_element_3).text)
            assert lengthDTC == 4
            verifyheader5 = self.driver.find_element_by_id(BorrowLoanPage.Contract_header_3).is_displayed()
            assert verifyheader5 == True
            lengthContract = len(self.driver.find_element_by_id(BorrowLoanPage.Contract_element_3).text)
            assert lengthContract == 9
            verifyheader6 = self.driver.find_element_by_id(BorrowLoanPage.SecurityNmbr_header_3).is_displayed()
            assert verifyheader6 == True
            lengthContract = len(self.driver.find_element_by_id(BorrowLoanPage.SecurityNmbr_element_3).text)
            assert lengthContract == 7
            verifyheader7 = self.driver.find_element_by_id(BorrowLoanPage.Cusip_header_3).is_displayed()
            assert verifyheader7 == True
            lengthCusip = len(self.driver.find_element_by_id(BorrowLoanPage.Cusip_element_3).text)
            assert lengthCusip == 9
            verifyheader8 = self.driver.find_element_by_id(BorrowLoanPage.Symbol_header_3).is_displayed()
            assert verifyheader8 == True
            symbol = self.driver.find_element_by_id(BorrowLoanPage.Symbol_element_3).text
            assert symbol == BorrowLoanPage.CusipAAPL
            verifyheader9 = self.driver.find_element_by_id(BorrowLoanPage.ContraParty_header_3).is_displayed()
            assert verifyheader9 == True
            verifyheader10 = self.driver.find_element_by_id(BorrowLoanPage.PC_header_3).is_displayed()
            assert verifyheader10 == True
            verifyheader11 = self.driver.find_element_by_id(BorrowLoanPage.Quantity_header_3).is_displayed()
            assert verifyheader11 == True
            validatenumericformat(self.driver.find_element_by_id(BorrowLoanPage.Quantity_element_3).text)
            verifyheader12 = self.driver.find_element_by_id(BorrowLoanPage.Price_header_3).is_displayed()
            assert verifyheader12 == True
            validatecurrencyformat(self.driver.find_element_by_id(BorrowLoanPage.Price_element_3).text)
            verifyheader13 = self.driver.find_element_by_id(BorrowLoanPage.Amount_header_3).is_displayed()
            assert verifyheader13 == True
            validatecurrencyformat(self.driver.find_element_by_id(BorrowLoanPage.Amount_element_3).text)
            verifyheader14 = self.driver.find_element_by_id(BorrowLoanPage.Rate_header_3).is_displayed()
            assert verifyheader14 == True
            validatepercentageformat(self.driver.find_element_by_id(BorrowLoanPage.Rate_element_3).text)
            verifyheader15 = self.driver.find_element_by_id(BorrowLoanPage.Rebate_header_3).is_displayed()
            assert verifyheader15 == True
            validatecurrencyformat(self.driver.find_element_by_id(BorrowLoanPage.Rebate_element_3).text)
            self.driver.quit()
        except:
            screenshot("fail",tc_name)
            self.driver.quit()
            raise




