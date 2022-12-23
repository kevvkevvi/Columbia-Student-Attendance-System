# unit test for request w payload
# (get request can be done in browser)
import requests
import json


def test_section_add():
    info = dict(call_no='COMS4111', course_name='Intro to Database', enrollment_number=160)
    resp = requests.post("http://127.0.0.1:5011/api/sections", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_section_delete():
    info = {'call_no': 'COMS4111'}
    resp = requests.delete("http://127.0.0.1:5011/api/sections", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_section_update():
    info = dict(call_no='COMS6156', course_name='CloudComputing')
    resp = requests.post("http://127.0.0.1:5011/api/sections/edit_course_name", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)

def test_section_update2():
    info = dict(call_no='COMS6156', enrollment_number=200)
    resp = requests.post("http://127.0.0.1:5011/api/sections/edit_enrollment_number", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)



def test_class_add():
    info = dict(call_no='CSEE4119', date='2022-12-16', attendance=10)
    resp = requests.post("http://127.0.0.1:5011/api/class", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_class_delete():
    info = {'call_no': 'CSEE4119', 'date': '2022-12-16'}
    resp = requests.delete("http://127.0.0.1:5011/api/class", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_class_update():
    info = dict(call_no='COMS6156', date='2022-02-13', attendance=80)
    resp = requests.post("http://127.0.0.1:5011/api/class/edit_attendance", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)

def test_student_add():
    info = dict(uni='dt2599', call_no='COMS6156', date='2022-02-13')
    resp = requests.post("http://ec2-44-204-239-194.compute-1.amazonaws.com:5011/api/students", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_student_delete():
    info = {'call_no': 'CSEE4119', 'date':'2022-12-16', 'uni': 'zc1133'}
    resp = requests.delete("http://127.0.0.1:5011/api/students", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


if __name__ == "__main__":
    test_student_add()