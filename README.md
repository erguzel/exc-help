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

output:

```

{
  "message": "sum_divide_function failure",
  "dontthrow": true,
  "logit": true,
  "_file": "/Users/olgunerguzel/Workspace/exc-help/tests/exchelp/test_exception_helper.py",
  "_line": 14,
  "shouldexit": true,
  "report": {
    "who": {
      "name": "human",
      "locals": {
        "a": 3,
        "b": 4,
        "d": 0,
        "sum": 7,
        "e": {
          "message": "some core cause exception",
          "dontthrow": false,
          "logit": false,
          "_file": "/Users/olgunerguzel/Workspace/exc-help/tests/exchelp/test_exception_helper.py",
          "_line": 12,
          "shouldexit": false,
          "sum": 7,
          "_timeStamp": "2022-12-23 20:52:54.115004",
          "_env": "oe-ws-main.local",
          "_repr": "CoreException('some core cause exception', ZeroDivisionError('division by zero'))"
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
    "3",
    1,
    2
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
  "_timeStamp": "2022-12-23 20:52:54.115049",
  "_env": "oe-ws-main.local",
  "_class": "CoverException",
  "_cause": {
    "message": "some core cause exception",
    "dontthrow": false,
    "logit": false,
    "_file": "/Users/olgunerguzel/Workspace/exc-help/tests/exchelp/test_exception_helper.py",
    "_line": 12,
    "shouldexit": false,
    "sum": 7,
    "_timeStamp": "2022-12-23 20:52:54.115004",
    "_repr": "CoreException('some core cause exception', ZeroDivisionError('division by zero'))"
  },
  "_repr": "CoverException('sum_divide_function failure')"
}


```




## Authors

Contributors names and contact info

 olgunerguzel@gmail.com

## Version History

* Initial release 1.0.0

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

