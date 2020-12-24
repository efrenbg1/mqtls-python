from mqtls import mqtls
import time

broker = mqtls(host="rmote.app", port=2443,
               user="efren@boyarizo.es", pw="1Q2w3e4r")

print(broker.publish("topic", 3, "6"))
