import socket
import json

class RPCClient:
    def __init__(self, address):
        self.socket = socket.socket()
        self.socket.connect(address)

    def call(self, *args):
        data = json.dumps({'args': args}).encode()
        self.socket.send(data)
        data = json.loads(self.__read_all().decode())
        return data['result']

    def __read_all(self, buffer_size=1024):
        result = b''
        while True:
            data = self.socket.recv(buffer_size)
            result += data
            if len(data) < buffer_size:
                break
        return result

    def __del__(self):
        self.socket.close()
