import pymysql
import os
from dotenv import load_dotenv

from app.module.module.models import Module


load_dotenv()

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")


def getAllModules():
    Modules = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()

    sql = '''
    SELECT 
        M.id, Cc.name, Cs.title, Cs.description, M.title, M.price
    FROM
        Module M
            INNER JOIN
        Course Cs ON Cs.id = M.id_course
            INNER JOIN
        Category_course Cc ON Cc.id = Cs.id_category;
          '''

    cursor.execute(sql)

    cursor.close()

    result = cursor.fetchall()
    print(len(result))

    for e in result:

        Modules.append(Module(e[0], e[1], e[2], e[3], e[4], e[5]))

    db.close()

    return Modules

def getModulesBy(id):
    Modules = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()

    sql = '''
    SELECT 
        M.id, Cc.name, Cs.title, Cs.description, M.title, M.price
    FROM
        Module M
            INNER JOIN
        Course Cs ON Cs.id = M.id_course
            INNER JOIN
        Category_course Cc ON Cc.id = Cs.id_category
        WHERE
        Cs.id = %s;
          '''

    cursor.execute(sql, (id))

    cursor.close()

    result = cursor.fetchall()
    print(len(result))

    for e in result:

        Modules.append(Module(e[0], e[1], e[2], e[3], e[4], e[5]))

    db.close()

    return Modules



def updateModule(course, title, price, id):
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)

    title = str(title)
    cursor = db.cursor()

    sql = "Update  Module set id_course=%s, title=%s, price=%s"\
        "where id = %s"

    cursor.execute(sql, (course, title, price, id))

    db.commit()

    cursor.close()

    db.close()

    return "Listo"


def getModuleE(id):
    Modules = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''
    SELECT 
        M.id, Cc.name, Cs.title, Cs.description, M.title, M.price
    FROM
        Module M
            INNER JOIN
        Course Cs ON Cs.id = M.id_course
            INNER JOIN
        Category_course Cc ON Cc.id = Cs.id_category
        where M.id=%s;
          '''

    cursor.execute(sql, (id))

    cursor.close()

    result = cursor.fetchall()
    print(len(result))

    for e in result:

        print(e[4])
        Modules.append(Module(e[0], e[1], e[2], e[3], e[4], e[5]))


    db.close()

    return Modules



def createModule(course, title, price):
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)

    title = str(title)


    cursor = db.cursor()

    sql = "INSERT INTO Module(id_course, title, price)"\
        "Values(%s, %s, %s)"

    cursor.execute(sql, (course, title, price))

    db.commit()

    cursor.close()

    db.close()

    return "Listo"