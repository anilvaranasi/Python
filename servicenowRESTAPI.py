#REST API to read ServiceNow data
#Need to install requests package for python
#easy_install requests
import requests
import sys, os
import json


def override_where():
    """ overrides certifi.core.where to return actual location of cacert.pem"""
    # change this to match the location of cacert.pem
    return os.path.abspath("cacert.pem")


# is the program compiled?
if hasattr(sys, "frozen"):
    import certifi.core

    os.environ["REQUESTS_CA_BUNDLE"] = override_where()
    certifi.core.where = override_where

    # delay importing until after where() has been replaced
    import requests.utils
    import requests.adapters
    # replace these variables in case these modules were
    # imported before we replaced certifi.core.where
    requests.utils.DEFAULT_CA_BUNDLE_PATH = override_where()
    requests.adapters.DEFAULT_CA_BUNDLE_PATH = override_where()
#requests.get('https://github.com', verify='/path/to/certfile') 
# Set the request parameters
url = 'https://dev63486.service-now.com/api/now/table/incident?sysparm_limit=10'
#url = 'https://dev63486.service-now.com/api/now/table/incident?sysparm_query=active%3Dtrue%5Estate%3D2sysparm_limit=100'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'Abcd123$'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
#data = response.json()
result = {}
responseJSON = response.json()['result']
for item in responseJSON:
    print(str(item['number']))
#print(responseJSON)
#data = response
#incidentList = response
#for item in incidentList
 #   print(str(item['number'])
#s1 = json.dumps(data,default=str)
#print(s1)
#d2 = json.loads(s1)
#print(data)
#stageVar = data + ""
#print(data[1].number)
#print(data.result.)
#geek_dict = json.loads(data)
#print(d2)
#print(geek_dict['result'])