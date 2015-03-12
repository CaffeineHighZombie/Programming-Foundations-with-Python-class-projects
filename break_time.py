import time
import webbrowser

total_count = 0
break_count = 3

print("This program started on: " + time.ctime())
while(total_count < break_count):
    time.sleep(2*60*60)
    webbrowser.open("https://youtu.be/KQ6zr6kCPj8?t=1m55s")
    total_count += 1
