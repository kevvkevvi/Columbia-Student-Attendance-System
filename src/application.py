from flask import Flask, Response, request
import datetime
import json
from db_resource import DbResource
from flask_cors import CORS



# Create the Flask application object.
# frontend not found
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


@app.route("/sections", methods=["POST"])
def add_section(): # add a new section
    data = request.get_json()
    result = DbResource().add_section(
        data["call_no"], data["course_name"], data["enrollment_number"]
    )

    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application/json")
    else:
        rsp = Response("FAIL", status=400, content_type="text/plain")

    return rsp

@app.route("/sections", methods=["GET"])
def get_sections():  # get all sections or by query strings (pagination supported)
    result = DbResource().get_sections(request.args.to_dict())
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/sections/<call_no>", methods=["GET"])
def get_section_by_key(call_no):  # get section by primary key
    result = DbResource().get_section_by_key(call_no)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/sections/name/<name>", methods=["GET"])
def get_section_by_name(name):

    result = DbResource().get_section_by_name(name)

    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

# @app.route("/sections/edit_name", methods=["PUT"])
# def update_section_name(): # update a section's name
#
#     data = request.form
#     result = DbResource().update_section_name(
#         data["call_no"], data["course_name"]
#     )
#
#     if result:
#         rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
#     else:
#         rsp = Response("FAIL", status=404, content_type="text/plain")
#
#     return rsp

@app.route("/sections", methods=["PUT"])
def update_section_enrollment():  # update a section's enrollment_number
    data = request.get_json()
    result = DbResource().update_section(
        data["call_no"], data["course_name"], data["enrollment_number"]
    )
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp


@app.route("/sections/<no>", methods=["DELETE"])
def delete_section(no): # delete a section

    result = DbResource().delete_section(no)

    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")

    return rsp


@app.route("/classes", methods=["POST"])
def add_class():  # a section adds a new class
    data = request.get_json()              #form
    result = DbResource().add_class(data['call_no'], data['date'], data['attendance_num'])
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp

@app.route("/classes", methods=["GET"])
def get_classes():  # get all classes or by query strings (pagination supported)
    result = DbResource().get_classes(request.args.to_dict())
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/classes/<call_no>", methods=["GET"])
def get_class_by_key(call_no):  # Class Read by section
    result = DbResource().get_class_by_key(call_no)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/classes/<call_no>/date/<date>", methods=["GET"])
def get_class_attendance(call_no, date):  # get section's attendance on <date>
    result = DbResource().get_one_class(call_no, date)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/classes", methods=["PUT"])
def update_class_attendance():  # update a class's attendance
    data = request.form
    result = DbResource().update_class_num(data['call_no'], data['date'], data['attendance'])
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp

@app.route("/classes", methods=["DELETE"])
def delete_class():  # delete a class
    data = request.form
    result = DbResource().delete_class(data['call_no'], data['date'])
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp

@app.route("/enrollments", methods=["POST"])
def add_enrollment():

    data = request.form
    result = DbResource().add_enrollment(data["call_no"], data["uni"])

    # number of affected rows
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")

    return rsp


@app.route("/enrollments/<no>", methods=["GET"])
def get_enrollments_by_no(no):

    result = DbResource().get_enrollments_by_no(no)

    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/enrollments/uni/<uni>", methods=["GET"])
def get_enrollments_by_uni(uni):

    result = DbResource().get_enrollments_by_uni(uni)

    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp



@app.route("/enrollments", methods=["DELETE"])
def delete_enrollment():

    data = request.form
    result = DbResource().delete_enrollment(data["call_no"], data["uni"])

    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")

    return rsp


@app.route("/attendances", methods=["POST"])
def add_attendance():  # a student attend a class, the class's attendance number increase 1
    data = request.form
    result = DbResource().add_attendance(data['uni'], data['call_no'], data['date'], increase_attendance=True)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp


@app.route("/attendances", methods=["GET"])
def get_attendances():  # get all attendances or by query strings (pagination supported)
    result = DbResource().get_attendances(request.args.to_dict())
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/attendances/<call_no>/date/<date>", methods=["GET"])
def get_attendances_by_class(call_no, date):  # get all students' attendance records on <call_no><date>
    result = DbResource().get_attendances_by_class(call_no, date)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/attendances/<call_no>/date/<date>/uni/<uni>", methods=["GET"])
def get_one_attendance(call_no, date, uni):  # get <uni>'s attendance record on <call_no><date>
    result = DbResource().get_one_attendance(call_no, date, uni)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/attendances/<call_no>/", methods=["GET"])
def get_attendance_by_section(call_no):  # get all students attendance records of <call_no>
    result = DbResource().get_attendance_by_section(call_no)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/attendances/<call_no>/uni/<uni>", methods=["GET"])
def get_attendances_section_student(call_no, uni):  # get <uni> attendance records of <call_no>
    result = DbResource().get_attendances_section_student(call_no, uni)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/attendances", methods=["DELETE"])
def delete_attendance():  # delete a student, the class's attendance decrease 1
    data = request.form
    result = DbResource().delete_attendance(data['uni'], data['call_no'], data['date'], decrease_attendance=True)
    if result:
        rsp = Response(json.dumps(result, cls=DateEncoder), status=200, content_type="application.json")
    else:
        rsp = Response("FAIL", status=404, content_type="text/plain")
    return rsp





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)