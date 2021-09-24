from flask import Blueprint, jsonify, json, render_template, redirect
from flask import request
from flask import session


from app.module.user import controller as user_module 
from app.module.course import controller as course_module
from app.module.branch_of_kwnoledge import controller as branch_of_kwnoledge_module


site_api = Blueprint('site_api', __name__)

@site_api.route('/', methods=['GET', 'POST'])
def index():


    # return render_template("site/index.html")
    return redirect(f"/login")



@site_api.route("/home")
def home():

    if 'loggedin' in session:

        Branch = branch_of_kwnoledge_module.get_all()


        return render_template("site/home.html", username=session["username"], branch=Branch)
    
    return redirect(f"/")



@site_api.route("/category_library")
def category_library():

    if 'loggedin' in session:

        id = str(request.args.get("id"))
        Branch = branch_of_kwnoledge_module.get_all()
         
        return
        # return render_template("site/home.html", username=session["username"], branch=Branch)
    
    return redirect(f"/")