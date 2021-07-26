from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from flask import session
from flask import jsonify
from flask import Blueprint
from flask import json
from werkzeug.utils import secure_filename
import os

from app.module.course import controller as course_module
from app.module.user import controller as user_module 



ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


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
            file.save(os.path.join(course_api.config['UPLOAD_FOLDER'], filename))
        # print("%s %s %s"%(title, category, description))
     
        course_module.createCourse(title, category, description, "public/uploads/"+filename)


        return redirect(f"/catalogoCursos")

    Course = course_module.getAllCourses()


    return render_template("course_module/category_course.html", course=Course)


@course_api.route("/deleteMaterial")
def deleteMaterial():

    mid = str(request.args.get("id"))
    course_module.deleteMaterialBy(mid)

    return redirect(f"/material")


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


@course_api.route('/material', methods=['GET', 'POST'])
def material():
    if request.method == 'POST':

        module = str(request.form['module'])
        title = str(request.form['title'])
        video = str(request.form['video'])

        print("%s %s %s"%(module, title, video))
        done = course_module.createMaterial(module, title, video)
        print(done)

        return redirect(f"/material")

    Material = course_module.getAllMaterial()

    return render_template("course_module/material.html", material=Material)

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


@course_api.route("/category_course", methods=['GET'])
def category_course():

    Catalog = course_module.getCategory_course()

    return jsonify( json.dumps([ obj.__dict__ for obj in Catalog] )), 200

@course_api.route("/getCourseBy", methods=['GET'])
def category_courseBy():

    categoryId = str(request.args.get("categoryId"))

    print(categoryId)

    # Colection = []
    Colection = course_module.getCourseBy(categoryId)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200


@course_api.route("/getCourseE", methods=['GET'])
def category_courseE():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = course_module.getCourseE(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200


@course_api.route("/getModuleBy", methods=['GET'])
def get_ModulesBy():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = course_module.getModulesBy(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200


@course_api.route("/getMaterialBy", methods=['GET'])
def get_MaterialsBy():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = course_module.getMaterialBy(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200



@course_api.route("/getModuleE", methods=['GET'])
def category_moduleE():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = course_module.getModuleE(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200



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
            file.save(os.path.join(course_api.config['UPLOAD_FOLDER'], filename))

        print("Update Course")

        print(filename)
        answer = course_module.updateCourseCatalog(category, title, description, uid, "public/uploads/"+filename)

        print(answer)
        return redirect(f"/catalogoCursos")


    # return render_template("newCourse.html") 
    return redirect(f"/catalogoCursos")

