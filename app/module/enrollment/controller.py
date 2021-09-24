import pymysql
import os
from dotenv import load_dotenv


from app.module.course import controller as course_module

from app.module.category_course import controller as category_course_module

from app.module.enrollment.models import Enrollment
from app.module.enrollment.models import Holder
from app.module.enrollment.models import Grid

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
            E.id,
            E.id_course,
            C.image,
            C.title,
            C.description,
            U.email,
            E.enrollment_date
        FROM
            Enrollment E
                INNER JOIN
            Course C ON E.id_course = C.id
                INNER JOIN
            User_table U ON U.id = E.id_user
          '''

    cursor.execute(sql)

    cursor.close()

    result = cursor.fetchall()

    for e in result:

        Catalog.append( Enrollment(e[0], e[1], e[2], e[3], e[4], e[5], e[6]))

    db.close() 

    return Catalog


def grid(id_branch):

    category_course = category_course_module.filterBy(id_branch)
    course = []

    grid = Grid()

    for e in category_course:
       
        grid.colection.append(Holder(e))

        course = course_module.getCourseBy(e.id)

        for c in course:
            grid.colection[-1].course_colection.append(c)

    print("\n\n\t -- Branch | %s -- \n"%(id_branch))

    for h in grid.colection:
        print("\033[32;1mID:%s\t| Category:%s\033[0m"%(h.category.id, h.category.name))

        for c in h.course_colection:
            print("\t\t\033[34;1mCourse>>%s\033[0m"%(c.title))


    print("\n")


    return grid