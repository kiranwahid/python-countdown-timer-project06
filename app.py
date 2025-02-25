import time

countdown_time = int(input("Enter the countdown time in seconds: "))

while countdown_time > 0:
    print(countdown_time)
    countdown_time -= 1
    time.sleep(1)
    
    # minutes, seconds = divmod(countdown_time, 60)
    # time_format = '{:02d}:{:02d}'.format(minutes, seconds)
    # print(time_format, end='\r')
    # time.sleep(1)
    # countdown_time -= 1
    
print('Time is over!')
    
    

