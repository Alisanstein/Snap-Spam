import requests
import time

phonenum = input('Please enter a phone number: ')
urlsend = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
mydata1 = {"cellphone":"+98"+phonenum , "text" : "Salam."}


r = requests.post(urlsend , data=mydata1)


print(r.status_code)