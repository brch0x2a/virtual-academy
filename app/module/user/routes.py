from flask import Blueprint, jsonify, json, render_template


from .controller import getAllUser

user_api = Blueprint('user_api', __name__)

@user_api.route('/users', methods=['GET', 'POST'])
def allUser():
    All = getAllUser()
    print("fuck yeah")

    # return jsonify( json.dumps([ obj.__dict__ for obj in All] )), 200

    return render_template("user_module/user.html", users=All)