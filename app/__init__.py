from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from flask import session
from flask import jsonify
from flask import json
from werkzeug.utils import secure_filename
import os

# from . import module_user
# from . import module_course

from app.module.user import controller as module_user 
from app.module.course import controller as module_course


UPLOAD_FOLDER = 'app/static/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, static_url_path='/public')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'your secret key'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        user = str(request.form['user'])
        password = str(request.form['password'])

        print("login")

        access =  module_user.authUser(user, password)
        msg = "credenciales incorrectas"

        if access:
            session['loggedin'] = True
            session['id'] = access[0]
            session['username'] = access[1]

            return redirect(f"/home")
        else:
            return render_template("index.html", msg=msg)


    return render_template("index.html")


@app.route("/home")
def home():

    if 'loggedin' in session:

        Course = module_course.getAllCourses()


        return render_template("home.html", username=session["username"], course=Course)
    
    return redirect(f"/")

@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    return redirect(f"/")

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
     
        module_course.createCourse(title, category, description, "public/uploads/"+filename)


        return redirect(f"/catalogoCursos")

    Course = module_course.getAllCourses()


    return render_template("module_course/category_course.html", course=Course)


@app.route("/deleteMaterial")
def deleteMaterial():

    mid = str(request.args.get("id"))
    module_course.deleteMaterialBy(mid)

    return redirect(f"/material")


@app.route("/deleteModule")
def deleteModule():

    mid = str(request.args.get("id"))
    module_course.deleteModuleBy(mid)

    return redirect(f"/modules")

@app.route("/deleteCourse")
def deleteCourse():

    mid = str(request.args.get("id"))
    module_course.deleteCourseBy(mid)

    return redirect(f"/catalogoCursos")


@app.route('/material', methods=['GET', 'POST'])
def material():
    if request.method == 'POST':

        module = str(request.form['module'])
        title = str(request.form['title'])
        video = str(request.form['video'])

        print("%s %s %s"%(module, title, video))
        done = module_course.createMaterial(module, title, video)
        print(done)

        return redirect(f"/material")

    Material = module_course.getAllMaterial()

    return render_template("module_course/material.html", material=Material)

@app.route('/modules', methods=['GET', 'POST'])
def modules():
    if request.method == 'POST':

        course = str(request.form['course'])
        title = str(request.form['title'])
        price = str(request.form['price'])


        # print("%s %s %s"%(course, title, price))
        done = module_course.createModule(course, title, price)
        # print(done)

        return redirect(f"/modules")

    Modules = module_course.getAllModules()

    return render_template("module_course/modules.html", modules=Modules)


@app.route("/updateModules", methods=['POST'])
def updateModules():

    if request.method == 'POST':

        title = str(request.form['utitle'])
        course = int(request.form['ucourse'])
        
        price = str(request.form['uprice'])
        uid = str(request.form['uid'])


        print("%s %s %s %s"%(title, course, price, uid))
        module_course.updateModule(course, title, price, uid)

        return redirect(f"/modules")




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        nick_name = str(request.form['nick_name'])
        mail = str(request.form['mail'])
        password = str(request.form['pass'])

        done = module_user.createUser(nick_name, mail, password)
        
        print(done)

        return redirect(f"/")


    return render_template("auth/signup.html")


@app.route("/category_course", methods=['GET'])
def category_course():

    Catalog = module_course.getCategory_course()

    return jsonify( json.dumps([ obj.__dict__ for obj in Catalog] )), 200

@app.route("/getCourseBy", methods=['GET'])
def category_courseBy():

    categoryId = str(request.args.get("categoryId"))

    print(categoryId)

    # Colection = []
    Colection = module_course.getCourseBy(categoryId)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200


@app.route("/getCourseE", methods=['GET'])
def category_courseE():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = module_course.getCourseE(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200




@app.route("/getModuleBy", methods=['GET'])
def get_ModulesBy():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = module_course.getModulesBy(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200


@app.route("/getMaterialBy", methods=['GET'])
def get_MaterialsBy():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = module_course.getMaterialBy(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200



@app.route("/getModuleE", methods=['GET'])
def category_moduleE():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = module_course.getModuleE(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200



@app.route('/users', methods=['GET', 'POST'])
def allUser():
    User = module_user.getAllUser()

    return render_template("User.html", users=User)


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
        answer = module_course.updateCourseCatalog(category, title, description, uid, "public/uploads/"+filename)

        print(answer)
        return redirect(f"/catalogoCursos")


    # return render_template("newCourse.html") 
    return redirect(f"/catalogoCursos")


