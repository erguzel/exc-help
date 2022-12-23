import os
import sys
sys.path.insert(1,os.getcwd())

from src.exchelp.exception_helper import CoreException,ReportObject


def sum_divide_function(a,b,d):
    try:
        sum = a+b
        divide = sum/d
        return divide
    except Exception as e:
        CoreException('sum_divide_function failure',e,logIt=True,dontThrow=True,shouldExit=True).\
            adddata('report',ReportObject(f'sum var would be {sum}').\
                    addData('who',{'name':'human','locals':locals()})).\
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



print(sum_divide_function(3,4,0))



