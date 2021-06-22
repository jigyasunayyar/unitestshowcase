'''
method to test the unit test cases
'''
import functools


def add(*args):
    '''
    addition method
    '''
    return sum(args)
def subtract(*args):
    '''
    subtract method
    '''
    return functools.reduce(lambda x, y: x-y, args)
def multiply(*args):
    '''
    multiplication method
    '''
    return functools.reduce(lambda x, y: x*y, args)

    
