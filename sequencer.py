# -*- coding: utf-8 -*-
import threading
import zmq
import csv

def load_test_plan():
    '''
    load test_plan.csv
    :return: test_plan list
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
    Forwarding msg from the web pub to seq.
    '''
    web_addr = 'tcp://127.0.0.1:8888'

    def __init__(self, addr):
        self.status = False
        self.test_plan = load_test_plan()
        self.socket = context.socket(zmq.SUB)
        self.socket.setsockopt(zmq.SUBSCRIBE, b'')
        self.socket.connect(addr)

    def run(self, seq):
        '''
        :param zmqSeq: ZMQSeq instance
        '''
        while True:
            msg = self.socket.recv_string()
            print(msg)
            if msg == 'start' and self.status == False: # you cant twice run it, without running out.
                self.status = True
                t = threading.Thread(target=seq.run, args=(self.test_plan,))
                t.start()
                # cant join, we need to recv stop
            elif msg == 'stop':
                self.status = False
                seq.stop()




class ZMQSeq():
    '''
    connect the sep of TE.
    '''
    addr = 'tcp://127.0.0.1:8800'

    def __init__(self, addr):
        self.status = False
        self.socket = context.socket(zmq.REQ)
        self.socket.connect(addr)

    def run(self, test_plan):
        self.status = True
        for item in test_plan:
            print(self.status)
            if self.status:
                self.socket.send_pyobj(item)
                result = self.socket.recv_pyobj()
                # you can write log.
                print(result)
            else:
                break

    def stop(self):
        self.status = False

    def close(self):
        self.socket.close()
