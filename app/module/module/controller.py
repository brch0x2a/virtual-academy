from app.module.common.db.consumer import runGetScript, runUpdateScript

from app.module.module.models import Module


def getAllModules():
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

    result = runGetScript(sql)

    return result

def getModulesBy(id):

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

    result = runGetScript(sql, (id))

    return result



def updateModule(course, title, price, id):
    title = str(title)

    sql = "Update  Module set id_course=%s, title=%s, price=%s"\
        "where id = %s"

    result = runUpdateScript(sql, (course, title, price, id))

    return result


def getModuleE(id):
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

    result = runGetScript(sql, (id))

    return result



def createModule(course, title, price):
    title = str(title)

    sql = "INSERT INTO Module(id_course, title, price)"\
        "Values(%s, %s, %s)"

    result = runUpdateScript(sql, (course, title, price))

    return result