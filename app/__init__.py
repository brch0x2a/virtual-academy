from flask import Flask

from app.module.user import controller as user_module 
from app.module.course import controller as course_module

from app.module.user.routes import user_api
from app.module.auth.routes import auth_api
from app.module.site.routes import site_api
from app.module.course.routes import course_api
from app.module.module.routes import module_api
from app.module.lesson.routes import lesson_api
from app.module.category_course.routes import category_course_api
from app.module.branch_of_kwnoledge.routes import branch_of_kwnoledge_api
from app.module.enrollment.routes import enrollment_api

import os
from dotenv import load_dotenv

load_dotenv()

UPLOAD_FOLDER = os.environ.get("APP_UPLOAD_FOLDER")

app = Flask(__name__, static_url_path='/public')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'your secret key'


app.register_blueprint(user_api)
app.register_blueprint(auth_api)
app.register_blueprint(site_api)
app.register_blueprint(branch_of_kwnoledge_api)
app.register_blueprint(course_api)
app.register_blueprint(module_api)
app.register_blueprint(lesson_api)
app.register_blueprint(category_course_api)
app.register_blueprint(enrollment_api)
