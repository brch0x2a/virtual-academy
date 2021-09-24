# User

import pymysql
import os
from app.module.user.models import User_table
from dotenv import load_dotenv
from app.module.common.dbConsumer.dbConsumer import runGetScript

load_dotenv()

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")


def createUser(pnick_name,  pemail, ppassword):

    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)

    nick_name = str(pnick_name)
    email = str(pemail)
    password = str(ppassword)

    cursor = db.cursor()

    sql = "INSERT INTO User_table(fname, email, password)"\
        "Values(%s, %s, %s)"

    cursor.execute(sql, (nick_name, email, password))

    db.commit()
    cursor.close()

    db.close()

    return "Listo"



def getAllUser():
    Users = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''
  SELECT 
    id, fname, email
FROM
    academy.User_table;
          '''

    cursor.execute(sql)

    cursor.close()

    result = cursor.fetchall()
    print(len(result))

    for e in result:

        Users.append(User_table(e[0], e[1], e[2], ""))

    db.close()

    return Users


def authUser(username, password):
    # db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)

    # cursor = db.cursor()


    sql = '''
    SELECT 
        id, fname
    FROM
        academy.User_table
    WHERE
        email = %s
            AND password = %s;
          '''

    result = runGetScript(sql, (username, password))
    result = result[0]
    # cursor.execute(sql, (username, password))

    # cursor.close()

    # result = cursor.fetchone()

    # db.close()

    return result