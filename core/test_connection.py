import MySQLdb # type: ignore

try:
    db = MySQLdb.connect(
        host="localhost",
        user="user",
        passwd="1234",
        db="jrc_ferreteria"
    )
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data)
    db.close()
except MySQLdb.Error as e:
    print(f"Error connecting to MySQL Database: {e}")
