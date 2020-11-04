import requests
import json
import ast
from datetime import datetime
import shutil
import csv

#reports_base = 'https://dc1nexpose04v.corp.firstrepublic.com:3780/api/3/reports/' + str(
    #id) + '/history/latest/output'  # URL for Nexpose API Reports Call

url = 'https://nexposeURL:portNumber'
windows_servers_np_id = 19
name = 'Windows Servers NP'
current_date = datetime.now()
date_string = current_date.strftime("%Y_%m_%d_%H_%M_%S")
test_directory = "C:\\Users\\trwilliams\\Test Folder"


#z = requests.Session()
#z.trust_env = False  # Necessary to avoid OSError('Tunnel connection failed: 407 Proxy Authentication Required',)
#fetchedreport = z.get(asset_groups, auth=('*********', '*********'), verify=False)
#print(fetchedreport.text)

assets_instance = url + '/api/3/asset_groups' + '/' + str(windows_servers_np_id) + '/assets'
r = requests.Session()
r.trust_env = False
fetched_assets = r.get(assets_instance, auth=('**********', '*********'), verify=False)
json_object = json.dumps(fetched_assets.text)
dict_object = json.loads(json_object)
assets = ast.literal_eval(dict_object)
asset = (assets['resources'])
vulnerabilities_via_asset = []
list_of_vuln = []
print(type(asset))

def get_vulnerabilies_via_asset(id):
    v = requests.Session()
    v.trust_env = False

    asset_vulnerability_url = url + '/' + str(id) + '/vulnerabilities'
    fetch_vulnerabilities = v.get(asset_vulnerability_url, auth=('*********', '*********'), verify=False)
    if fetch_vulnerabilities.status_code == 200:
        print('API call successful... working...')
        print(fetch_vulnerabilities.text)
        vuln_json_object = json.dumps(fetch_vulnerabilities.text)
        vuln_dict_object = json.loads(vuln_json_object)
        #print(type(vuln_dict_object))
        vulnerabilities = ast.literal_eval(vuln_dict_object)
        vulnerability = (vulnerabilities['resources'])




        for elem in vulnerability:
            values_view = elem.values()
            value_iterator = iter(values_view)
            first_value = next(value_iterator)
            list_of_vuln.append(first_value)


for item in asset:
    get_vulnerabilies_via_asset(item)

print(list_of_vuln)


