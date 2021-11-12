from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from flask import session
from flask import jsonify
from flask import Blueprint
from flask import json
from werkzeug.utils import secure_filename

import os
from dotenv import load_dotenv

from app.module.module import controller as module_module

load_dotenv()


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

UPLOAD_FOLDER = os.environ.get("APP_UPLOAD_FOLDER")

module_api = Blueprint('module_api', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@module_api.route("/getModuleE", methods=['GET'])
def category_moduleE():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = module_module.getModuleE(id)

    # return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200
    return jsonify( Colection ), 200


@module_api.route('/modules', methods=['GET', 'POST'])
def modules():
    if request.method == 'POST':

        course = str(request.form['course'])
        title = str(request.form['title'])
        price = str(request.form['price'])


        # print("%s %s %s"%(course, title, price))
        done = module_module.createModule(course, title, price)
        # print(done)

        return redirect(f"/modules")

    Modules = module_module.getAllModules()

    return render_template("course_module/modules.html", modules=Modules)


@module_api.route("/updateModules", methods=['POST'])
def updateModules():

    if request.method == 'POST':

        title = str(request.form['utitle'])
        course = int(request.form['ucourse'])
        
        price = str(request.form['uprice'])
        uid = str(request.form['uid'])


        print("%s %s %s %s"%(title, course, price, uid))
        module_module.updateModule(course, title, price, uid)

        return redirect(f"/modules")






@module_api.route("/getModuleBy", methods=['GET'])
def get_ModulesBy():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = module_module.getModulesBy(id)

    # return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200
    return jsonify( Colection ), 200

@module_api.route("/branch_of_knowledge", methods=['GET'])
def brach_of_knowledge():
    return render_template("course_module/branch_of_knowledge.html")
    


