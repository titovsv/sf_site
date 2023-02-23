from time import sleep
import config
 
print(config.URL)

i = 0
while i < 10:
    print('Still less ten')
    sleep(1)
    i += 1