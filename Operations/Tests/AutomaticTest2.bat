@ECHO OFF 
:: This batch file runs the test cycle and generates the JSON file
TITLE JSON file 
:: Section 1: Executing Test Cycle
ECHO ==========================
ECHO Runing test cycle 
ECHO ============================
pytest --env %1 --browser %2 -v -m smoke --junitxml=junitxml_report.xml --html=report_smoke.html --self-contained-html
:: Section 3: JSON file compression
::ECHO ============================
::ECHO Sending Results to Zephyr
::ECHO ============================
::python SENDReport.py