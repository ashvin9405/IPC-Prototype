from multiprocessing.connection import Listener
import socket
print ("waiting for connection....")
address = (socket.gethostname(), 6000)
listener = Listener(address, authkey=None)
conn = listener.accept()



print('connection accepted from: ', listener.last_accepted)

while True:
    received_data = conn.recv()
    print(f"Received data : {received_data}. Data is instance of {type(received_data)}")
    print("\n")

listener.close()