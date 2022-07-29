
class FPLPage(object):
    FPL_header = "FPL"
    FPLAccounts_header = "FPL Accounts"
    FPLAvailable_header = "FPL Available Inventory"
    FPLOutOfBalance_header = "FPL Out of Balance Report"
    FPLPositions_header = "FPL Positions Report"
    FPLCustomer_header = "FPL Customer Loan/Return Allocation"
    FPLRebate_header = "FPL Rebate Allocation"
    FPLAccountBalance_header = "FPL Account Balance vs. Market Value"
    FPLRegAcct_header = "Reg Acct FPL Out Of Balance"

    SettleDate = "ctl00_CC_SettleDateTxt"
    SettleDate2 = "ctl00_CC_tbSettleDate"
    SettleDateFrom = "ctl00_CC_SettleDateFromTxt"
    SettleDateTo = "ctl00_CC_SettleDateToTxt"
    ReportDate = "ctl00_CC_ReportDateFromTxt"
    ReportDate2 = "ctl00_CC_ReportDateTxt"
    TradeDate = "ctl00_CC_DateFromTxt"
    TradeDate2 = "ctl00_CC_tbTradeDate"
    TradeDate3 = "ctl00_CC_TradeDateFromTxt"
    Date = "ctl00_CC_DateTxt"
    DatePiker = "//div[@id='ui-datepicker-div']/div/a/span"
    CusipTxt = "ctl00_CC_CUSIPTxt"
    CusipAAPL = "AAPL"
    CusipMSFT = "MSFT"
    CusipAMZN = "AMZN"
    SearchButton = "ctl00_CC_SearchBtn"
    SearchButton2 = "ctl00_CC_btnSearch"
    Download_button = "ctl00_CC_DownloadBtn"
    Download_button2 = "ctl00_CC_btnDownload"
    TradeDateOption = "ctl00_CC_MonthDateDll"
    TestTradeDate = "Dec 2020"

    DTCNumber_header_1 = "DTCNumber"
    DTCNumber_element_1 = "//table[@id='ctl00_WG_FPLAccountsGridView']/tbody/tr[2]/td[2]"
    ClientAccount_header_1 = "Client Account"
    ClientAccount_element_1 = "//table[@id='ctl00_WG_FPLAccountsGridView']/tbody/tr[2]/td[3]"
    FPLAccount_header_1 = "FPL Account"
    FPLAccount_element_1 = "//table[@id='ctl00_WG_FPLAccountsGridView']/tbody/tr[2]/td[4]"
    Name_header_1 = "Name"
    Name_element_1 = "//table[@id='ctl00_WG_FPLAccountsGridView']/tbody/tr[2]/td[5]"
    Office_header_1 = "Office"
    Office_element_1 = "//table[@id='ctl00_WG_FPLAccountsGridView']/tbody/tr[2]/td[6]"
    AllocationType_header_1 = "Allocation Type"
    AllocationType_element_1 = "//table[@id='ctl00_WG_FPLAccountsGridView']/tbody/tr[2]/td[7]"
    AccountPriority_header_1 = "Account Priority"
    AccountPriority_element_1 = "//table[@id='ctl00_WG_FPLAccountsGridView']/tbody/tr[2]/td[8]"
    IsActive_header_1 = "IsActive"

    ReportDate_header_2 = "ReportDate"
    ReportDate_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[2]"
    DTC_header_2 = "DTC"
    DTC_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[3]"
    AccountNumber_header_2 = "AccountNumber"
    AccountNumber_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[4]"
    AccType_header_2 = "AcctType"
    AccType_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[5]"
    Name_header_2 = "Name"
    NameLine2_header_2 = "NameLine2"
    Office_header_2 = "Office"
    Office_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[8]"
    Cusip_header_2 = "CUSIP"
    Cusip_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[9]"
    Symbol_header_2 = "Symbol"
    Symbol_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[10]"
    Quantity_header_2 = "Quantity"
    Quantity_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[11]"
    Price_header_2 = "Price"
    Price_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[12]"
    MarketValue_header_2 = "MarketValue"
    MarketValue_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[13]"
    LoanRate_header_2 = "LoanRateAvg"
    LoanRate_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[14]"
    Units_header_2 = "Units"
    Units_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[15]"
    Potencial_header_2 = "PotentialValue"
    Potencial_element_2 = "//table[@id='ctl00_WG_FPLAvailableInvemtoryGridView']/tbody/tr[2]/td[16]"

    ReportDate_header_3 = "ReportDate"
    ReportDate_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[2]"
    DTC_header_3 = "DTC"
    DTC_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[3]"
    Cusip_header_3 = "CUSIP"
    Cusip_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[4]"
    Symbol_header_3 = "Symbol"
    Symbol_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[5]"
    StkRecQty_header_3 = "StkRecQty"
    StkRecQty_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[6]"
    LoanQty_header_3 = "LoanQty"
    LoanQty_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[7]"
    LoanQty5166_header_3 = "LoanQty 5166"
    LoanQty5166_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[8]"
    DiffQtyStkRec_header_3 = "DiffQty StkRec vs DTC"
    DiffQtyStkRec_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[9]"
    DiffQtyDTC_header_3 = "DiffQty DTC vs 5166"
    DiffQtyDTC_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[10]"
    StkRec_header_3 = "StkRecPrice"
    StkRec_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[11]"
    StkPrice_header_3 = "StkRec Amt"
    StkPrice_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[12]"
    LoanPrice_header_3 = "LoanPrice"
    LoanPrice_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[13]"
    LoanAmt_header_3 = "LoanAmt"
    LoanAmt_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[14]"
    DiffAmt_header_3 = "DiffAmt StkRec vs DTC"
    DiffAmt_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[15]"
    LoanPrice5166_header_3 = "LoanPrice 5166"
    LoanPrice5166_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[16]"
    LoanAmt5166_header_3 = "LoanAmt 5166"
    LoanAmt5166_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[17]"
    Rate5166_header_3 = "Rate 5166"
    Rate5166_element_3 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[18]"

    DTC_header_4 = "DTC"
    DTC_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[2]"
    ReportDate_header_4 = "ReportDate"
    ReportDate_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[3]"
    AccountNumber_header_4 = "AccountNumber"
    AccountNumber_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[4]"
    AccType_header_4 = "AcctType"
    AccType_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[5]"
    Name_header_4 = "Name"
    Name_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[6]"
    NameLine2_header_4 = "NameLine2"
    NameLine2_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[7]"
    Office_header_4 = "Office"
    Office_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[8]"
    Cusip_header_4 = "CUSIP"
    Cusip_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[9]"
    Symbol_header_4 = "Symbol"
    Symbol_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[10]"
    LoanQty_header_4 = "LoanQty"
    LoanQty_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[11]"
    Price_header_4 = "Price"
    Price_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[12]"
    MarketValue_header_4 = "MarketValue"
    MarketValue_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[13]"
    Rate_header_4 = "Rate"
    Rate_element_4 = "//table[@id='ctl00_CC_FPLOutOfBalanceGridView']/tbody/tr[2]/td[14]"

    ReportDate_header_5 = "ReportDate"
    ReportDate_element_5 = "//table[@id='ctl00_WG_FPLReturnAllocationGridView']/tbody/tr[2]/td[2]"
    Office_header_5 = "Office"
    Office_element_5 = "//table[@id='ctl00_WG_FPLReturnAllocationGridView']/tbody/tr[2]/td[3]"
    Cusip_header_5 = "CUSIP"
    Cusip_element_5 = "//table[@id='ctl00_WG_FPLReturnAllocationGridView']/tbody/tr[2]/td[4]"
    Symbol_header_5 = "Symbol"
    Symbol_element_5 = "//table[@id='ctl00_WG_FPLReturnAllocationGridView']/tbody/tr[2]/td[5]"
    ClientAccount_header_5 = "ClientAccount"
    ClientAccount_element_5 = "//table[@id='ctl00_WG_FPLReturnAllocationGridView']/tbody/tr[2]/td[6]"
    ClientSettled_header_5 = "ClientSettledPosition"
    ClientSettled_element_5 = "//table[@id='ctl00_WG_FPLReturnAllocationGridView']/tbody/tr[2]/td[7]"
    ClientTrade_header_5 = "ClientTradeQty"
    ClientTrade_element_5 = "//table[@id='ctl00_WG_FPLReturnAllocationGridView']/tbody/tr[2]/td[8]"
    FPLAccount_header_5 = "FPLAccount"
    FPLAccount_element_5 = "//table[@id='ctl00_WG_FPLReturnAllocationGridView']/tbody/tr[2]/td[9]"
    FullyPaid_header_5 = "FullyPaidLoanQty"
    FullyPaid_element_5 = "//table[@id='ctl00_WG_FPLReturnAllocationGridView']/tbody/tr[2]/td[10]"

    Date_header_6 = "Date"
    Date_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[2]"
    DTC_header_6 = "DTC"
    DTC_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[3]"
    ClientAccount_header_6 = "Client Account"
    ClientAccount_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[4]"
    FPLAccount_header_6 = "FPL Account"
    FPLAccount_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[5]"
    AccType_header_6 = "Acct Type"
    AccType_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[6]"
    Office_header_6 = "Office"
    Office_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[7]"
    Cusip_header_6 = "CUSIP"
    Cusip_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[8]"
    Symbol_header_6 = "Symbol"
    Symbol_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[9]"
    QTY_header_6 = "QTY"
    QTY_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[10]"
    Price_header_6 = "Price"
    Price_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[11]"
    MarketValue_header_6 = "Market Value"
    MarketValue_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[12]"
    ClientRev_header_6 = "Client Rev Percent"
    ClientRev_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[13]"
    CorrRev_header_6 = "Corr Rev Percent"
    CorrRev_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[14]"
    CSDRev_header_6 = "CSD Rev Percent"
    CSDRev_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[15]"
    GSFRev_header_6 = "GSF Rev Percent"
    GSFRev_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[16]"
    LoanQty5166_header_6 = "Loan Qty 5166"
    LoanQty5166_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[18]"
    Price5166_header_6 = "Price 5166"
    Price5166_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[19]"
    LoanAMt5166_header_6 = "LoanAmt 5166"
    LoanAMt5166_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[20]"
    Rate5166_header_6 = "Rate 5166"
    Rate5166_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[21]"
    NumOfDays_header_6 = "Num Of Days"
    NumOfDays_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[22]"
    LoanRebate_header_6 = "Loan Rebate"
    LoanRebate_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[23]"
    FPLRebate_header_6 = "FPL Rebate"
    FPLRebate_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[24]"
    ClientDev_header_6 = "Client Rev Rebate"
    ClientDev_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[25]"
    CorrDevReb_header_6 = "Corr Rev Rebate"
    CorrDevReb_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[26]"
    CSDRevReb_header_6 = "CSD Rev Rebate"
    CSDRevReb_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[27]"
    GSFRevReb_header_6 = "GSF Rev Rebate"
    GSFRevReb_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[28]"
    AllocType_header_6 = "Alloc Type"
    AllocType_element_6 = "//table[@id='ctl00_WG_FPLRebateAllocationGridView']/tbody/tr[3]/td[17]"

    DTC_header_7 = "DTC"
    DTC_element_7 = "//table[@id='ctl00_WG_FPLAccountBalanceGridView']/tbody/tr[2]/td[2]"
    ReportDate_header_7 = "ReportDate"
    ReportDate_element_7 = "//table[@id='ctl00_WG_FPLAccountBalanceGridView']/tbody/tr[2]/td[3]"
    Account_header_7 = "Account"
    Account_element_7 = "//table[@id='ctl00_WG_FPLAccountBalanceGridView']/tbody/tr[2]/td[4]"
    RepCode_header_7 = "Repcode"
    RepCode_element_7 = "//table[@id='ctl00_WG_FPLAccountBalanceGridView']/tbody/tr[2]/td[5]"
    AccountName_header_7 = "AccountName"
    AccountName_element_7 = "//table[@id='ctl00_WG_FPLAccountBalanceGridView']/tbody/tr[2]/td[6]"
    NameLine1_header_7 = "NameLine1"
    NameLine1_element_7 = "//table[@id='ctl00_WG_FPLAccountBalanceGridView']/tbody/tr[2]/td[7]"
    CurrentClose_header_7 = "CurrentCloseLMV"
    CurrentClose_element_7 = "//table[@id='ctl00_WG_FPLAccountBalanceGridView']/tbody/tr[2]/td[8]"
    PreviousClose_header_7 = "PreviousCloseLMV"
    PreviousClose_element_7 = "//table[@id='ctl00_WG_FPLAccountBalanceGridView']/tbody/tr[2]/td[9]"
    CashBalance_header_7 = "CashBalance"
    CashBalance_element_7 = "//table[@id='ctl00_WG_FPLAccountBalanceGridView']/tbody/tr[2]/td[10]"
    SettleBalance_header_7 = "SettleBalance"
    SettleBalance_element_7 = "//table[@id='ctl00_WG_FPLAccountBalanceGridView']/tbody/tr[2]/td[11]"
    DiffSettle_header_7 = "Diff SettleBalance vs PreviousCloseLMV"
    DiffSettle_element_7 = "//table[@id='ctl00_WG_FPLAccountBalanceGridView']/tbody/tr[2]/td[12]"

    ReportDate_header_8 = "ReportDate"
    ReportDate_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[2]"
    DTC_header_8 = "DTC"
    DTC_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[3]"
    Cusip_header_8 = "CUSIP"
    Cusip_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[4]"
    Symbol_header_8 = "Symbol"
    Symbol_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[5]"
    StkRecQty_header_8 = "StkRecQty"
    StkRecQty_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[6]"
    LoanQty_header_8 = "LoanQty"
    LoanQty_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[7]"
    LoanQty5166_header_8 = "LoanQty 5166"
    LoanQty5166_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[8]"
    DiffQtyStkRec_header_8 = "DiffQty StkRec vs DTC"
    DiffQtyStkRec_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[9]"
    DiffQtyDTC_header_8 = "DiffQty DTC vs 5166"
    DiffQtyDTC_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[10]"
    StkRecPrice_header_8 = "StkRecPrice"
    StkRecPrice_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[11]"
    StkRecAmt_header_8 = "StkRec Amt"
    StkRecAmt_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[12]"
    LoanPrice_header_8 = "LoanPrice"
    LoanPrice_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[13]"
    LoanAmt_header_8 = "LoanAmt"
    LoanAmt_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[14]"
    DiffAmt_header_8 = "DiffAmt StkRec vs DTC"
    DiffAmt_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[15]"
    LoanPrice5166_header_8 = "LoanPrice 5166"
    LoanPrice5166_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[16]"
    LoanAmt5166_header_8 = "LoanAmt 5166"
    LoanAmt5166_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[17]"
    Rate5166_header_8 = "Rate 5166"
    Rate5166_element_8 = "//table[@id='ctl00_CC_FPLRegOutOfBalanceGridView']/tbody/tr[2]/td[18]"



