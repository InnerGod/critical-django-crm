#ig-sw12
import mysql.connector

condb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

cursor = condb.cursor()

cursor.execute("CREATE DATABASE db_critical_weeks_app")

print("All Done!")

