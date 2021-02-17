#REST API to read ServiceNow data
#Need to install requests package for python
#easy_install requests
import requests
import json
def buildUrl (instanceName, api, table, query, limit):
    url = 'https://'+ instanceName + '.service-now.com' + api + table + "?" + "sysparm_query=" + query + "&sysparm_limit=" + limit
    return url

def makeRESTCall(url,username,password):
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
instanceName = 'dev63486'
api = '/api/now/table/'
table = 'incident'
#query = 'active%3Dtrue%5Estate%3D2'
query = 'active=true^state=2'
limit = '2'
url = buildUrl(instanceName,api,table,query,limit)
#print(url)

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'Abcd123$'
responseJSON = makeRESTCall(url,user,pwd)
def parseResponse(responseJSON):
    row = ''
    counter=1
    for item1 in responseJSON:
        shortDesc=str(item1['short_description'])
        if (int(counter) < int(len(responseJSON))):
            shortDesc=shortDesc.replace(',', ' ')
            row+='('+"'"+str(item1['number'])+"'"+','+"'"+str(item1['category'])+"'"+','+"'"+str(item1['subcategory'])+"'"+','+"'"+shortDesc+"'"+')'+","
            print(counter)
            counter=counter+1
        else:
            row+='('+"'"+str(item1['number'])+"'"+','+"'"+str(item1['category'])+"'"+','+"'"+str(item1['subcategory'])+"'"+','+"'"+shortDesc+"'"+')'
    return row
row = parseResponse(responseJSON)
print(row)
def loadSnowflake(row):
    import snowflake.connector
    con = snowflake.connector.connect(
        user='VARANCONSULTING',
        password='Abcd123$',
        account='FN49743.us-east-2.aws',
        session_parameters={
            'QUERY_TAG': 'EndOfMonthFinancials',
        }
    )
    #rowSet = "    ('INC000111', 'beth mary', 'hardware', 'laptop', 'test1') " + "," + "    ('INC00002', 'system administrator', 'hardware', 'desktop', 'test')"
    rowSet=row
    tableName = 'INCIDENT'
    columnList = '(NUMBER, CATEGORY, SUBCATEGORY, SHORTDESC)'
    sqlQuery = "INSERT INTO " + tableName + columnList + ' VALUES ' + rowSet + ";"
    con.cursor().execute("ALTER SESSION SET QUERY_TAG = 'EndOfMonthFinancials'")
    con.cursor().execute("USE WAREHOUSE COMPUTE_WH")
    con.cursor().execute("USE DATABASE IDRREPORTS")
    con.cursor().execute("USE SCHEMA PUBLIC")
    #con.cursor().execute(
    # "INSERT INTO ACCOUNTS(LAB, NAME) VALUES " + 
    #"    ('labx24', 'accountx1'), " + 
    #"    ('labx25', 'accountx2')")
    print(sqlQuery)
    con.cursor().execute(sqlQuery)
loadSnowflake(row)
