
# COURSE

from app.module.common.db.consumer import runGetScript, runUpdateScript

from app.module.course.models import Course
from app.module.category_course import controller as category_course_module


def getCategory_course():

    sql = '''
    SELECT 
        id, name
    FROM
        academy.Category_course;
          '''

    result = runGetScript(sql)

    return result


def createCourse(title, category, description, image):
    title = str(title)

    sql = "INSERT INTO Course(id_category, title, description, image)"\
        "Values(%s, %s, %s, %s)"

    result = runUpdateScript( sql, (category, title, description, image) )

    return result


def getAllCourses():
    sql = '''
    SELECT 
        Cs.id, Cc.name, Cs.title, Cs.description, Cs.image
    FROM
        Course Cs
            INNER JOIN
        Category_course Cc ON Cc.id = Cs.id_category
          '''

    result = runGetScript(sql)

    return result



def getCourseBy(categoryId):

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

    result = runGetScript(sql, (categoryId))

    return result

def getCourseById(courseId):

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

    result = runGetScript(sql, (courseId))

    return result


def getCourseByBranch(branch_id):

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

    result = runGetScript(sql, (branch_id))

    return result



def getCourseE(id):
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

    result = runGetScript( sql, (id) )

    return result

def updateCourseCatalog(category, title, description, uid, uimage):
    title = str(title)
    category = str(category)
    description = str(description)
    uid = str(uid)
    image = str(uimage)

    print(image)
    # print("id:%s\t t: %s c: %s d:%s\timage:%s"%(uid, title, category, description, image))

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

    result = runUpdateScript( sql, (category, title, description, image, uid) )

    return result


def deleteModuleBy(id):
    print("delete id: %s", id)

    sql = '''            

        DELETE FROM Module
        WHERE
            id = %s;
          '''

    result = runUpdateScript( sql, (id) )

    return result


def deleteCourseBy(id):
    print("delete id: %s", id)

    sql = '''            

        DELETE FROM Course
        WHERE
            id = %s;
          '''

    result = runUpdateScript( sql, (id) )

    return result


