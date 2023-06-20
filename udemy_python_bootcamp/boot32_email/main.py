##################### Starting Project ######################

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
from random import randint
import smtplib
import datetime as dt
import pandas as pd

email = 'ingrid@gmail.test'
now = dt.datetime.now()
today_month = int(now.month)
today_day = int(now.day)
today_year = int(now.year)

bdays = pd.read_csv('C:\\Users\\G020772\\repos\\workspace\\python_bootcamp\\boot32_email\\birthdays.csv')
todays_bdays = bdays[(bdays['month']==today_month) & (bdays['day']==today_day)]

recipients = todays_bdays.to_dict(orient='records')

for person in recipients:
    print(person)
    name = person['name']
    recipient = person['email']
    letter = f"letter_{randint(1, 3)}"
    with open(f'C:\\Users\\G020772\\repos\\workspace\\python_bootcamp\\boot32_email\\letter_templates\\{letter}.txt') as f:
        letter_content = f.read()
        letter_content = letter_content.replace("[NAME]", name)
    letter_finished = f"Subject: Happy birthday!\n\n{letter_content}" 
    print(letter_finished)
    # with smtplib.SMTP('smtp.gmail.com') as connection:
    #     connection.starttls() #TLS mode - encrypts the content of the email
    #     connection.login(user=email, password=pw)
    #     connection.sendmail(from_addr=email, to_addrs=recipient, msg=content)