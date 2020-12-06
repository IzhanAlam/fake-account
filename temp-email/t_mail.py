import json
from websocket import create_connection

class t_mail_inbox:
    def __init__(self):
        self.ws = create_connection("wss://dropmail.me/websocket")
        self.close = self.ws.close
        self.email_ = []
        email = self.ws.recv()[1:]
        self.email_.append(email)
        self.ws.recv()

    def get_next_email(self):
        mail_c = self.ws.recv()[1:]
        return json.loads(mail_c)
        


