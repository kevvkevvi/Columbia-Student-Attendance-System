# unit test for request w payload
# (get request can be done in browser)
import requests
import json


def test_section_add():
    info = dict(call_no='CSEE4119', course_name='Computer Networks', enrollment_number=120)
    resp = requests.post("http://127.0.0.1:5011/api/sections", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_section_delete():
    resp = requests.delete("http://127.0.0.1:5011/api/sections/no/CSEE4119")
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_section_update():
    info = dict(call_no='COMS6156', course_name='CloudComputing')
    resp = requests.post("http://127.0.0.1:5011/api/sections/edit", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_enrollment_add():
    info = dict(call_no='CSEE4119', uni='hr2543')
    resp = requests.post("http://127.0.0.1:5011/api/enrollments", data=info)
    if resp.status_code == 200:  # verify valid response code
        print("OK")
    else:
        print("Fail")
    print(resp)


def test_enrollment_delete():
    info = {'call_no': 'COMS6156', 'uni': 'aws1234'}
    resp = requests.delete("http://127.0.0.1:5011/api/enrollments/no&uni", data=info)
    if resp.status_code == 200:
        print("OK")
    else:
        print("Fail")


if __name__ == "__main__":
    test_enrollment_add()