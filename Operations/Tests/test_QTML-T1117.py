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

# T1117 OPERATIONS PORTAL - BORROW LOAN - SMARTLOAN BORROW FOR NEEDS panel validation
@pytest.mark.smoke
class TestCRD_T1117():
    @pytest.fixture()

    def setup(self, env, browser):
        #pytest.set_trace()
        selectBrowser(self, browser)
        self.driver.implicitly_wait(30)
        baseURL = "http://wedbush%5c"+vusername+":"+vpassword+"@"+Environments.return_environments(env)
        self.driver.get(baseURL)
        #self.driver.execute_script("document.body.style.zoom='80%'")
        self.driver.maximize_window()

    def test_QTML_T1117(self, setup):
        tc_name = "T1117"
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
            self.driver.find_element_by_link_text(BorrowLoanPage.SmartLoanBorrow_header).click()
            time.sleep(3)
            screenshot("pass", tc_name + "_2")
            self.driver.find_element_by_id(BorrowLoanPage.SettleDate).click()
            self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            self.driver.find_element_by_xpath(BorrowLoanPage.DatePiker).click()
            self.driver.find_element_by_link_text("9").click()
            self.driver.find_element_by_id(BorrowLoanPage.SearchButton).click()
            time.sleep(3)
            screenshot("pass",tc_name + "_3")
            verifyheader1 = self.driver.find_element_by_id(BorrowLoanPage.SettleDate_header).is_displayed()
            assert verifyheader1 == True
            settledate = self.driver.find_element_by_id(BorrowLoanPage.SettleDate_element).text
            verifydate = checkvaliddateformat(settledate)
            assert verifydate == True
            verifyheader2 = self.driver.find_element_by_id(BorrowLoanPage.Cusip_header).is_displayed()
            assert verifyheader2 == True
            lengthCusip = len(self.driver.find_element_by_id(BorrowLoanPage.Cusip_element).text)
            assert lengthCusip == 9
            verifyheader3 = self.driver.find_element_by_id(BorrowLoanPage.Symbol_header).is_displayed()
            assert verifyheader3 == True
            verifyheader4 = self.driver.find_element_by_id(BorrowLoanPage.SecType_element).is_displayed()
            assert verifyheader4 == True
            verifyheader5 = self.driver.find_element_by_id(BorrowLoanPage.BetaBorrowNeeds_header).is_displayed()
            assert verifyheader5 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.BetaBorrowNeeds_element).text)
            verifyheader6 = self.driver.find_element_by_id(BorrowLoanPage.BetaBorrowQty_header).is_displayed()
            assert verifyheader6 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.BetaBorrowQty_element).text)
            verifyheader7 = self.driver.find_element_by_id(BorrowLoanPage.SmartLoanNeeds_header).is_displayed()
            assert verifyheader7 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.SmartLoanNeeds_element).text)
            verifyheader8 = self.driver.find_element_by_id(BorrowLoanPage.SmartLoanQty_header).is_displayed()
            assert verifyheader8 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.SmartLoanQty_element).text)
            verifyheader9 = self.driver.find_element_by_id(BorrowLoanPage.NeedsDiff_header).is_displayed()
            assert verifyheader9 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.NeedsDiff_element).text)
            verifyheader10 = self.driver.find_element_by_id(BorrowLoanPage.BorrowQtyDiff_header).is_displayed()
            assert verifyheader10 == True
            validatenumericformat(self.driver.find_element_by_xpath(BorrowLoanPage.BetaBorrowQty_element).text)
            self.driver.quit()
        except:
            screenshot("fail",tc_name)
            self.driver.quit()
            raise




