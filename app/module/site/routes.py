from flask import Blueprint, jsonify, json, render_template, redirect
from flask import request
from flask import session


from app.module.user import controller as user_module 
from app.module.course import controller as course_module


site_api = Blueprint('site_api', __name__)

@site_api.route('/', methods=['GET', 'POST'])
def index():


    return redirect(f"/login")



@site_api.route("/home")
def home():

    if 'loggedin' in session:

        Course = course_module.getAllCourses()


        return render_template("site/home.html", username=session["username"], course=Course)
    
    return redirect(f"/")

