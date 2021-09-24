
# COURSE

import pymysql
import os
from dotenv import load_dotenv

from app.module.course.models import Course
from app.module.category_course import controller as category_course_module

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


def createCourse(title, category, description, image):
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)

    title = str(title)

    cursor = db.cursor()

    sql = "INSERT INTO Course(id_category, title, description, image)"\
        "Values(%s, %s, %s, %s)"

    cursor.execute(sql, (category, title, description, image))

    db.commit()

    cursor.close()

    db.close()


    return "Listo"


def getAllCourses():
    Courses = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''
    SELECT 
        Cs.id, Cc.name, Cs.title, Cs.description, Cs.image
    FROM
        Course Cs
            INNER JOIN
        Category_course Cc ON Cc.id = Cs.id_category
          '''

    cursor.execute(sql)

    cursor.close()

    result = cursor.fetchall()
    print(len(result))

    for e in result:

        Courses.append(Course(e[0], e[1], e[2], e[3], e[4]))


    db.close()

    return Courses



def getCourseBy(categoryId):
    Courses = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''
    SELECT 
        Cs.id, Cc.name, Cs.title, Cs.description, Cs.image
    FROM
        Course Cs
            INNER JOIN
        Category_course Cc ON Cc.id = Cs.id_category
    WHERE
        Cc.id = %s
          '''

    cursor.execute(sql, (categoryId))

    cursor.close()

    result = cursor.fetchall()
    # print(len(result))

    for e in result:

        Courses.append(Course(e[0], e[1], e[2], e[3], e[4]))


    db.close()

    return Courses


def getCourseByBranch(branch_id):
    Courses = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''
    SELECT 
        Cs.id, Cc.name, Cs.title, Cs.description, Cs.image
    FROM
        Course Cs
            INNER JOIN
        Category_course Cc ON Cc.id = Cs.id_category
            inner join
        Branch_of_knowledge B ON B.id = Cc.id_branch 
    WHERE
        B.id = %s
          '''

    cursor.execute(sql, (branch_id))

    cursor.close()

    result = cursor.fetchall()
    print(len(result))

    for e in result:

        Courses.append(Course(e[0], e[1], e[2], e[3], e[4]))


    db.close()

    return Courses



def getCourseE(id):
    Courses = []
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()


    sql = '''
    SELECT 
        Cs.id, Cc.name, Cs.title, Cs.description, Cs.image
    FROM
        Course Cs
            INNER JOIN
        Category_course Cc ON Cc.id = Cs.id_category
    WHERE
        Cs.id = %s
          '''

    cursor.execute(sql, (id))

    cursor.close()

    result = cursor.fetchall()
    print(len(result))

    for e in result:

        Courses.append(Course(e[0], e[1], e[2], e[3], e[4]))


    db.close()

    return Courses

def updateCourseCatalog(category, title, description, uid, uimage):
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)

    title = str(title)
    category = str(category)
    description = str(description)
    uid = str(uid)
    image = str(uimage)

    print(image)
    # print("id:%s\t t: %s c: %s d:%s\timage:%s"%(uid, title, category, description, image))

    cursor = db.cursor()

    sql = ''' 
            UPDATE Course 
            SET 
                id_category = %s,
                title = %s,
                description = %s,
                image= %s
            WHERE
                id = %s
    '''

    cursor.execute(sql, (category, title, description, image, uid))

    db.commit()

    cursor.close()

    db.close()

    return "Listo"


def deleteModuleBy(id):

    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()

    print("delete id: %s", id)

    sql = '''            

        DELETE FROM Module
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


def deleteCourseBy(id):
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = db.cursor()

    print("delete id: %s", id)

    sql = '''            

        DELETE FROM Course
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


