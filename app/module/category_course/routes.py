from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from flask import session
from flask import jsonify
from flask import Blueprint
from flask import json
from werkzeug.utils import secure_filename

import os
from dotenv import load_dotenv

from app.module.category_course import controller as category_course_module


load_dotenv()


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

UPLOAD_FOLDER = os.environ.get("APP_UPLOAD_FOLDER")

category_course_api = Blueprint('category_course_api', __name__)

@category_course_api.route("/category_course_collection", methods=['GET', 'POST'])
def category_course_collection():

    if request.method == "POST":
        name = str(request.form['title'])
        id_branch = str(request.form['branch'])

     
        category_course_module.create(name, id_branch)

        return redirect(f"/category_course_collection")

    Branch = category_course_module.get_all()

    return render_template("course_module/category_course_collection.html", branch=Branch)



@category_course_api.route("/category_course", methods=['GET'])
def category_course():

    Catalog = category_course_module.get_all()

    # return jsonify( json.dumps([ obj.__dict__ for obj in Catalog] )), 200
    return jsonify( Catalog ), 200



@category_course_api.route("/getCategoryCourseE", methods=['GET'])
def category_courseE():

    id = str(request.args.get("id"))

    print("id-->>", id)

    # Colection = []
    Colection = category_course_module.getE(id)
    
    print("Colection-->>", Colection)

    return jsonify( Colection ), 200


# @category_course_api.route("/getCategoryCourseBy", methods=['GET'])
# def category_courseBy():

#     id_branch = str(request.args.get("id_branch"))

#     print("id-->>", id_branch)
#     Colection = []
#     Colection = category_course_module.filterBy(id_branch)

#     return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200


@category_course_api.route("/update_category_course", methods=['POST'])
def update_category_course():

    if request.method == 'POST':

        name = str(request.form['utitle'])
        uid = str(request.form['uid'])
        branch = str(request.form['ubranch'])

        category_course_module.update(uid, name, branch)

        return redirect(f"/category_course_collection")


@category_course_api.route("/delete_category_course")
def delete_category_course():

    mid = str(request.args.get("id"))
    category_course_module.delete(mid)

    return redirect(f"/category_course_collection")