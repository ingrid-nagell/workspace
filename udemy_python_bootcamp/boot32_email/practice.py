#SMTP: Simple mail transfer protocol
import smtplib
import datetime as dt

# In order to be able to send email from gmail,
# go to account settings 
# -> Turn on two-step verification
# -> Add app-password

now = dt.datetime.now()
year = now.year
today = now.date()
print(today)

sender = 'ingrid@gmail.com'
recipient = 'ingrid@gmail.com'
pw = 'add_app_pw_from_google_here'

content = '''Subject:Testing email\n\nHello,
This is a new message.'''

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls() #TLS mode - encrypts the content of the email
    connection.login(user=sender, password=pw)
    connection.sendmail(from_addr=sender, to_addrs=recipient, msg=content)
