Todo 
- Generate test data using python
- Extract dat using python
- Create Objects in snowflake
- Load data in snowflake
- Query data using SQL in snowflake
- Build reports in powerbi


Architecture:



Data source db, Flat files, client apps
    ||
    || Tools: IICS, ADF. Power Center, Airbyte, Python 
    ||
    ||Extract LOAD
STAGING AREA[ On prem/ Cloud]
||
|| TOOLS: DBT, IICS, ADF,PowerCenter, AWS glue, Python

Transform Aggregate

    ||
    ||
DATA WAREHOUSE(Facts, Dimensions, Calc, )



