import requests
import smtplib
import ssl
import os

url = (
    "https://newsapi.org/v2/everything?q=tesla&from=2024-03-09&sortBy=publishedAt&" 
    "apiKey=da82b67ed137451ab20fe574f738a71e"
)

# make request
request = requests.get(url)
# get json from response data
content = request.json()
article = content["articles"][0]

#email data
host = "smtp.gmail.com"
port = 465
username = "resminiloris@gmail.com"
receiver = username
password = os.getenv("EMAIL_SENDER_PASSWORD")
context = ssl.create_default_context()

message = f"""
Hi! how are you?
here's some news:

{article["title"]}
{article["description"]}

source: {article["source"]["name"]}
author: {article["author"]}
"""

#send email
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message.encode('utf-8'), mail_options=())


