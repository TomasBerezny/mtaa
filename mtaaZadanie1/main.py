# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sipfullproxy as p

host = "172.20.10.6"
port = 5060

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p.HOST = host
    p.PORT = port
    p.registrar = {}
    p.running = True
    p.recordroute = "Record-Route: <sip:%s:%d;lr>" % (host, port)
    p.topvia = "Via: SIP/2.0/UDP %s:%d" % (host, port)
    p.run_lib()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
