# User

import pymysql
from app.module.user.models import User_table

IP = "localhost"
PASS = "wrf!C:w(>7:&"


db = pymysql.connect(host=IP, user="brch", password=PASS, db="academy")


def createUser(pnick_name,  pemail, ppassword):

    db = pymysql.connect(host=IP, user="brch", password=PASS, db="academy")

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
    db = pymysql.connect(host=IP, user="brch", password=PASS, db="academy")
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
    db = pymysql.connect(host=IP, user="brch", password=PASS, db="academy")

    cursor = db.cursor()


    sql = '''
    SELECT 
        id, fname
    FROM
        academy.User_table
    WHERE
        email = %s
            AND password = %s;
          '''

    cursor.execute(sql, (username, password))

    cursor.close()

    result = cursor.fetchone()

    db.close()

    return result