import os
import time
interval = 3600
while True:
    command = "osascript -e \'say \"Hey Shashanka Drink Water\"\';osascript -e \'display alert \"Hey Shashanka, Drink Water\"\'"
    os.system(command)
    time.sleep(interval)