# -*- coding: utf-8 -*-
from sequencer import ZMQSeq, ZMQSub
from testEngine import testEngine_main, ZMQRep

# Maintains a seq and a rep.
seq = ZMQSeq(ZMQSeq.addr)
rep = ZMQRep(ZMQRep.addr)
sub = ZMQSub(ZMQSub.web_addr)

# We start a Thread to run testEngine.
testEngine_main(rep)


# Simulating UI click, we run code of sequencer.
sub.run(seq)  # cant go out the loop


# close socket of seq.
seq.close()
