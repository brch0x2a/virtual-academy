from app.module.branch_of_kwnoledge.models import Branch_of_knowledge
from app.module.common.db.consumer import runGetScript, runUpdateScript


def get_all_all():
    
    sql = '''
        SELECT 
            id, name, image
        FROM
            academy.Branch_of_knowledge;
          '''
 
    result = runGetScript(sql)

    return result

def get_all():

    sql = '''
        SELECT 
            id, name, image
        FROM
            academy.Branch_of_knowledge;
          '''
    
    result = runGetScript(sql)

    return result



def create(title, image):
    

    sql = "INSERT INTO Branch_of_knowledge(name, image)"\
        "Values(%s, %s)"

    result = runUpdateScript(sql, (title, image))


    return result


def delete(id):
  

    print("delete id: %s", id)

    sql = '''            

        DELETE FROM Branch_of_knowledge
        WHERE
            id = %s;
          '''

    
    result = runUpdateScript(sql, (id) )
    
    print(len(result))


    return result


def getE(id):

    sql = '''
        SELECT 
            id, name, image
        FROM
            academy.Branch_of_knowledge 
        where id = %s
          '''

  
    result = runGetScript( sql, (id) )
    print(len(result))

    return result




def update(id, name, image):
    id = str(id)
    name = str(name)

    image = str(image)

    sql = ''' 
            UPDATE Branch_of_knowledge 
            SET 
                name = %s,
                image= %s
            WHERE
                id = %s
    '''

    result = runUpdateScript(sql, (name, image, id))

    return result