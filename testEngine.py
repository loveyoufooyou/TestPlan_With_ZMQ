# -*- coding: utf-8 -*-
from threading import Thread
import zmq
from functions import Functions
import asyncio


context = zmq.Context()

class ZMQSub_Function():
    '''
    recv 'stop' from the web pub to stop running funcs.
    '''
    web_addr = 'tcp://127.0.0.1:8888'

    def __init__(self, addr):
        self.socket = context.socket(zmq.SUB)
        self.socket.setsockopt(zmq.SUBSCRIBE, b'')
        self.socket.connect(addr)

    def run(self):
        while True:
            msg = self.socket.recv_string()
            if msg == 'stop':
                Functions.status = False



class ZMQPairClient():
    addr = 'tcp://127.0.0.1:8800'

    def __init__(self, addr):
        self.socket = context.socket(zmq.PAIR)
        self.socket.connect(addr)

    async def test_plan_main(self, test_plan, sub):
        '''run all test_plan as running async tasks'''
        task_tuple = ()
        for func_str, params in test_plan:
            try:
                # to get funcs from test_plan.csv
                func = getattr(Functions, func_str)
                # to create tasks of these funcs.
                task_tuple += (asyncio.create_task(func(*params)),)

            except Exception as e:
                print(e)
                continue
        # run async
        result = await asyncio.gather(*task_tuple)
        # send the result to sequencer
        self.socket.send_pyobj(result)
        sub.set_status(0)


    def run(self, loop, sub):
        '''contact with sequencer'''
        while True:
            msg = self.socket.recv_pyobj()
            if isinstance(msg, list):
                test_plan = msg
                # print('TE', test_plan)
                asyncio.run_coroutine_threadsafe(self.test_plan_main(test_plan, sub), loop)


    def close(self):
        self.socket.close()

    def start_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    def daemon_thread_async(self, loop):
        thread_async_daemon = Thread(target=self.start_loop, args=(loop,))
        thread_async_daemon.daemon = True
        thread_async_daemon.start()

def testEngine_main(pair_client, sub):
    sub_func = ZMQSub_Function(ZMQSub_Function.web_addr)
    t = Thread(target=sub_func.run)
    t.start()

    # main thread get event loop
    loop = asyncio.get_event_loop()
    # create a child thread to run the loop forever.
    pair_client.daemon_thread_async(loop)

    # create a child thread to run a WhileTrue, and captured async tasks will
    # run in the loop in previous child thread.
    t_async = Thread(target=pair_client.run, args=(loop, sub))
    t_async.start()