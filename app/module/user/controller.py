# User

from app.module.common.db.consumer import runGetScript, runUpdateScript

from app.module.user.models import User_table
from app.module.common.db.consumer import runGetScript


def createUser(pnick_name,  pemail, ppassword):

    nick_name = str(pnick_name)
    email = str(pemail)
    password = str(ppassword)

    sql = "INSERT INTO User_table(fname, email, password)"\
        "Values(%s, %s, %s)"

    result = runGetScript( sql, (nick_name, email, password) )

    return result



def getAllUser():
    sql = '''
  SELECT 
    id, fname, email
FROM
    academy.User_table;
          '''
          
    result = runGetScript( sql )

    return result


def authUser(username, password):
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
    
    return result