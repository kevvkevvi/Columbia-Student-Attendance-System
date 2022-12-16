from flask import Flask, Response, request
import datetime
import json
from DBResource import *
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


@app.route("/api/sections", methods=["GET"])
def get_all_sections():  # get all sections
    result = DBResource().get_sections()
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/class", methods=["GET"])
def get_all_classes():  # get all classes
    result = DBResource().get_classes()
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/students", methods=["GET"])
def get_all_students():  # get all students
    result = DBResource().get_students()
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/sections/<call_no>", methods=["GET"])
def get_section_by_call_no(call_no):  # get section <call_no>'s course_name and enrollment
    result = DBResource().get_section(call_no)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/sections/<call_no>/class/", methods=["GET"])
def get_section_attendances(call_no):  # get section <call_no>'s classes' date and attendance
    result = DBResource().get_section_attendances(call_no)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/sections/<call_no>/class/<date>", methods=["GET"])
def get_section_attendance(call_no, date):  # get <call_no>'s attendance on <date>
    result = DBResource().get_section_attendance(call_no, date)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/sections/<call_no>/class/<date>/students/", methods=["GET"])
def get_section_class_students(call_no, date):  # get all students' attendance records on <call_no><date>
    result = DBResource().get_section_class_students(call_no, date)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/sections/<call_no>/class/<date>/students/<uni>", methods=["GET"]) 
def get_section_class_student(call_no, date, uni):  # get <uni>'s attendance record on <call_no><date>
    result = DBResource().get_section_class_student(call_no, date, uni)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/sections/<call_no>/students/", methods=["GET"])
def get_section_students(call_no, uni):  # get all students attendance records of <call_no>
    result = DBResource().get_section_students(call_no)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/sections/<call_no>/students/<uni>", methods=["GET"])
def get_section_student(call_no, uni):  # get <uni> attendance records of <call_no>
    result = DBResource().get_section_student(call_no, uni)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
