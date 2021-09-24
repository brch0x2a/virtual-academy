from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from flask import session
from flask import jsonify
from flask import Blueprint
from flask import json
from werkzeug.utils import secure_filename

import os
from dotenv import load_dotenv

from app.module.enrollment import controller as enrollment_module
from app.module.branch_of_kwnoledge import controller as branch_of_kwnoledge_module

# from app.module.course import controller as course_module
# from app.module.user import controller as user_module 

load_dotenv()

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

UPLOAD_FOLDER = os.environ.get("APP_UPLOAD_FOLDER")

enrollment_api = Blueprint('enrollment_api', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@enrollment_api.route("/enrollment_all", methods=['GET'])
def enrollment_all():

    Colection = enrollment_module.get_all()

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200




@enrollment_api.route("/enrollment_grid", methods=['GET'])
def grid():
    id_branch = str(request.args.get("id_branch"))

    Branch = branch_of_kwnoledge_module.getE(id_branch)

    branchE = {}

    for e in Branch:
        branchE = e

    print(branchE)

    Colection = enrollment_module.grid(id_branch)

    transform = [[ row.__dict__ for row in obj.course_colection ] for obj in Colection.colection ] 

    print("\033[32;1m %s\t%s  \033[0m\n\n"%(type(transform), transform))

    # return jsonify(json.dumps(transform))
    return render_template("site/grid.html", grid=transform, branch=branchE)



    
@enrollment_api.route("/get_enrollment_grid", methods=['GET'])
def get_grid():
    id_branch = str(request.args.get("id_branch"))

    Colection = enrollment_module.grid(id_branch)

    transform = [[ row.__dict__ for row in obj.course_colection ] for obj in Colection.colection ] 

    print("\033[32;1m %s\t%s  \033[0m\n\n"%(type(transform), transform))

    return jsonify(json.dumps(transform))
    # return render_template("site/grid.html")