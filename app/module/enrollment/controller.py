from app.module.common.db.consumer import runGetScript

from app.module.course import controller as course_module

from app.module.category_course import controller as category_course_module

from app.module.enrollment.models import Enrollment
from app.module.enrollment.models import Holder
from app.module.enrollment.models import Grid


def get_all():

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

    result = runGetScript(sql)

    return result


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