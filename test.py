from datetime import datetime, timedelta

departure_time = datetime.strftime(datetime.now() + timedelta(days=7), '%d/%m/%Y')
return_time = datetime.strftime(datetime.now() + timedelta(days=37), '%d/%m/%Y')

print(departure_time, return_time)

#"01/07/2023"