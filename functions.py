# -*- coding: utf-8 -*-
import traceback


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
