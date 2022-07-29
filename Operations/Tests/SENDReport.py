
import requests
from Config import *

'''
url = 'https://api.adaptavist.io/tm4j/v2/automations/executions/cucumber'
myobj = {'autoCreateTestCases': 'true', 'projectKey': 'QTML' }
files = {'CRDSmokeTest.zip': open('CRDSmokeTest.zip','rb')}

headers = {"Authorization": "Bearer " + token, 'Content-Type': 'multipart/form-data', 'accept': '*.*', 'Accept-Encoding': 'gzip,deflate,br', 'Connection': 'keep-alive'}

x = requests.post(url, data = myobj, headers = headers, files = files)
print(x.content)
print(x.text)
'''
url = "https://api.zephyrscale.smartbear.com/v2/automations/executions/junit?autoCreateTestCases=true&projectKey=" + projectZephyr
#url = "https://api.adaptavist.io/tm4j/v2/automations/executions/junit?autoCreateTestCases=true&projectKey=" + projectZephyr

payload={}
files=[
  #('file',('SmokeTest.zip',open('SmokeTest.zip','rb'),'application/zip'))
  ('file',('junitxml_report.xml',open('junitxml_report.xml','rb'),'application/xml'))
]
headers = {
  'Authorization': 'Bearer ' + token
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
