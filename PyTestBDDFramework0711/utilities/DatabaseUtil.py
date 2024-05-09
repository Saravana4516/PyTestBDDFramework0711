import pymysql.cursors
import yaml
import pyodbc as odbccon
import mysql.connector

with open('./config/envInfo.yaml', "r") as f:
    info = yaml.safe_load(f)

def connect_to_database(env):
    if (env == 'QA'):
        # noinspection PyArgumentList
        connection = pymysql.connect(
            host=info["REGION"]["QA"]["hostname"],
            port=info["REGION"]["QA"]["portnumber" ],
            user=info["REGION"]["QA"] ["username"],
            password=info[ "REGION"]["QA"]["password"],
            charset='utf8mb4',
            ssl={"fake_flag_to_enable_tls.": True}
        )
    
        print("The DB connection is successful")
    else:

        connection = pymysql.connect(
            host=info["REGION"]["DEV"]["hostname"],
            port=info["REGION"]["DEV"]["portnumber"],
            user=info["REGION"]["DEV"]["username"],
            password=info["REGION"]["DEV"]["password"],
            charset='utf8mb4',
            ssl={"fake_flag_to_enable_tls.": True}
        )

    return connection
        