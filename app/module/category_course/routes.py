@course_api.route("/category_course", methods=['GET'])
def category_course():

    Catalog = course_module.getCategory_course()

    return jsonify( json.dumps([ obj.__dict__ for obj in Catalog] )), 200

@course_api.route("/getCourseBy", methods=['GET'])
def category_courseBy():

    categoryId = str(request.args.get("categoryId"))

    print(categoryId)

    # Colection = []
    Colection = course_module.getCourseBy(categoryId)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200


@course_api.route("/getCourseE", methods=['GET'])
def category_courseE():

    id = str(request.args.get("id"))

    print(id)
    # Colection = []
    Colection = course_module.getCourseE(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200
