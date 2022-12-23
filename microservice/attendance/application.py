################################################
#  Third MicroService
#  Attendance
#  sections(call_no, course_name, enrollment_number)
#  class(call_no, date, attendance)
#  students(UNI, call_no, date)
#  By Yipeng Geng, yg2913
################################
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
def get_sections():  # get all sections or by query strings (pagination supported)
    result = DBResource().get_sections(request.args.to_dict())
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/class", methods=["GET"])
def get_classes():  # get all classes or by query strings (pagination supported)
    result = DBResource().get_classes(request.args.to_dict())
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/students", methods=["GET"])
def get_students():  # get all students or by query strings (pagination supported)
    result = DBResource().get_students(request.args.to_dict())
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/sections/<call_no>", methods=["GET"])
def get_section(call_no):  # get section by primary key
    result = DBResource().get_section(call_no)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
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


@app.route("/api/sections/<call_no>/class/<date>", methods=["PUT"])
def update_section_attendance(call_no, date): # Retrieve the current attendance record
    attendance_record = DBResource().get_section_attendance(call_no, date)
    attendance_record['attendance'] += 1  # Increment the attendance count
    DBResource().update_section_attendance(call_no, date, attendance_record) # Update the attendance record in the database
    return "SUCCESS"


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


@app.route("/api/sections", methods=["POST"])
def add_section():  # add a new section
    data = request.form
    result = DBResource().add_section(data['call_no'], data['course_name'], data['enrollment_number'])
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    print(rsp)
    return rsp


@app.route("/api/class", methods=["POST"])
def add_class():  # a section adds a new class
    data = request.form
    result = DBResource().add_class(data['call_no'], data['date'], data['attendance'])
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp


@app.route("/api/students", methods=["POST"])
def add_student():  # a student attend a class, the class's attendance number increase 1
    data = request.form
    print(data)
    result = DBResource().add_student(data['uni'], data['call_no'], data['date'], increase_attendance=True)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp


@app.route("/api/sections", methods=["DELETE"])
def delete_section():  # delete a section
    data = request.form
    result = DBResource().delete_section(data['call_no'])
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp


@app.route("/api/class", methods=["DELETE"])
def delete_class():  # delete a class
    data = request.form
    result = DBResource().delete_class(data['call_no'], data['date'])
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp

@app.route("/api/students", methods=["DELETE"])
def delete_student():  # delete a student, the class's attendance decrease 1
    data = request.form
    result = DBResource().delete_student(data['uni'], data['call_no'], data['date'], decrease_attendance=True)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp


@app.route("/api/sections/edit_enrollment_number", methods=["POST"])
def update_section_enrollment():  # update a section's enrollment_number
    data = request.form
    result = DBResource().update_section_enrollment(data['call_no'], data['enrollment_number'])
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp

@app.route("/api/sections/edit_course_name", methods=["POST"])
def update_section_name():  # update a section's course_name
    data = request.form
    result = DBResource().update_section_name(data['call_no'], data['course_name'])
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp


@app.route("/api/class/edit_attendance", methods=["POST"])
def update_class_attendance():  # update a class's attendance
    data = request.form
    result = DBResource().update_class_attendance(data['call_no'], data['date'], data['attendance'])
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
