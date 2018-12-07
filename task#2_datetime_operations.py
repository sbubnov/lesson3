from datetime import datetime,timedelta

dt_now = datetime.now()
dt2 = datetime(2015,5,16,8,3,4)
yesterday = dt_now - timedelta(days=1)
month_ago = dt_now - timedelta (days=30)

date_string = "01/01/17 12:10:03.234567"

print('Вчера было ' + str(yesterday) + '\n' + 'Сегодня ' + 
    str(dt_now) + '\n' + 'Месяца назад было ' + str(month_ago) + '\n')


date_from_str = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_from_str)