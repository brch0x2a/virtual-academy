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
        print("Object: ",access)
        msg = "credenciales incorrectas"

        if access:
            session['loggedin'] = True
            session['id'] = access['id']
            session['username'] = access['fname']

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


@auth_api.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        nick_name = str(request.form['nick_name'])
        mail = str(request.form['mail'])
        password = str(request.form['pass'])

        done = user_module.createUser(nick_name, mail, password)
        
        print(done)

        return redirect(f"/")


    return render_template("auth/signup.html")