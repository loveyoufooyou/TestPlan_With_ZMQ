# -*- coding: utf-8 -*-
from threading import Thread
import zmq
import csv



def load_test_plan():
    '''
    load test_plan.csv
    :return: test_list list
    '''
    test_list = []
    with open('test_plan.csv', 'r') as csvfile:
        test_plan = csv.reader(csvfile)
        next(test_plan)
        for item in test_plan:
            test_list.append((item[5], tuple(item[6:])))
    return test_list

context = zmq.Context()

class ZMQSub():
    '''
    Forwarding msg from the web pub to sequencer.
    '''
    web_addr = 'tcp://127.0.0.1:8888'

    def __init__(self, addr):
        self.status = False
        self.socket = context.socket(zmq.SUB)
        self.socket.setsockopt(zmq.SUBSCRIBE, b'')
        self.socket.connect(addr)

    def run(self, pair_server):
        '''
        :param pair_server: ZMQPair instance
        '''
        while True:
            msg = self.socket.recv_string()

            # you cant twice run it, without running out.
            if msg == 'start' and self.status == False:
                self.set_status()
                t = Thread(target=pair_server.run, args=(load_test_plan(),))
                t.start()
            elif msg == 'stop':
                self.set_status(0)


    def set_status(self, num=None):
        if num == 0:
            self.status = False
        else:
            self.status = True



class ZMQPairServer():
    '''
    connect the pair of TestEngine.
    '''
    addr = 'tcp://127.0.0.1:8800'

    def __init__(self, addr):
        self.socket = context.socket(zmq.PAIR)
        self.socket.bind(addr)

    def run(self, test_plan):
        self.socket.send_pyobj(test_plan)
        print('task:', test_plan)
        result = self.socket.recv_pyobj()
        if isinstance(result, list):
            print('result ', result)
        # you can write log.



    def close(self):
        self.socket.close()
