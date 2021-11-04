from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from flask import session
from flask import jsonify
from flask import Blueprint
from flask import json
from werkzeug.utils import secure_filename

import os
from dotenv import load_dotenv

from app.module.branch_of_kwnoledge import controller as branch_of_kwnoledge_module

load_dotenv()

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'svg'}

UPLOAD_FOLDER = os.environ.get("APP_UPLOAD_FOLDER")

branch_of_kwnoledge_api = Blueprint('branch_of_kwnoledge_api', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@branch_of_kwnoledge_api.route("/branch_of_kwnoledge_all", methods=['GET'])
def branch_of_kwnoledge_all():

    Branch = branch_of_kwnoledge_module.get_all()

    return jsonify( Branch ), 200

@branch_of_kwnoledge_api.route("/branch_of_kwnoledge", methods=['GET', 'POST'])
def branch_of_kwnoledge_catalog():

    if request.method == "POST":
        title = str(request.form['title'])

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
     
        branch_of_kwnoledge_module.create(title, "public/uploads/"+filename)

        return redirect(f"/branch_of_kwnoledge")

    Branch = branch_of_kwnoledge_module.get_all()

    return render_template("course_module/branch_of_kwnoledge.html", branch=Branch)




@branch_of_kwnoledge_api.route("/delete_branch_of_kwnoledge")
def delete_branch_of_kwnoledge():

    mid = str(request.args.get("id"))
    branch_of_kwnoledge_module.delete(mid)

    return redirect(f"/branch_of_kwnoledge")


@branch_of_kwnoledge_api.route("/branch_of_kwnoledgeE", methods=['GET'])
def get_branch_of_kwnoledgeE():

    id = str(request.args.get("id"))

    # print("ID ON EDIT BE",id)

    # Colection = []
    Colection = branch_of_kwnoledge_module.getE(id)

    return jsonify( Colection ), 200


@branch_of_kwnoledge_api.route("/update_branch_of_kwnoledge", methods=['POST'])
def update_branch_of_kwnoledge():

    if request.method == 'POST':

        name = str(request.form['utitle'])
        uid = str(request.form['uid'])

        print(name+" ==> "+uid)

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        # print("Input value : ", file)

        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        
        if file:
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                filename = "public/uploads/"+filename

        branch_of_kwnoledge_module.update(uid, name, (filename if file else ''))

        return redirect(f"/branch_of_kwnoledge")
