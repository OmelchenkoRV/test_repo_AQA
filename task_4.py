import smtplib
from email.message import EmailMessage
Sender_email = "omelchenkorv@gmail.com"
Reciever_email = "el.piankova@gmail.com"
Password = input('Enter your email account password: ')
newMessage = EmailMessage()
newMessage['Subject'] = "Homework6"
newMessage['From'] = Sender_email
newMessage['To'] = Reciever_email
newMessage.set_content("I did it!")


server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()


server.login(Sender_email, Password)


server.sendmail(Sender_email, Reciever_email, newMessage.as_string())

server.quit()
print(f"Successfully sent email to {Reciever_email}")