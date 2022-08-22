# -*- coding: utf-8 -*-
import time
from threading import Thread
import zmq
from functions import Functions

context = zmq.Context()
funcs = Functions()

class ZMQRep():
    addr = 'tcp://127.0.0.1:8800'

    def __init__(self, addr):
        self.socket = context.socket(zmq.REP)
        self.socket.bind(addr)

    def run(self):
        while True:
            fun, params = self.socket.recv_pyobj()
            print('FUNCTION:%s%s'%(fun, params))
            result = funcs.__getattribute__(fun)(*params)
            time.sleep(5)
            self.socket.send_pyobj(result)

    def close(self):
        self.socket.close()


def testEngine_main(rep):
    t = Thread(target=rep.run)
    # We can set daemon, if running on dev.
    t.daemon = True
    t.start()