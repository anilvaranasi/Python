#REST API to read ServiceNow data
#Need to install requests package for python
#easy_install requests
import requests
import json
def buildUrl (instanceName, api, table, query, limit):
    url = 'https://'+ instanceName + '.service-now.com' + api + table + "?" + "sysparm_query=" + query + "&sysparm_limit=" + limit
    return url

def readServiceNowData(url,username,password):
    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    print (url + " " + username + " " + password)
    # Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers )
    # Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    # Decode the JSON response into a dictionary and use the data
    #data = response.json()
    result = {}
    #responseJSON = response.json()['result']
    responseJSON = response.json()['result']
    return responseJSON
# Set the request parameters
#url = 'https://dev63486.service-now.com/api/now/table/incident?sysparm_limit=10'
instanceName = 'dev99016'
api = '/api/now/table/'
table = 'incident'
#query = 'active%3Dtrue%5Estate%3D2'
query = 'active=true^state=2'
limit = '100'
url = buildUrl(instanceName,api,table,query,limit)
#print(url)

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'Abcd1234%'

responseJSON = readServiceNowData(url,user,pwd)
for item in responseJSON:
    print(str(item['number']))



