import pymysql
import os
from app.module.branch_of_kwnoledge.models import Branch_of_knowledge
from dotenv import load_dotenv

load_dotenv()

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")



def get_all():
    Library = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''
        SELECT 
            id, name, image
        FROM
            academy.Branch_of_knowledge;
          '''

    cursor.execute(sql)

    cursor.close()

    result = cursor.fetchall()
    print(len(result))

    for e in result:

        Library.append(Branch_of_knowledge(e[0], e[1], e[2]))

    db.close()

    return Library
