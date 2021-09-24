import pymysql
import os
from app.module.branch_of_kwnoledge.models import Branch_of_knowledge
from dotenv import load_dotenv
from app.module.common.dbConsumer.dbConsumer import runGetScript


load_dotenv()

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")

def get_all_all():
    Library = []
    # db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    # cursor = db.cursor()

    sql = '''
        SELECT 
            id, name, image
        FROM
            academy.Branch_of_knowledge;
          '''
    # cursor.execute(sql)

    # cursor.close()

    # result = cursor.fetchall()
    result = runGetScript(sql)
    # print(len(result))

    # for e in result:

    #     Library.append(Branch_of_knowledge(e[0], e[1], e[2]))

    # db.close()

    return result

def get_all():
    Library = []
    # db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    # cursor = db.cursor()

    sql = '''
        SELECT 
            id, name, image
        FROM
            academy.Branch_of_knowledge;
          '''
    # cursor.execute(sql)

    # cursor.close()

    # result = cursor.fetchall()
    result = runGetScript(sql)
    print(len(result))

    for e in result:

        Library.append(Branch_of_knowledge(e[0], e[1], e[2]))

    # db.close()

    return Library



def create(title, image):
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)

    title = str(title)

    cursor = db.cursor()

    sql = "INSERT INTO Branch_of_knowledge(name, image)"\
        "Values(%s, %s)"

    cursor.execute(sql, (title, image))

    db.commit()

    cursor.close()

    db.close()

    return "Listo"


def delete(id):
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()

    print("delete id: %s", id)

    sql = '''            

        DELETE FROM Branch_of_knowledge
        WHERE
            id = %s;
          '''

    cursor.execute(sql, (id))

    cursor.close()

    result = cursor.fetchall()
    print(len(result))

    db.commit()
    db.close()

    return "Done"


def getE(id):
    Library = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''
        SELECT 
            id, name, image
        FROM
            academy.Branch_of_knowledge 
        where id = %s
          '''

    cursor.execute(sql, (id))

    cursor.close()

    result = cursor.fetchall()
    print(len(result))


    for e in result:

        Library.append(Branch_of_knowledge(e[0], e[1], e[2]))


    db.close()

    return Library




def update(id, name, image):
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)


    id = str(id)
    name = str(name)

    image = str(image)


    cursor = db.cursor()

    sql = ''' 
            UPDATE Branch_of_knowledge 
            SET 
                name = %s,
                image= %s
            WHERE
                id = %s
    '''

    cursor.execute(sql, (name, image, id))

    db.commit()

    cursor.close()

    db.close()

    return "Listo"