# -*- coding: utf-8 -*-
import asyncio
import traceback


class Functions():
    '''
    as a container of functions
    '''
    @staticmethod
    async def add(param1, param2):
        try:
            return float(param1) + float(param2)
        except:
            return traceback.format_exc(limit=2)

    @staticmethod
    async def sub(param1, param2):
        try:
            return float(param1) - float(param2)
        except:
            return traceback.format_exc(limit=2)

    @staticmethod
    async def mul(param1, param2):
        try:
            await asyncio.sleep(10)
            return float(param1) * float(param2)
        except:
            return traceback.format_exc(limit=2)


    @staticmethod
    async def div(param1, param2):
        try:
            return float(param1) / float(param2)
        except:
            return traceback.format_exc(limit=2)
