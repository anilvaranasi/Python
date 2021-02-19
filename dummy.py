# Import json module
import json

# Define json data
JSONData2='{"sourceTable":"incident","query":"active=true","stColumnList":"number|category|subcategory|short_description","targetTable":"tableName","ttColumnList":"NUMBER, CATEGORY, SUBCATEGORY, SHORTDESC"}'
JSONData = '{"Java": "3 Credits", "PHP": "2 Credits", "C++": "3 Credits"}'

# Load the json data into a variable
storedata = json.loads(JSONData2)

# Iterate the for loop to print the data with key
#for val in storedata:
  #print(val, storedata[val])
print(storedata['sourceTable'])