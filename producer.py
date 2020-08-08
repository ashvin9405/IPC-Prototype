from multiprocessing.connection import Client
import random as r
import string, time
import socket

print("sending data...")

address = (socket.gethostname(), 6000)
conn = Client(address, authkey=None)

while True:
    class RandomProducer:

        time.sleep(2)

        def __init__(self):
            random_choice = r.randint(1, 4)
            if random_choice == 1:
                self.random_string()
            elif random_choice == 2:
                self.random_integer()
            else:
                self.random_float()

        def random_string(self):
            letters = string.ascii_letters
            r_string = ''
            for i in range(5):
                k = r.choice(letters)
                r_string += k
            conn.send(r_string)

        def random_integer(self):
            r_int = r.randint(1, 100)
            conn.send(r_int)

        def random_float(self):
            r_float = r.uniform(1, 50)
            conn.send(r_float)

    RP_1 = RandomProducer()