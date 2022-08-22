# -*- coding: utf-8 -*-

from sequencer import ZMQSub, ZMQPairServer
from testEngine import testEngine_main, ZMQPairClient


# Maintains a server of sequencer and a client of testEngine and a sub.
pair_server = ZMQPairServer(ZMQPairServer.addr)
pair_client = ZMQPairClient(ZMQPairClient.addr)
sub = ZMQSub(ZMQSub.web_addr)


# We start a Thread to run testEngine.
testEngine_main(pair_client, sub)



# Simulating UI click, we run code of sequencer.
sub.run(pair_server)  # cant go out the loop


# close socket of seq.
pair_server.close()