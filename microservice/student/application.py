from flask import Flask, Response, request
from datetime import datetime
import json
from columbia_students_resource import ColumbiaStudentsResource
from flask_cors import CORS

# Create the Flask application object.
application = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(application)


@application.route("/student/<uni>", methods=["GET"])
def get_student_by_key(uni):

    result = ColumbiaStudentsResource.get_student_by_key(uni)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/api/student", methods=["POST"])
def add_section():

    data = request.form
    result = ColumbiaStudentsResource.add_student(data['UNI'], data['first_name'], data['last_name'], data['email'])

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000)

