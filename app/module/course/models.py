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
    def __init__(self, id, category,  course, description, title, price):
        self.id = id 
        self.course = course
        self.category = category
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