from websocket import create_connection
import json
import requests

ws = create_connection("wss://dropmail.me/websocket")
test3 = ws.recv()
email_hashes = []
email_hash = ws.recv()[1:]
email_hashes.append(email_hash)
print(test3)
# Add a previous email

tf = ws.send("R{}".format('laste.ml:0c5af5b30a3d37791d053f947f3557d72'))
#t22 = ws.send("Hello")
test2 = ws.recv()[1:]

print(test2)

