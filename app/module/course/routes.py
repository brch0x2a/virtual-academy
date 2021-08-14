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


@course_api.route("/deleteLesson")
def deleteLesson():

    mid = str(request.args.get("id"))
    course_module.deleteLessonBy(mid)

    return redirect(f"/lesson")


@course_api.route("/deleteModule")
def deleteModule():

    mid = str(request.args.get("id"))
    course_module.deleteModuleBy(mid)

    return redirect(f"/modules")

@course_api.route("/deleteCourse")
def deleteCourse():

    mid = str(request.args.get("id"))
    course_module.deleteCourseBy(mid)

    return redirect(f"/catalogoCursos")


@course_api.route('/lesson', methods=['GET', 'POST'])
def lesson():
    if request.method == 'POST':

        module = str(request.form['module'])
        title = str(request.form['title'])
        video = str(request.form['video'])

        print("%s %s %s"%(module, title, video))
        done = course_module.createLesson(module, title, video)
        print(done)

        return redirect(f"/lesson")

    Lesson = course_module.getAllLesson()

    return render_template("course_module/lesson.html", lesson=Lesson)

@course_api.route('/modules', methods=['GET', 'POST'])
def modules():
    if request.method == 'POST':

        course = str(request.form['course'])
        title = str(request.form['title'])
        price = str(request.form['price'])


        # print("%s %s %s"%(course, title, price))
        done = course_module.createModule(course, title, price)
        # print(done)

        return redirect(f"/modules")

    Modules = course_module.getAllModules()

    return render_template("course_module/modules.html", modules=Modules)


@course_api.route("/updateModules", methods=['POST'])
def updateModules():

    if request.method == 'POST':

        title = str(request.form['utitle'])
        course = int(request.form['ucourse'])
        
        price = str(request.form['uprice'])
        uid = str(request.form['uid'])


        print("%s %s %s %s"%(title, course, price, uid))
        course_module.updateModule(course, title, price, uid)

        return redirect(f"/modules")



@course_api.route("/getModuleBy", methods=['GET'])
def get_ModulesBy():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = course_module.getModulesBy(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200

@course_api.route("/branch_of_knowledge", methods=['GET'])
def brach_of_knowledge():
    return render_template("course_module/branch_of_knowledge.html")
    




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

