# unit test for request w payload
# (get request can be done in browser)
import requests
import json


def test_section_add():
    info = dict(call_no='COMS4111', course_name='Intro to Database', enrollment_number=160)
    resp = requests.post("http://127.0.0.1:5011/sections", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)

# def test_section_delete1():
#     info = {'call_no': 'COMS4111'}
#     resp = requests.delete("http://127.0.0.1:5011/sections", data=info)
#     if resp.status_code == 200:  # verify valid response code
#         print("OK")
#     else:
#         print("Fail")
#     print(resp)


def test_section_delete():
    resp = requests.delete("http://127.0.0.1:5011/api/sections/CSEE4119")
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_section_update():
    info = dict(call_no='COMS6156', course_name='CloudComputing')
    resp = requests.post("http://127.0.0.1:5011/sections/edit_course_name", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)

def test_section_update1():
    info = dict(call_no='COMS6156', course_name='CloudComputing')
    resp = requests.post("http://127.0.0.1:5011/sections/edit_name", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_section_update2():
    info = dict(call_no='COMS6156', enrollment_number=200)
    resp = requests.post("http://127.0.0.1:5011/sections/edit_num", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)



def test_class_add():
    info = dict(call_no='CSEE4119', date='2022-12-16', attendance=10)
    resp = requests.post("http://127.0.0.1:5011/class", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_class_delete():
    info = {'call_no': 'CSEE4119', 'date': '2022-12-16'}
    resp = requests.delete("http://127.0.0.1:5011/class", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_class_update():
    info = dict(call_no='COMS6156', date='2022-02-13', attendance=80)
    resp = requests.post("http://127.0.0.1:5011/class/edit_attendance", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)

def test_student_add():
    info = dict(uni='zl1133', call_no='CSEE4119', date='2022-12-16')
    resp = requests.post("http://127.0.0.1:5011/students", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_student_delete():
    info = {'call_no': 'CSEE4119', 'date':'2022-12-16', 'uni': 'zc1133'}
    resp = requests.delete("http://127.0.0.1:5011/students", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_enrollment_add():
    info = dict(call_no='CSEE4119', uni='hr2543')
    resp = requests.post("http://127.0.0.1:5011/enrollments", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_enrollment_delete():
    info = {'call_no': 'COMS6156', 'uni': 'aws1234'}
    resp = requests.delete("http://127.0.0.1:5011/enrollments/no&uni", data=info)
    if resp.status_code == 200:
        print("OK")
    else:
        print("Fail")

if __name__ == "__main__":
    test_enrollment_add()
    test_student_delete()
