import socket
import signal
import json
from threading import Thread

class ClientHandler(Thread):
    def __init__(self, socket, routine):
        Thread.__init__(self)
        self.socket = socket
        self.routine = routine

    def run(self):
        try:
            data = json.loads(self.__read_all().decode())
            result = self.routine(*data['args'])
            self.socket.send(json.dumps({'result': result}).encode())
        except:
            self.socket.send(json.dumps({'result': None}).encode())
    
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

class RPCServer:
    def __init__(self, address, routine):
        self.routine = routine
        self.socket = socket.socket()
        self.socket.bind(address)
        self.socket.listen(5)
        signal.signal(signal.SIGINT, self.__signal_handler)
        signal.signal(signal.SIGTERM, self.__signal_handler)

    def run(self):
        while True:
            (client_socket, (ip, port)) = self.socket.accept()
            handler = ClientHandler(client_socket, self.routine)
            handler.start()

    def __signal_handler(self, *args):
        raise OSError("Interrupted")

    def __del__(self):
        self.socket.close()
