import time

def countdown_timer(seconds):
    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(minutes, sec)
        print("Time Left:", timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("\nTime's up!")

if __name__ == "__main__":
    seconds = int(input("Enter the number of seconds to countdown: "))
    countdown_timer(seconds)
