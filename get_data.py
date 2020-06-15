# get_data.py & print name

import json
import requests

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
#print(response.status_code)
#print(response.text)
my_dict = json.loads(response.text)
print(my_dict["name"])

#loop of name and id

request_url_2 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response_2 = requests.get(request_url_2)
#print(response_2.status_code)
#print(response_2.text)
my_dict_2 = json.loads(response_2.text)
for x in my_dict_2:
    print(x["id"], x["name"])

#find the max grade
request_url_3 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response_3 = requests.get(request_url_3)
my_dict_3 = json.loads(response_3.text)

grades = []
students = my_dict_3["students"]
for y in students:
    grades.append(y["finalGrade"])

print(max(grades))