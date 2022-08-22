# -*- coding: utf-8 -*-
from sequencer import sequencer_mian, ZMQSeq
from testEngine import testEngine_main, ZMQRep

# Maintains a seq and a rep.
seq = ZMQSeq(ZMQSeq.addr)
rep = ZMQRep(ZMQRep.addr)
# sub = ZMQSub(ZMQSub.web_addr)

# We start a Thread to run testEngine.
testEngine_main(rep)


# Simulating UI click, we run code of sequencer.
for i in range(10):
    sequencer_mian(seq)


# close socket of seq.
seq.close()
