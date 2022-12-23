# exc-help

exc-help exception helper package

## Description

exc-help is a core python project which is used to manage exceptions. It is designed in a pattern that one dedicated exception type is used to store and log the exception information in desired application state in json format. It also has a type checking method to identify the variable types, and to take action accordingly in the runtime.

## Getting Started

### Dependencies

* No dependency

### Installing

* Not available in pip repositories yet
* pip install git+ssh://git@github.com/erguzel/exc-help.git

### Executing program

* Simply reference to your module

```
import exchelp.exception_helper as eh

try:
    12/0
except Exception as e:
    eh.CoreException('Some calculation failed',cause=e,logIt=True,dontThrow=False,shouldExit=False).addData('someDataKey','someDataValue').Act()

```

Some data key-value pairs can be added to exception.

```
import exchelp.exception_helper as eh

try:
    12/0
except Exception as e:
    eh.CoreException('Some calculation failed',cause=e,logIt=True,dontThrow=False,shouldExit=False).addData('someDataKey','someDataValue').Act()
```

output

```
{"message": "Some calculation failed", "_file": "/Users/olgunerguzel/Workspace/exc-help/src/main.py", "_line": 4, "someDataKey": "someDataValue", "_timeStamp": "2022-12-12 13:19:00.336627", "_env": "oe-ws-main.local", "_class": "CoreException", "_cause": {"_str": "division by zero", "_class": "ZeroDivisionError"}}
Traceback (most recent call last):
  File "/Users/olgunerguzel/Workspace/exc-help/src/main.py", line 4, in <module>
    12/0
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/olgunerguzel/Workspace/exc-help/src/main.py", line 6, in <module>
    eh.CoreException('Some calculation failed',cause=e,logIt=True,dontThrow=False,shouldExit=False).addData('someDataKey','someDataValue').Act()
  File "/Users/olgunerguzel/Workspace/exc-help/src/exchelp/exception_helper.py", line 157, in Act
    raise self
exchelp.exception_helper.CoreException: Some calculation failed

```

## Help

Check given variable type, do not throw but log as json in case of exception

```
age = 12

try:
    eh.check_type(age,str,typecheckmode=eh.TypeCheckMode.TYPE)
except Exception as e:
    eh.CoreException('Type check for xxx operation error',cause=e,dontThrow=True,logIt=True).Act()

```

output:

```

{"message": "Type check for xxx operation error", "_file": "/Users/olgunerguzel/Workspace/exc-help/src/main.py", "_line": 7, "_timeStamp": "2022-12-12 13:58:46.390028", "_env": "oe-ws-main.local", "_class": "CoreException", "_cause": {"message": "given instance variable 12 is not in expected TypeCheckMode.SUBTYPE of <class 'str'>", "_timeStamp": "2022-12-12 13:58:46.390007", "_class": "TypeMismatchException"}}

```

Example usage

```
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

```

output:

```

{
 "message": "sum_divide_function failure",
 "_file": "~/Workspace/exc-help/tests/exchelp/test_exception_helper.py",
 "_line": 11,
 "report": {
  "remark": "sum var would be 7",
  "who": {
   "name": "human",
   "locals": {
    "a": 3,
    "b": 4,
    "d": 0,
    "sum": 7,
    "e": {
     "_repr": "ZeroDivisionError('division by zero')"
    }
   }
  }
 },
 "someList": [
  1,
  2,
  3,
  "4"
 ],
 "someSet": [
  1,
  2,
  "3"
 ],
 "someTuple": [
  3,
  4,
  5,
  "3"
 ],
 "some single tuplike": 255,
 "someType": "<not-serializable>",
 "someByteStr": "b'hello world'",
 "someBytes": "b'\\x07\\x08\\t\\xff'",
 "byteArr": "b'\\x04\\x05\\x07'",
 "byteArrStr": "b'hello world'",
 "_timeStamp": "2022-12-23 12:23:32.678820",
 "_env": "oe-ws-main.local",
 "_class": "CoreException",
 "_cause": {
  "_repr": "ZeroDivisionError('division by zero')"
 },
 "_repr": "CoreException('sum_divide_function failure', ZeroDivisionError('division by zero'))"
}


```




## Authors

Contributors names and contact info

 olgunerguzel@gmail.com

## Version History

* Initial release 1.0.0

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

