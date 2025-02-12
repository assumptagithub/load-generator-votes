import random
import time

choices = ["A", "B"]

while True:
    vote = random.choice(choices)
    print(f"Generated vote: {vote}")
    time.sleep(1)  
