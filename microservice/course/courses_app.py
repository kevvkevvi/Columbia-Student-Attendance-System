from flask import Flask, Response, request
from datetime import datetime
import json
from columbia_courses_resource import ColumbiaCoursesResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(
    __name__,
    static_url_path="/",
    static_folder="static/class-ui/",
    template_folder="web/templates",
)

CORS(app)


@app.route("/section/no/<no>", methods=["GET"])
def get_section_by_key(no):

    result = ColumbiaCoursesResource.get_section_by_key(no)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/section/name/<name>", methods=["GET"])
def get_section_by_name(name):

    result = ColumbiaCoursesResource.get_section_by_name(name)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/enrollments/no/<no>", methods=["GET"])
def get_enrollments_by_no(no):

    result = ColumbiaCoursesResource.get_enrollments_by_no(no)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/enrollments/uni/<uni>", methods=["GET"])
def get_enrollments_by_uni(uni):

    result = ColumbiaCoursesResource.get_enrollments_by_uni(uni)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/sections", methods=["POST"])
def add_section():
    data = request.get_json()
    result = ColumbiaCoursesResource.add_section(
        data["call_no"], data["course_name"], data["enrollment_number"]
    )

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application/json")
    else:
        rsp = Response("FAIL", status=400, content_type="text/plain")

    return rsp


@app.route("/api/sections/no/<no>", methods=["DELETE"])
def delete_section(no):

    result = ColumbiaCoursesResource.delete_section(no)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")

    return rsp


@app.route("/api/sections/edit", methods=["POST"])
def update_section_name():

    data = request.form
    result = ColumbiaCoursesResource.update_section_name(
        data["call_no"], data["course_name"]
    )

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")

    return rsp


@app.route("/api/enrollments", methods=["POST"])
def add_enrollment():

    data = request.form
    result = ColumbiaCoursesResource.add_enrollment(data["call_no"], data["uni"])

    # number of affected rows
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")

    return rsp


@app.route("/api/enrollments/no&uni", methods=["DELETE"])
def delete_enrollment():

    data = request.form
    result = ColumbiaCoursesResource.delete_enrollment(data["call_no"], data["uni"])

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
