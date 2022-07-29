@ECHO OFF 
:: This batch file runs the test cycle and generates the JSON file
TITLE JSON file 
:: Section 1: Executing Test Cycle
ECHO ==========================
ECHO Runing test cycle 
ECHO ============================
pytest --env %1 -v -m smoke --json-report --html=report_smoke.html --self-contained-html
:: Section 2: JSON file generation
ECHO ============================
ECHO Generating JSON file
ECHO ============================
python JSONParser.py
:: Section 3: JSON file compression
ECHO ============================
ECHO Generating JSON.zip file
ECHO ============================
tar -a -c -f SmokeTest.zip SmokeTest.json
:: Section 3: JSON file compression
ECHO ============================
ECHO Sending Results to Zephyr
ECHO ============================
python SENDReport.py