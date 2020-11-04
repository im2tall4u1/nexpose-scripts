# Written by Trent Williams
# Creation Date 8/24/2020
# Modified Date 9/1/2020
# This program connects to Nexpose to download a report, writes it to CSV and moves it to desired location.
# Uses the requests library

import os
import requests
from requests.auth import HTTPProxyAuth
from datetime import datetime
import json
import ast
import shutil


#print(os.environ)

proxy_string = 'https://nexposeURL:portNumber'


dest_temp = "\\\\dc1ngdfile02v\\Packages\\InfoSec_Report" # production environment directory
test_directory = "C:\\Users\\User\\Test Folder" # local test directory

list_of_reports = [] # list of report ids
names_of_reports = [] # names matchup with report ids in list_of_reports

large_report = int
name_of_report = ''
#reports = s.get('https://dc1nexpose04v.corp.firstrepublic.com:3780/api/3/reports/3580/history/latest/output', auth=('z_nexpose_api', 'ogeCO4YgNgC58bo3oK#?'), verify=False)
#print(reports.text)



def create_report_request(id, name):
    base = proxy_string + '/api/3/reports/' + str(id) + '/history/latest/output' # URL for Nexpose API Call
    z = requests.Session()
    z.trust_env = False # Necessary to avoid OSError('Tunnel connection failed: 407 Proxy Authentication Required',)
    fetchedreport = z.get(base, auth=('********', '*********'), verify=False)

    current_date = datetime.now()
    date_string = current_date.strftime("%Y_%m_%d_%H_%M_%S") # DateTime for file name

    if fetchedreport.status_code == 200:
        print('Report Exists')
        with open(name + '_' + date_string + '.csv', 'w') as f:
            f.write(fetchedreport.text) # writes report to CSV
            shutil.copyfile(name + '_' + date_string + '.csv', test_directory) # moves CSV to directory

for report, name in zip(list_of_reports,names_of_reports):
    create_report_request(report, name)

