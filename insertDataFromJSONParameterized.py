#!/usr/bin/env python
import sys
import snowflake.connector
import json
userName = sys.argv[1]
passwordText = sys.argv[2]
accountName = sys.argv[3]
con = snowflake.connector.connect(
   # user='VARANCONSULTING',
   # password='Abcd123$',
   # account='FN49743.us-east-2.aws',
   user=userName,
   password=passwordText,
   account=accountName,
    session_parameters={
        'QUERY_TAG': 'EndOfMonthFinancials',
    }
)
cursor = con.cursor();
cursor.execute("ALTER SESSION SET QUERY_TAG = 'EndOfMonthFinancials'")
cursor.execute("USE WAREHOUSE COMPUTE_WH")
cursor.execute("USE DATABASE IDRREPORTS")
cursor.execute("USE SCHEMA PUBLIC")
# Putting Data
JSONText = '{"NUMBER": "2021020101",    "NAME": "AccountFeb0101",    "LAB": "LABFeb0101",    "TYPE": "CORPORATE"}'
#queryString = "insert into ACCOUNTS select parse_json(column1) from values (JSONText)"
#queryString = "select * from IDRREPORTS.PUBLIC.ACCOUNTS"
#queryString = "create or replace table test_semi_structured(var variant, arr array, obj object);"
#print(json.load(JSONText))
#cursor.execute(queryString)
#queryString = "desc table test_semi_structured;"
#cursor.execute(queryString)
#print(list(cursor.fetchall()))
#cursor.close()

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

json_string1 = """
{
    "NUMBER": "2021020101",
    "NAME": "AccountFeb0101",
    "LAB": "LABFeb0101",
    "TYPE": "CORPORATE",
}
"""
data = json.loads(json_string)
print(data)

queryString = "insert into ACCOUNTS select parse_json(column1) from values (" + json_string1 + ")"
cursor.execute(queryString)
#cursor.close()