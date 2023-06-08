import os
import sys
sys.path.insert(1,os.getcwd())

from src.exchelp.exception_helper import CoverException,ReportObject,CoreException
import src.exchelp.exception_helper as eh

import pytest 


def sum_divide_function(a,b,d):
    try:
        sum = a+b
        try:
            return sum/d
        except Exception as k :
            CoreException('some core cause exception',k).adddata('sum',sum).act()
        
    except Exception as e:
        CoverException('sum_divide_function failure',cause=e,logIt=True,dontThrow=True,shouldExit=True).\
            adddata('report',ReportObject().\
                    adddata('who',{'name':'human','locals':locals()})).\
                    adddata('someList',[1,2,3,'4']).\
                    adddata('someSet',{1,2,'3'}).\
                    adddata('someTuple',(3,4,5,'3')).\
                    adddata('some single tuplike',(255)).\
                    adddata('someType',type(dict)).\
                    adddata('someByteStr',bytes('hello world','utf-8')).\
                    adddata('someBytes',bytes([7,8,9,255])).\
                    adddata('byteArr',bytearray([4,5,7])).\
                    adddata('byteArrStr',bytearray('hello world','utf-8')).\
                act()


#print(sum_divide_function(3,4,0))

def test_test_function():
    #case 1
    result = 'printing world'
    actual = eh.test_function('world')

    assert result == actual

