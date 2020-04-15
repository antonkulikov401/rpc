from rpc.server import RPCServer
import sys

def square(n: int):
    return n ** 2

if __name__ == '__main__':
    try:
        server = RPCServer((sys.argv[1], int(sys.argv[2])), square)
        server.run()
    except:
        print("Error:", sys.exc_info()[1])
