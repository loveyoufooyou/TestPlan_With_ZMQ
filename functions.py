# -*- coding: utf-8 -*-
'''
项目中的测试用例，这里写文件到 log 中，可以手动 stop。
'''
import asyncio
import time
import random
import traceback

RUNNING = False

class Functions():
    '''
    as a container of functions
    '''
    @staticmethod
    def add(param1, param2):
        try:
            return float(param1) + float(param2)
        except Exception as e:
            return traceback.format_exc(limit=2)

    @staticmethod
    def sub(param1, param2):
        try:
            return float(param1) - float(param2)
        except Exception as e:
            return traceback.format_exc(limit=2)

    @staticmethod
    def mul(param1, param2):
        try:
            return float(param1) * float(param2)
        except Exception as e:
            return traceback.format_exc(limit=2)


    @staticmethod
    def div(param1, param2):
        try:
            return float(param1) / float(param2)
        except Exception as e:
            return traceback.format_exc(limit=2)
