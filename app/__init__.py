from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from flask import session
from flask import jsonify
from flask import json
from werkzeug.utils import secure_filename
import os

# from . import user_module
# from . import course_module

from app.module.user import controller as user_module 
from app.module.course import controller as course_module

from app.module.user.routes import user_api
from app.module.auth.routes import auth_api
from app.module.site.routes import site_api

UPLOAD_FOLDER = 'app/static/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, static_url_path='/public')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'your secret key'
app.register_blueprint(user_api)
app.register_blueprint(auth_api)
app.register_blueprint(site_api)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/catalogoCursos", methods=['GET', 'POST'])
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print("%s %s %s"%(title, category, description))
     
        course_module.createCourse(title, category, description, "public/uploads/"+filename)


        return redirect(f"/catalogoCursos")

    Course = course_module.getAllCourses()


    return render_template("course_module/category_course.html", course=Course)


@app.route("/deleteMaterial")
def deleteMaterial():

    mid = str(request.args.get("id"))
    course_module.deleteMaterialBy(mid)

    return redirect(f"/material")


@app.route("/deleteModule")
def deleteModule():

    mid = str(request.args.get("id"))
    course_module.deleteModuleBy(mid)

    return redirect(f"/modules")

@app.route("/deleteCourse")
def deleteCourse():

    mid = str(request.args.get("id"))
    course_module.deleteCourseBy(mid)

    return redirect(f"/catalogoCursos")


@app.route('/material', methods=['GET', 'POST'])
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

@app.route('/modules', methods=['GET', 'POST'])
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


@app.route("/updateModules", methods=['POST'])
def updateModules():

    if request.method == 'POST':

        title = str(request.form['utitle'])
        course = int(request.form['ucourse'])
        
        price = str(request.form['uprice'])
        uid = str(request.form['uid'])


        print("%s %s %s %s"%(title, course, price, uid))
        course_module.updateModule(course, title, price, uid)

        return redirect(f"/modules")




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        nick_name = str(request.form['nick_name'])
        mail = str(request.form['mail'])
        password = str(request.form['pass'])

        done = user_module.createUser(nick_name, mail, password)
        
        print(done)

        return redirect(f"/")


    return render_template("auth/signup.html")


@app.route("/category_course", methods=['GET'])
def category_course():

    Catalog = course_module.getCategory_course()

    return jsonify( json.dumps([ obj.__dict__ for obj in Catalog] )), 200

@app.route("/getCourseBy", methods=['GET'])
def category_courseBy():

    categoryId = str(request.args.get("categoryId"))

    print(categoryId)

    # Colection = []
    Colection = course_module.getCourseBy(categoryId)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200


@app.route("/getCourseE", methods=['GET'])
def category_courseE():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = course_module.getCourseE(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200




@app.route("/getModuleBy", methods=['GET'])
def get_ModulesBy():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = course_module.getModulesBy(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200


@app.route("/getMaterialBy", methods=['GET'])
def get_MaterialsBy():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = course_module.getMaterialBy(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200



@app.route("/getModuleE", methods=['GET'])
def category_moduleE():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = course_module.getModuleE(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200






@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # User = getAllUser()

    return render_template("Quiz.html")



@app.route("/newCourse", methods=['GET', 'POST'])
def newCourse():    
    if request.method == 'POST':
        return redirect(f"/")

    return render_template("newCourse.html") 


@app.route("/updateCourse", methods=['GET', 'POST'])
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        print("Update Course")

        print(filename)
        answer = course_module.updateCourseCatalog(category, title, description, uid, "public/uploads/"+filename)

        print(answer)
        return redirect(f"/catalogoCursos")


    # return render_template("newCourse.html") 
    return redirect(f"/catalogoCursos")


