'''
Name: Max Ehrlich, William Carr, Muhammad Fazlani
email: ehrlicmh@mail.uc.edu, carrwa@mail.uc.edu, fazlanmn@mail.uc.edu
Assignment: Assignment 10
Created: April 5, 2023
Course: IS 4010
Semester/Year: Spring 23
Brief Description: This project demonstrates our ability to access an API, request information, and finally present the info.
'''


import json5
import requests


response = requests.get('https://api.nal.usda.gov/fdc/v1/food/534258?api_key=0kGH6V8UHGMqlnQiuMxFN1XNLPyrwfvu5gieRSYZ')#this sends a request to the api endpoint by using our own api code
json_string = response.content
parsed_json = json5.loads(json_string) # This creates our python dictionary

print(parsed_json) # prints the full dictionary

print('type of food: ',parsed_json['description'])# prints value in dictionary based off of key provided
print('publication date:', parsed_json['publicationDate'])
print('health facts:', parsed_json['foodNutrients'])

