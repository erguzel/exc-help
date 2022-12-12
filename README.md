# exc-help

exc-help exception helper package

## Description

exc-help is a core python project which is used to manage exceptions. It is designed in a pattern that one dedicated exception type is used to store and log the exception information in desired application state in json format. It also has a type checking method to identify the variable types, and to take action accordingly in the runtime.

## Getting Started

### Dependencies

* No dependency

### Installing

* Not available in pip repositories yet
* pip install git+ssh://git@github.com/erguzel/exc-help.git/

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
    eh.check_type(age,int,typecheckmode=eh.TypeCheckMode.TYPE,shouldThrow=True)
except Exception as e:
    eh.CoreException('Type check for xxx operation error',cause=e,dontThrow=True,logIt=True).Act()

```

output:

```

{"message": "Type check for xxx operation error", "_file": "/Users/olgunerguzel/Workspace/exc-help/src/main.py", "_line": 7, "_timeStamp": "2022-12-12 13:58:46.390028", "_env": "oe-ws-main.local", "_class": "CoreException", "_cause": {"message": "given instance variable 12 is not in expected TypeCheckMode.SUBTYPE of <class 'str'>", "_timeStamp": "2022-12-12 13:58:46.390007", "_class": "TypeMismatchException"}}

```

## Authors

Contributors names and contact info

 Olgun Erguezel

## Version History

* Initial release 1.0.0

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

