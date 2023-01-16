##################### Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt

from pandas import read_csv

now = dt.datetime.now()
today_month = int(now.month)
today_day = int(now.day)

bdays = read_csv('python_bootcamp\\boot32_email\\birthdays.csv')

todays_bdays = bdays[(bdays['month']==today_month) & (bdays['day']==today_day)]

recipients = todays_bdays.to_dict(orient='records')

