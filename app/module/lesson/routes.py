from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from flask import session
from flask import jsonify
from flask import Blueprint
from flask import json
from flask import send_file
from werkzeug.utils import secure_filename

import os
from dotenv import load_dotenv

from app.module.lesson import controller as lesson_module

from app.module.course import controller as course_module

load_dotenv()


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

UPLOAD_FOLDER = os.environ.get("APP_UPLOAD_FOLDER")

lesson_api = Blueprint('lesson_api', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@lesson_api.route('/show/PDFs/')
def send_pdf():
    return send_from_directory(UPLOAD_FOLDER+"docs/", 'Lezione-Cinematica.pdf')



@lesson_api.route("/getLessonBy", methods=['GET'])
def get_LessonsBy():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = lesson_module.getLessonBy(id)

    # return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200
    return jsonify( Colection), 200


@lesson_api.route("/deleteLesson")
def deleteLesson():

    mid = str(request.args.get("id"))
    lesson_module.deleteLessonBy(mid)

    return redirect(f"/lesson")


@lesson_api.route("/deleteModule")
def deleteModule():

    mid = str(request.args.get("id"))
    lesson_module.deleteModuleBy(mid)

    return redirect(f"/modules")

@lesson_api.route("/deleteCourse")
def deleteCourse():

    mid = str(request.args.get("id"))
    #lesson_module.deleteCourseBy(mid)
    course_module.deleteCourseBy(mid)
    #lesson module?? --> it is not sended to course module??

    return redirect(f"/catalogoCursos")


@lesson_api.route('/lesson', methods=['GET', 'POST'])
def lesson():
    if request.method == 'POST':

        module = str(request.form['module'])
        title = str(request.form['title'])
        video = str(request.form['video'])


        if 'file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)

        file = request.files['file']

        filename = ""
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER+"docs", filename))
        # print("%s %s %s"%(title, category, description))
    

        # print("%s %s %s %s"%(module, title, video, filename))
        lesson_module.createLesson(module, title, video, filename)
        
        return redirect(f"/lesson")

    Lesson = lesson_module.getAllLesson()

    return render_template("course_module/lesson.html", lesson=Lesson, upload_folder="public/uploads/")