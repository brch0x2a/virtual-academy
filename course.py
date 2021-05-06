import pymysql

IP = "localhost"
PASS = "wrf!C:w(>7:&"


db = pymysql.connect(IP, "brch", PASS, "academy")


class Category_course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Course:
    def __init__(self, id, category, title, description, image):
        self.id = id
        self.title  = title
        self.category = category 
        self.description = description
        self.image = image 


class Module:
    def __init__(self, id, course, description, title, price):
        self.id = id 
        self.course = course
        self.description = description
        self.title = title 
        self.price = price


class Material:
    def __init__(self, id, category, course, description, module, title, filepath):
        self.id = id 
        self.category = category
        self.course = course
        self.description = description
        self.module = module
        self.title = title 
        self.filepath = filepath


def getCategory_course():
    Catalog = []
    db = pymysql.connect(IP, "brch", PASS, "academy")
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
    db = pymysql.connect(IP, "brch", PASS, "academy")

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
    db = pymysql.connect(IP, "brch", PASS, "academy")
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


def getAllModules():
    Modules = []
    db = pymysql.connect(IP, "brch", PASS, "academy")
    cursor = db.cursor()

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

    cursor.execute(sql)

    cursor.close()

    result = cursor.fetchall()
    print(len(result))

    for e in result:

        Modules.append(Module(e[0], e[1], e[2], e[3], e[4]))

    db.close()

    return Modules



def getCourseBy(categoryId):
    Courses = []
    db = pymysql.connect(IP, "brch", PASS, "academy")
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
    print(len(result))

    for e in result:

        Courses.append(Course(e[0], e[1], e[2], e[3], e[4]))


    db.close()

    return Courses



def getCourseE(id):
    Courses = []
    db = pymysql.connect(IP, "brch", PASS, "academy")
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


def createModule(course, title, price):
    db = pymysql.connect(IP, "brch", PASS, "academy")

    title = str(title)


    cursor = db.cursor()

    sql = "INSERT INTO Module(id_course, title, price)"\
        "Values(%s, %s, %s)"

    cursor.execute(sql, (course, title, price))

    db.commit()

    cursor.close()

    db.close()

    return "Listo"


def updateModule(course, title, price):
    db = pymysql.connect(IP, "brch", PASS, "academy")

    title = str(title)


    cursor = db.cursor()

    sql = "Update INTO Module(id_course, title, price)"\
        "Values(%s, %s, %s)"

    cursor.execute(sql, (course, title, price))

    db.commit()

    cursor.close()

    db.close()

    return "Listo"





def getAllMaterial():
    Materials = []
    db = pymysql.connect(IP, "brch", PASS, "academy")
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
            Material M
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

        Materials.append(Material(e[0], e[1], e[2], e[3], e[4], e[5], e[6]))


    db.close()

    return Materials



def updateCourseCatalog(category, title, description, uid):
    db = pymysql.connect(IP, "brch", PASS, "academy")

    title = str(title)
    category = str(category)
    description = str(description)
    uid = str(uid)


    print("id:%s\t t: %s c: %s d:%s"%(uid, title, category, description))


    cursor = db.cursor()

    sql = ''' 
            UPDATE Course 
            SET 
                id_category = %s,
                title = %s,
                description = %s
            WHERE
                id = %s
    '''

    cursor.execute(sql, (category, title, description, uid))

    db.commit()

    cursor.close()

    db.close()

    return "Listo"




def deleteMaterialBy(id):


    db = pymysql.connect(IP, "brch", PASS, "academy")
    cursor = db.cursor()


    sql = '''            
            DELETE FROM Material 
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



def deleteModuleBy(id):


    db = pymysql.connect(IP, "brch", PASS, "academy")
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


    db = pymysql.connect(IP, "brch", PASS, "academy")
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