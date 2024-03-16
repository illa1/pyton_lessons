# import
import time

# define the counddown function
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1

    print('time over')

# input time
t = int(input('Enter the time in secunds: '))

# function
countdown(t)