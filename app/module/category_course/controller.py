from app.module.category_course.models import Category_course
from app.module.common.db.consumer import runGetScript, runUpdateScript

def get_all():

    sql = '''
    SELECT 
        id, name, id_branch
    FROM
        academy.Category_course;
          '''
    
    result = runGetScript(sql)

    return result


def create(name, id_branch):

    name = str(name)

    sql = "INSERT INTO Category_course(name, id_branch)"\
        "Values(%s, %s)"
    
    result = runUpdateScript( sql, (name, id_branch) )

    return result


def delete(id):
    print("delete id: %s", id)

    sql = '''            
        DELETE FROM Category_course
        WHERE
            id = %s;
          '''


    result = runUpdateScript( sql, (id) )

    return result


def getE(id):

    sql = '''
        SELECT 
            id, name, id_branch
        FROM
            academy.Category_course 
        where id = %s
          '''

    result = runGetScript( sql, (id) )

    return result



def filterBy(id_branch):

    sql = '''
        SELECT 
            id, name, id_branch
        FROM
            academy.Category_course 
        where id_branch = %s
          '''

    result = runGetScript( sql, (id_branch) )

    return result



def update(id, name, id_branch):

    id = str(id)
    name = str(name)

    id_branch = str(id_branch)


    sql = ''' 
            UPDATE Category_course 
            SET 
                name = %s,
                id_branch= %s
            WHERE
                id = %s
    '''

    result = runUpdateScript( sql, (name, id_branch, id) )

    return result