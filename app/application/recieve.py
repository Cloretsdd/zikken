import sys

def recieve():

    recieve = sys.stdin.readline()
    recieve = recieve + "OK!"

    print('Content-type: text/html\n')
    print(recieve)

    return recieve

if __name__ == "__main__":
    recieve()