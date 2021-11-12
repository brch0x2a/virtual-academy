import pymysql
import pymysql.cursors
import os
from dotenv import load_dotenv

# nombres convención --> dbConsumer.lalala
    # USAR ALIAS 
# cambiar nombre a la carpeta [carpeta --> db, archivo --> consumer]
# definir dto --> usar el dict de pymysql
# PROPAGAR CAMBIOS 


def getBD():
    # ,port=3307
    load_dotenv()
    MYSQL_HOST = os.environ.get("MYSQL_HOST")
    MYSQL_USER = os.environ.get("MYSQL_USER")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
    MYSQL_DB = os.environ.get("MYSQL_DB")
    MYSQL_PORT = os.environ.get("MYSQL_PORT")
    
    db = pymysql.connect(host=MYSQL_HOST, 
                         user=MYSQL_USER, 
                         password=MYSQL_PASSWORD, 
                         db=MYSQL_DB,
                         port=int(MYSQL_PORT),
                         cursorclass=pymysql.cursors.DictCursor
                         )
    return db
    
    
def runGetScript(myScript,scriptParams=None):
    db = getBD()
    cursor = db.cursor()
    cursor.execute(myScript,args=scriptParams)
    cursor.close()
    result = cursor.fetchall()
    
    cursor.close()
    db.close() 
    # ver si result es muy complicado
    print("RESULT: \n", result)
    return result

def runUpdateScript(myScript,scriptParams=None):
    try:
        #an script that updates bd state
        db = getBD()
        cursor = db.cursor()
        cursor.execute(myScript,args=scriptParams)
        db.commit()
        
        cursor.close()
        db.close() 
        # ver si result es muy complicado
        return {
            "error":None,
            "data":
                {
                "title" : "Success",
                "message" : " TOO LISTO PA' "
                }
            }
    except:
        return {
            "error":True,
            "data":
                {
                "title" : "Error",
                "message" : "An exception occurred",
                 }
            }

    

    
    