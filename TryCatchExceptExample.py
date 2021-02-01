# Connecting to Snowflake using try and except blocks
import snowflake.connector
snowflake.connector.paramstyle='qmark'
con = snowflake.connector.connect(
    user='VARANCONSULTING',
    password='Abcd123$',
    account='FN49743.us-east-2.aws',
    autocommit=False,
    session_parameters={
        'QUERY_TAG': 'EndOfMonthFinancials',
    }
)
cursor = con.cursor()
cursor.execute("USE WAREHOUSE COMPUTE_WH")
cursor.execute("USE DATABASE IDRREPORTS")
cursor.execute("USE SCHEMA PUBLIC")
try:
    cursor.execute(
        "INSERT INTO ACCOUNTS(LAB, NAME) VALUES " + 
        "    ('labx7', 'accountx1'), " + 
        "    ('labx8', 'accountx2')")
    cursor.execute(
        "INSERT INTO ACCOUNTS(NUMBER) VALUES " + 
        "    ('NOTNUMBER') ")
    con.commit()
except Exception as e:
    con.rollback()
    raise e
finally:
    con.close()