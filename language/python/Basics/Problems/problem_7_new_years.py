"""
Start at 10 seconds and count down until 1 and then print "Happy New Year! 🎉"
"""

import time

second_left = 10

while second_left > 0:
    print(second_left)
    second_left -= 1
    time.sleep(1)

print("Happy New Year! 🎉")