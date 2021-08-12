@course_api.route("/getModuleE", methods=['GET'])
def category_moduleE():

    id = str(request.args.get("id"))

    print(id)

    # Colection = []
    Colection = course_module.getModuleE(id)

    return jsonify( json.dumps([ obj.__dict__ for obj in Colection] )), 200
