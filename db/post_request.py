import requests

url = "http://ec2-34-224-37-72.compute-1.amazonaws.com:5011/api/enrollments"

data = {"call_no": "COMS6156", "uni": "kjl2185"}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("Data inserted successfully")
else:
    print("An error occurred:", response.status_code)
