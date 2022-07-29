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

# T1116 OPERATIONS PORTAL - BORROW LOAN - BORROW LOAN main menu validation
@pytest.mark.smoke
class TestCRD_T1116():
    @pytest.fixture()
    def setup(self, env, browser):
        selectBrowser(self, browser)
        self.driver.implicitly_wait(30)
        baseURL = "http://wedbush%5c"+vusername+":"+vpassword+"@"+Environments.return_environments(env)
        self.driver.get(baseURL)
        self.driver.maximize_window()

    def test_QTML_T1116(self, setup):
        tc_name = "T1116"
        time.sleep(3)
        action = ActionChains(self.driver)
        try:
            verifyheader = self.driver.find_element_by_xpath(LoginPage.header).is_displayed()
            assert verifyheader == True
            verifyheader1 = self.driver.find_element_by_link_text(BorrowLoanPage.borrowloan_header).is_displayed()
            assert verifyheader1 == True
            borrowLoan = self.driver.find_element_by_link_text(LoginPage.borrowloan_header)
            action.move_to_element(borrowLoan).perform()
            verifyheader2 = self.driver.find_element_by_link_text(BorrowLoanPage.SmartLoanBorrow_header).is_displayed()
            assert verifyheader2 == True
            verifyheader3 = self.driver.find_element_by_link_text(BorrowLoanPage.SmartLoanLoan_header).is_displayed()
            assert verifyheader3 == True
            verifyheader4 = self.driver.find_element_by_link_text(BorrowLoanPage.OpenContracts_header).is_displayed()
            assert verifyheader4 == True
            verifyheader5 = self.driver.find_element_by_link_text(BorrowLoanPage.OpenContractsMarks_header).is_displayed()
            assert verifyheader5 == True
            verifyheader6 = self.driver.find_element_by_link_text(BorrowLoanPage.OpenPositions_header).is_displayed()
            assert verifyheader6 == True
            verifyheader7 = self.driver.find_element_by_link_text(BorrowLoanPage.LoanSummary_header).is_displayed()
            assert verifyheader7 == True
            verifyheader8 = self.driver.find_element_by_link_text(BorrowLoanPage.BorrowSummary_header).is_displayed()
            assert verifyheader8 == True
            verifyheader9 = self.driver.find_element_by_link_text(BorrowLoanPage.BorrowLoan_header).is_displayed()
            assert verifyheader9 == True
            verifyheader10 = self.driver.find_element_by_link_text(BorrowLoanPage.BorrowOportunities_header).is_displayed()
            assert verifyheader10 == True
            verifyheader11 = self.driver.find_element_by_link_text(BorrowLoanPage.RateUpside_header).is_displayed()
            assert verifyheader11 == True
            verifyheader12 = self.driver.find_element_by_link_text(BorrowLoanPage.LendingPit_header).is_displayed()
            assert verifyheader12 == True
            verifyheader13 = self.driver.find_element_by_link_text(BorrowLoanPage.UnAllocated_header).is_displayed()
            assert verifyheader13 == True
            screenshot("pass",tc_name + "_1")
            self.driver.close()
        except:
            screenshot("fail",tc_name)
            self.driver.close()
            raise




