from mqtls import mqtls
import time

broker = mqtls(host="rmote.app", port=2443,
               user="efren@boyarizo.es", pw="1Q2w3e4r")

while True:
    print(broker.publish("A4:CF:12:F4:DE:E0", 1, "0"))
    time.sleep(10)
