import pymysql

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='finances',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)