from app.module.common.db.consumer import runGetScript, runUpdateScript

from app.module.lesson.models import Lesson

def createLesson(module, title, filepath, reading):
    title = str(title)

    print("\033[092m INSERT \033[0m")

    sql = "INSERT INTO Lesson(id_module, title, filepath, reading_path)"\
        "Values(%s, %s, %s, %s)"

    result = runUpdateScript( sql, (module, title, filepath, reading) )

    return result


def getAllLesson():

    sql = '''
        SELECT 
            M.id,
            Cc.name,
            Cs.title,
            Cs.description,
            Md.title,
            M.title,
            M.filepath,
            M.reading_path
        FROM
            Lesson M
                INNER JOIN
            Module Md ON Md.id = M.id_module
                INNER JOIN
            Course Cs ON Cs.id = Md.id_course
                INNER JOIN
            Category_course Cc ON Cc.id = Cs.id_category;
          '''

    result = runGetScript( sql )

    return result




def getLessonBy(moduleId):

    sql = '''
        SELECT 
            M.id,
            Cc.name,
            Cs.title,
            Cs.description,
            Md.title,
            M.title,
            M.filepath,
            M.reading_path
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

    result = runGetScript( sql, (moduleId) )

    return result



def deleteLessonBy(id):
    sql = '''            
            DELETE FROM Lesson 
                WHERE
                id = %s;
          '''

    result = runUpdateScript( sql, (id) )

    return result