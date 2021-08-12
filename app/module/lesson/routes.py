@course_api.route("/getLessonBy", methods=['GET'])
def get_LessonsBy():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = course_module.getLessonBy(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200

