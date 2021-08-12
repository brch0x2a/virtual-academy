import pymysql
import os
from dotenv import load_dotenv
from app.module.course.models import Category_course

load_dotenv()

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")



def getCategory_course():
    Catalog = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''
    SELECT 
        id, name
    FROM
        academy.Category_course;
          '''

    cursor.execute(sql)

    cursor.close()

    result = cursor.fetchall()

    for e in result:

        Catalog.append(Category_course(e[0], e[1]))

    db.close() 

    return Catalog