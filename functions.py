# -*- coding: utf-8 -*-
import asyncio
import traceback


class Functions():
    status = False
    '''
    as a container of functions.
    
    note:
        Your test_plan.csv should be classified! 
        If test_func needs long time to run, they can be classified as stoppable and unstoppable.

        stoppable:
            You can stop and split, because we can recv the signal from web.
        unstoppable:
            It means you can't stop. it must run until accomplishment of all tasks.

        So, when you run stoppable and unstoppable func with long time, clicking the 'stop', the 
        code will stop stoppable funcs rather than unstoppable funcs. You must wait until accomplish 
        of unstoppable func.
    '''
    @classmethod
    async def stoppable(cls, param1, param2, *args, **kwargs):
        cls.status = True
        n = 0
        while cls.status:
            n += 10
            await asyncio.sleep(1)
            if n >= 100:  # accomplish signal
                return 'ACCOMPLISH', n
        return 'Fail', None



    # the following is unstoppable functions.

    @staticmethod
    async def add(param1, param2, *args, **kwargs):
        try:
            return float(param1) + float(param2)
        except:
            return traceback.format_exc(limit=2)

    @staticmethod
    async def sub(param1, param2, *args, **kwargs):
        try:
            return float(param1) - float(param2)
        except:
            return traceback.format_exc(limit=2)

    @staticmethod
    async def mul(param1, param2, *args, **kwargs):
        try:
            await asyncio.sleep(10)
            return float(param1) * float(param2)
        except:
            return traceback.format_exc(limit=2)


    @staticmethod
    async def div(param1, param2, *args, **kwargs):
        try:
            return float(param1) / float(param2)
        except:
            return traceback.format_exc(limit=2)
