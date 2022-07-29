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
from ScreenObjects.TreasuryPage import *
from ScreenObjects.Phase3FIXPage import *
from ScreenObjects.AccountingPage import *
from ScreenObjects.CreditPage import *
from ScreenObjects.CompliancePage import *
from ScreenObjects.Phase3Page import *
from ScreenObjects.FPLPage import *
from ScreenObjects.SettlementPage import *
from ScreenObjects.BorrowLoanPage import *
from ScreenObjects.CSDOperationsPage import *
from selenium.webdriver.common.action_chains import ActionChains
from Tests.Environments import *
from Tests.Browsers import *
from datetime import datetime
from datetime import timedelta

# T1117 OPERATIONS PORTAL - BORROW LOAN - SMARTLOAN BORROW FOR NEEDS panel validation
# @pytest.mark.smoke
# class TestCRD_T1117():
#     @pytest.fixture()
#
#     def setup(self, env, browser):

driver = webdriver.Chrome('chromedriver.exe')

#pytest.set_trace()
# selectBrowser(self, browser)
driver.implicitly_wait(30)
vusername = "islaso"
vpassword = "rIder08gibbs"
env = "UAT"
baseURL = "http://wedbush%5c"+vusername+":"+vpassword+"@"+Environments.return_environments(env)
driver.get(baseURL)
#driver.execute_script("document.body.style.zoom='80%'")
driver.maximize_window()

# Using Today's Date, minus 28 days
trade_date = datetime.now() - timedelta(days=28)
# Format's checkout date in format dd/mm/YYYY
trade_date_formatted = trade_date.strftime("%m/%d/%Y")

# def test_QTML_T1117(self, setup):
tc_name = "DEBUGGER"
time.sleep(3)
action = ActionChains(driver)
try:
    verifyheader = driver.find_element_by_xpath(LoginPage.header).is_displayed()
    assert verifyheader == True
    verifyheader1 = driver.find_element_by_link_text(CompliancePage.Compliance_header).is_displayed()
    assert verifyheader1 == True
    screenshot("pass", tc_name + "_1")
    borrowLoan = driver.find_element_by_link_text(LoginPage.Compliance_header)
    action.move_to_element(borrowLoan).perform()
    driver.find_element_by_link_text(CompliancePage.ETBList_header).click()
    driver.find_element_by_id(CompliancePage.tradeDateTxt).clear()
    driver.find_element_by_id(CompliancePage.tradeDateTxt).send_keys("01/01/2021")
    driver.find_element_by_id(CompliancePage.tradeDateTxt).send_keys(Keys.TAB)
    driver.find_element_by_id(CompliancePage.cusipTxt).send_keys("AAPL")
    driver.find_element_by_id(CompliancePage.SearchButton).click()
    '''
    time.sleep(2)
    driver.find_element_by_id(CompliancePage.tradeDateTxt).click()
    driver.find_element_by_xpath(CompliancePage.DatePiker).click()
    driver.find_element_by_xpath(CompliancePage.DatePiker).click()
    driver.find_element_by_xpath(CompliancePage.DatePiker).click()
    driver.find_element_by_xpath(CompliancePage.DatePiker).click()
    driver.find_element_by_link_text("9").click()
    driver.find_element_by_id(CompliancePage.cusipTxt).send_keys("91282CCS8")
    driver.find_element_by_id(CompliancePage.SearchButton).click()
    '''
    time.sleep(5)
    screenshot("pass", tc_name + "_2")
    verifyheader = driver.find_element_by_id(CompliancePage.TradeDate_header).is_displayed()
    assert verifyheader == True
    tradedate = driver.find_element_by_id(CompliancePage.TradeDate_element).text
    verifydate = checkvaliddateformat(tradedate)
    assert verifydate == True
    verifyheader3 = driver.find_element_by_id(CompliancePage.Cusip_header).is_displayed()
    assert verifyheader3 == True
    lengthcusip = len(driver.find_element_by_id(CompliancePage.Cusip_element).text)
    assert lengthcusip == 9
    verifyheader4 = driver.find_element_by_id(CompliancePage.Symbol_header).is_displayed()
    assert verifyheader4 == True
    verifyheader5 = driver.find_element_by_id(CompliancePage.SecNum_header).is_displayed()
    assert verifyheader5 == True
    lengthsecnum = len(driver.find_element_by_id(CompliancePage.SecNum_element).text)
    assert lengthsecnum == 7
    verifyheader6 = driver.find_element_by_id(CompliancePage.Price_header).is_displayed()
    assert verifyheader6 == True
    validatecurrencyformat(driver.find_element_by_id(CompliancePage.Price_element).text)
    verifyheader7 = driver.find_element_by_id(CompliancePage.Threshold_header).is_displayed()
    assert verifyheader7 == True
    verifyheader8 = driver.find_element_by_id(CompliancePage.FailDays_header).is_displayed()
    assert verifyheader8 == True
    lengthactclass = len(driver.find_element_by_id(CompliancePage.FailDays_element).text)
    assert lengthactclass == 1
    verifyheader9 = driver.find_element_by_id(CompliancePage.External_header).is_displayed()
    assert verifyheader9 == True
    validatenumericformat(driver.find_element_by_id(CompliancePage.External_element).text)
    verifyheader10 = driver.find_element_by_id(CompliancePage.Firm_header).is_displayed()
    assert verifyheader10 == True
    validatenumericformat(driver.find_element_by_id(CompliancePage.Firm_element).text)
    verifyheader11 = driver.find_element_by_id(CompliancePage.TotalInventory_header).is_displayed()
    assert verifyheader11 == True
    validatenumericformat(driver.find_element_by_id(CompliancePage.TotalInventory_element).text)
    verifyheader12 = driver.find_element_by_id(CompliancePage.LentUnits_header).is_displayed()
    assert verifyheader12 == True
    validatenumericformat(driver.find_element_by_id(CompliancePage.LentUnits_element).text)
    verifyheader13 = driver.find_element_by_id(CompliancePage.Utilization_header).is_displayed()
    assert verifyheader13 == True
    validatedecimalformat(driver.find_element_by_id(CompliancePage.Utilization_element).text)
    assert lengthcusip == 9
    verifyheader14 = driver.find_element_by_id(CompliancePage.AvgRAte_header).is_displayed()
    assert verifyheader14 == True
    validatedecimalformat(driver.find_element_by_id(CompliancePage.AvgRAte_element).text)
    verifyheader15 = driver.find_element_by_id(CompliancePage.Status_header).is_displayed()
    assert verifyheader15 == True
    verifyheader16 = driver.find_element_by_id(CompliancePage.LoanedQty_header).is_displayed()
    assert verifyheader16 == True
    validatenumericformat(driver.find_element_by_id(CompliancePage.LoanedQty_element).text)
    verifyheader17 = driver.find_element_by_id(CompliancePage.Borrowed_header).is_displayed()
    assert verifyheader17 == True
    validatenumericformat(driver.find_element_by_id(CompliancePage.Borrowed_element).text)
    verifyheader18 = driver.find_element_by_id(CompliancePage.LastFailQty_header).is_displayed()
    assert verifyheader18 == True
    validatenumericformat(driver.find_element_by_id(CompliancePage.LastFailQty_element).text)
    driver.quit()
except:
    screenshot("fail", tc_name)
    driver.quit()
    raise
