import time
from time import sleep, strftime
from twilio.jwt import client
from twilio.rest import Client
from multiprocessing import Process

#get time
local_time = time.localtime()
time_string = time.strftime("%H", local_time)

second_on_hour = 3600
second_on_four_hour = 14400

#twilio
account_sid = 'xxxx'
auth_token = 'xxxx'
twilio_client = Client(account_sid, auth_token)

breakfast = int(raw_input('When would you like to have your breakfast?'))
lunch = int(raw_input('What time do you prefer to eat your lunch?'))
dinner = int(raw_input('what time do you usually eat your dinner?'))
walk = int(raw_input('When would like to take a short walk ?'))


def food_walk():
    while (True):
        if int(strftime('%H')) == breakfast :
            message = twilio_client.messages.create(
                body = 'Good Morning :) \n '
                       'Don\'t forget your breakfast! \n'
                       'Have a nice day!',
                from_='+xxxx',
                to = '+xxxx'
            )
        if int(strftime('%H')) == lunch :
            message = twilio_client.messages.create(
                body='Don\'t forget to eat your lunch!',
                from_='xxxx',
                to='xxxx'
            )
        if int(strftime('%H')) == dinner:
            message = twilio_client.messages.create(
                body='It\'s time for dinner!',
                from_='xxxx',
                to='xxxx'
            )
        if int(strftime('%H')) == walk:
            message = twilio_client.messages.create(
                body='It\'s time to move your body!',
                from_='xxxx',
                to='xxxx'
            )
        sleep(second_on_hour)#to start loop again and update time after one hour
        strftime('%H')


def water1():
    total_water = 9
    water_count = 0
    while True:
        if int(strftime('%H')) >= 8: #When time is above 8am strat to remind for water
            while water_count < total_water:
                time.sleep(5400) #delays for 1.5 hour
                message = twilio_client.messages.create(
                    body = 'Don\'t forget to hydrate!',
                    from_ = 'xxxx',
                    to = 'xxxx'
                )
                if int(strftime('%H')) >= 21: #when time is 9pm it will stop
                    break
                water_count += 1
        sleep(second_on_four_hour)
        strftime('%H')

#run to function at same time
if __name__ == '__main__':
    p1 = Process(target=food_walk)
    p1.start()
    p2 = Process(target=water1)
    p2.start()



