class Enrollment:
    def __init__(self, id, id_course, image, title, description, email, enrollment_date):
        self.id = id
        self.id_course  = id_course
        self.image = image 
        self.title = title
        self.description = description
        self.email = email 
        self.enrollment_date = enrollment_date

class Holder:

    def __init__(self, category):

        self.category = category
        self.course_colection = []
        
class Grid:

    def __init__(self):

        self.colection = []
