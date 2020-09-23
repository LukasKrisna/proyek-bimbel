import mysql.connector
def koneksi():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bimbel",
        autocommit=True
    )
    if db.is_connected():
        return db
    else:
        print ('DB disconnected!')
    
 
