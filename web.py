# -*- coding: utf-8 -*-
import time
from flask import Flask, render_template
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

# def web_main(pub):
#     ##############################################################################
#     ########## you can change codes for your test of behavior UI action. #########
#     # pub.stop()
#     pub.start()
#     # pub.start()
#     # pub.start()
#
#     # must sleep. insure zmq can successfully send/recv msg.
#     time.sleep(0.1)
#
#     pub.stop()
#     ##############################################################################
#     ##############################################################################


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/start/')
def start():
    pub.start()
    return 'hello start'


@app.route('/test/stop/')
def stop():
    pub.stop()
    return 'hello stop'



if __name__ == '__main__':

    pub = ZMQPub(ZMQPub.web_addr)
    time.sleep(0.5)
    app.run()

    # web_main(pub)

