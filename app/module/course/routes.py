from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from flask import session
from flask import jsonify
from flask import Blueprint
from flask import json
from werkzeug.utils import secure_filename

import os
from dotenv import load_dotenv

from app.module.course import controller as course_module
from app.module.user import controller as user_module 

load_dotenv()


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

UPLOAD_FOLDER = os.environ.get("APP_UPLOAD_FOLDER")

course_api = Blueprint('course_api', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@course_api.route("/getCourseBy", methods=['GET'])
def category_courseBy():

    categoryId = str(request.args.get("categoryId"))

    print(categoryId)

    # Colection = []
    Colection = course_module.getCourseBy(categoryId)

    # return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200
    return jsonify(Colection), 200

@course_api.route("/getCourseById", methods=['GET'])
def courseById():

    courseId = str(request.args.get("courseId"))

    print(courseId)

    # Colection = []
    Colection = course_module.getCourseById(courseId)

    # return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200
    return jsonify(Colection), 200



@course_api.route("/getCourseByBranch", methods=['GET'])
def category_courseByBranch():

    branch_id = str(request.args.get("id_branch"))

    print(branch_id)

    # Colection = []
    Colection = course_module.getCourseByBranch(branch_id)

    return jsonify( Colection ), 200




@course_api.route("/catalogoCursos", methods=['GET', 'POST'])
def catalogoCursos():

    if request.method == "POST":
        title = str(request.form['title'])
        category = int(request.form['category'])
        description = str(request.form['description'])

        if 'file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            file.save(os.path.join(UPLOAD_FOLDER, filename))
        # print("%s %s %s"%(title, category, description))
     
        course_module.createCourse(title, category, description, "public/uploads/"+filename)


        return redirect(f"/catalogoCursos")

    Course = course_module.getAllCourses()


    return render_template("course_module/category_course.html", course=Course)




@course_api.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # User = getAllUser()

    return render_template("course_module/quiz.html")



@course_api.route("/newCourse", methods=['GET', 'POST'])
def newCourse():    
    if request.method == 'POST':
        return redirect(f"/")

    return render_template("newCourse.html") 


@course_api.route("/updateCourse", methods=['GET', 'POST'])
def updateCourse():

    if request.method == 'POST':

        title = str(request.form['utitle'])
        category = int(request.form['ucategory'])
        description = str(request.form['udescription'])
        uid = str(request.form['uid'])

        # print("id:%s\t t: %s c: %s d:%s"%(id, title, category, description))

        if 'file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        print("Update Course")

        print(filename)
        answer = course_module.updateCourseCatalog(category, title, description, uid, "public/uploads/"+filename)

        print(answer)
        return redirect(f"/catalogoCursos")


    # return render_template("newCourse.html") 
    return redirect(f"/catalogoCursos")

