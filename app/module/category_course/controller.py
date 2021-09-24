import pymysql
import os
from dotenv import load_dotenv
from app.module.category_course.models import Category_course

load_dotenv()

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")

def get_all():
    Catalog = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()

    sql = '''
    SELECT 
        id, name, id_branch
    FROM
        academy.Category_course;
          '''

    cursor.execute(sql)

    cursor.close()

    result = cursor.fetchall()

    for e in result:

        Catalog.append(Category_course(e[0], e[1], e[2]))

    db.close() 

    # print(Catalog)

    return Catalog


def create(name, id_branch):
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)

    name = str(name)

    cursor = db.cursor()

    sql = "INSERT INTO Category_course(name, id_branch)"\
        "Values(%s, %s)"

    cursor.execute(sql, (name, id_branch))

    db.commit()

    cursor.close()

    db.close()

    return "Listo"


def delete(id):
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()

    print("delete id: %s", id)

    sql = '''            
        DELETE FROM Category_course
        WHERE
            id = %s;
          '''

    cursor.execute(sql, (id))

    cursor.close()

    result = cursor.fetchall()
    # print(len(result))

    db.commit()
    db.close()

    return "Done"


def getE(id):
    Library = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''
        SELECT 
            id, name, id_branch
        FROM
            academy.Category_course 
        where id = %s
          '''

    cursor.execute(sql, (id))

    cursor.close()

    result = cursor.fetchall()
    # print(len(result))


    for e in result:

        Library.append(Category_course(e[0], e[1], e[2]))


    db.close()

    return Library



def filterBy(id_branch):

    Library = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''
        SELECT 
            id, name, id_branch
        FROM
            academy.Category_course 
        where id_branch = %s
          '''

    cursor.execute(sql, (id_branch))

    cursor.close()

    result = cursor.fetchall()
    # print(sql)
    # print(id_branch)
    # print(len(result))

    for e in result:

        Library.append(Category_course(e[0], e[1], e[2]))


    db.close()

    return Library



def update(id, name, id_branch):

    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)


    id = str(id)
    name = str(name)

    id_branch = str(id_branch)


    cursor = db.cursor()

    sql = ''' 
            UPDATE Category_course 
            SET 
                name = %s,
                id_branch= %s
            WHERE
                id = %s
    '''

    cursor.execute(sql, (name, id_branch, id))

    db.commit()

    cursor.close()

    db.close()

    return "Listo"