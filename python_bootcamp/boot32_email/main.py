##################### Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

from random import randint
import smtplib
import datetime as dt

import pandas as pd

email = 'ingrid@gjensidige.no'
now = dt.datetime.now()
today_month = int(now.month)
today_day = int(now.day)
today_year = int(now.year)

bdays = pd.read_csv('C:\\Users\\G020772\\repos\\workspace\\python_bootcamp\\boot32_email\\birthdays.csv')
todays_bdays = bdays[(bdays['month']==today_month) & (bdays['day']==today_day)]
recipients = todays_bdays.to_dict(orient='records')

for person in recipients:
    letter = f"letter_{randint(1, 3)}"
    #letter_content = with open('C:\\Users\\G020772\\repos\\workspace\\python_bootcamp\\boot32_email\\letter_templates\\letter_1.txt')
    content = f"Subject: Happy birthday!\n\n{letter}" 

    print(content)
    # with smtplib.SMTP('smtp.gmail.com') as connection:
    #     connection.starttls() #TLS mode - encrypts the content of the email
    #     connection.login(user=email, password=pw)
    #     connection.sendmail(from_addr=email, to_addrs=person['email'], msg=content)