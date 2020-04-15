from rpc.client import RPCClient
import sys

if __name__ == '__main__':
    try:
        client = RPCClient((sys.argv[1], int(sys.argv[2])))
        for i in range(5):
            print(client.call(i))
    except:
        print("Error:", sys.exc_info()[1])
