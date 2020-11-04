import requests
import json
import ast


################ INSTANCES ####################

def initialize_scan(site_id):
    scan_instance = 'https://nexposeURL:portNumber/api/3/sites/' + site_id + '/scans'
    request = requests.Session()
    request.trust_env = False
    request_body = {
        "engineId": int(engine_id),
        "hosts": hosts_for_scanning,
        "name": scan_name,
        "templateId": template_id
    }
    scan_initialization = request.post(scan_instance, auth=('**********', '**********'), verify=False,
                                       data=request_body)

    response_json_object = json.dumps(scan_initialization.text)
    response_dict_object = json.loads(response_json_object)
    response_body = ast.literal_eval(response_dict_object)
    print(scan_initialization.text)
    # scan_id = (response_body['id'])

    if scan_initialization.status_code == 200:
        print("Success")

    else:
        print("Failed")
        print(hosts_for_scanning)
        print(template_id)


def get_scan_status(scan_id):
    scan_instance = 'https://nexposeURL:portNumber/api/3/scans/' + str(scan_id)
    pass

####################### Main Program ################################


if __name__ == '__main__':
    site_id = input("Enter the identifier of the site: ")
    engine_id = input("Enter scan engine id: ")
    hosts_for_scanning = list(input("Enter hosts that should be included as a part of the scan. "
                                    "This should be a mixture of IP Addresses and Hostnames: ").split(', '))
    scan_name = input("Enter user-driven scan name for the scan: ")
    template_id = input("Enter the identifier of the scan template: ")

    initialize_scan(site_id)


