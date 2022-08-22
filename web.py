# -*- coding: utf-8 -*-
import time

import zmq

context = zmq.Context()

class ZMQPub():
    '''
    send msg to sub of sequencer.
    '''
    web_addr = 'tcp://127.0.0.1:8888'

    def __init__(self, addr):
        self.socket = context.socket(zmq.PUB)
        self.socket.bind(addr)


    def start(self):
        '''UI action of 'start' clicking.'''
        self.socket.send_string('start')

    def stop(self):
        '''UI action of 'stop' clicking.'''
        self.socket.send_string('stop')

    def close(self):
        self.socket.close()

def web_main(pub):
    ##############################################################################
    ########## you can change codes for your test of behavior UI action. #########
    pub.start()
    pub.start()
    pub.start()
    time.sleep(0.1)
    pub.stop()
    ##############################################################################
    ##############################################################################

if __name__ == '__main__':
    time.sleep(5)
    pub = ZMQPub(ZMQPub.web_addr)
    time.sleep(0.5)
    web_main(pub)