import requests
import smtplib
import email
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
URL = "https://httpbin.org/image/svg"
print("Downloading image from" + " " + URL)
r = requests.get(URL)
print(r)
with open('image.svg', 'wb') as f:
    for chunk in r.iter_content():
        f.write(chunk)
