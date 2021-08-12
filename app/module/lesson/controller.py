import pymysql
import os
from dotenv import load_dotenv

from app.module.course.models import Lesson

load_dotenv()

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")


def createLesson(module, title, filepath):
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)

    title = str(title)

    cursor = db.cursor()

    sql = "INSERT INTO Lesson(id_module, title, filepath)"\
        "Values(%s, %s, %s)"

    cursor.execute(sql, (module, title, filepath))

    db.commit()

    cursor.close()

    db.close()

    return "Listo"


def getAllLesson():
    Lessons = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''
        SELECT 
            M.id,
            Cc.name,
            Cs.title,
            Cs.description,
            Md.title,
            M.title,
            M.filepath
        FROM
            Lesson M
                INNER JOIN
            Module Md ON Md.id = M.id_module
                INNER JOIN
            Course Cs ON Cs.id = Md.id_course
                INNER JOIN
            Category_course Cc ON Cc.id = Cs.id_category;
          '''

    cursor.execute(sql)

    cursor.close()

    result = cursor.fetchall()
    print(len(result))

    for e in result:

        Lessons.append(Lesson(e[0], e[1], e[2], e[3], e[4], e[5], e[6]))


    db.close()

    return Lessons




def getLessonBy(moduleId):
    Lessons = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()

    sql = '''
        SELECT 
            M.id,
            Cc.name,
            Cs.title,
            Cs.description,
            Md.title,
            M.title,
            M.filepath
        FROM
            Lesson M
                INNER JOIN
            Module Md ON Md.id = M.id_module
                INNER JOIN
            Course Cs ON Cs.id = Md.id_course
                INNER JOIN
            Category_course Cc ON Cc.id = Cs.id_category
            Where 
            Md.id = %s;
          '''

    cursor.execute(sql, (moduleId))

    cursor.close()

    result = cursor.fetchall()
    print(len(result))

    for e in result:

        Lessons.append(Lesson(e[0], e[1], e[2], e[3], e[4], e[5], e[6]))


    db.close()

    return Lessons



def deleteLessonBy(id):


    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''            
            DELETE FROM Lesson 
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