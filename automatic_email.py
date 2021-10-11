import os
import random
import smtplib

def automatic_email():
    user = input("Enter your Name : ")
    email = input("Enter your Email : ")
    message = (f"Dear {user}, Welcome to our Seller Community")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("iamaladdin02@gmail.com", "Masawwar@9692")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent")


automatic_email()