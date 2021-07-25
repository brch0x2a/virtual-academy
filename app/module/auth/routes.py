from flask import Blueprint, jsonify, json, render_template, redirect
from flask import request
from flask import session


from app.module.user import controller as user_module 
from app.module.course import controller as course_module


auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        user = str(request.form['user'])
        password = str(request.form['password'])

        print("login")

        access =  user_module.authUser(user, password)
        msg = "credenciales incorrectas"

        if access:
            session['loggedin'] = True
            session['id'] = access[0]
            session['username'] = access[1]

            return redirect(f"/home")
        else:
            return render_template("auth/login.html", msg=msg)


    return render_template("auth/login.html")




@auth_api.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    return redirect(f"/")