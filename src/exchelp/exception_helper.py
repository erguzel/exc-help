#exchelp
# Includes exception types to handle exceptions in genera
#
import json
import socket
import sys
from enum import Enum
from  datetime import  datetime

#
# Enums related to exception handling
#
class TypeCheckMode(Enum):
    TYPE = 1
    SUBTYPE = 2

#
# Util Funcitons
#def check_type(instance: object, ttype:type,typecheckmode: TypeCheckMode = TypeCheckMode.TYPE,shouldThrow=False,
#               shouldLog:bool=False,file:str=None,line:int=None)->bool:
#
def check_type(instance: object, ttype:type,typecheckmode: TypeCheckMode = TypeCheckMode.TYPE,shouldThrow=False,
               shouldLog:bool=False,file:str=None,line:int=None)->bool:
    """
    checks the instance type if it matches with ttype
    :param instance: variable to check type
    :param ttype: the type to be compared
    :param typecheckmode: check mode: TYPE checks with type() method
                                      SUBTYPE checks with isinstance() method
    :param strictmode: throws exception if true when type mismatch detected
    :return: True if types are matching
    """

    exception  = TypeMismatchException(f"given instance variable {instance} is not in expected "
                                       f"{typecheckmode} of {ttype}").shouldLog(shouldLog)

    if(instance is None):
        return True

    subtypeMatchCondition:bool = isinstance(instance,ttype)
    typeMatchCondition:bool = type(instance) is ttype

    result = True
    match typecheckmode:
        case TypeCheckMode.SUBTYPE:
            if (not subtypeMatchCondition):
                result = False
        case TypeCheckMode.TYPE:
            if (not typeMatchCondition ):
                result = False
        case _:
            if(file != None and line != None):
                TypeMismatchException(f'fiven enum type {typecheckmode} is in default value',
                                      shouldLog=shouldLog).ActWithLineAndFile(lineNo=line,module=file)
            TypeMismatchException(f'fiven enum type {typecheckmode} is in default value', shouldLog=shouldLog).Act()

    if(shouldThrow):
        if(not result):
            if(file != None and line != None):
                exception.ActWithLineAndFile(module=file,lineNo=line)
            exception.Act()

    return result

"""
Static helper methods for exception handling
"""
class ExceptionHelpers:
    @staticmethod
    def dictionarize(exception:Exception) ->str:
        """
                Dictionarize exception
                :param exception: exception object to dictionarize
                :return: return dictionarized string of exception object
        """
      
        exception.__dict__["_class"]=exception.__class__.__name__
        #if(len(exception.__str__())>0):
           # exception.__dict__["_str"] = exception.__str__()
        cause:Exception = exception.__cause__;
        if(cause != None):
            #if(len(cause.__str__())>0):
                #cause.__dict__["_str"]=cause.__str__()
            exception.__dict__["_cause"] = {key: val for key, val in ExceptionHelpers.dictionarize(cause).items() if key not in ["shouldExit","logIt","dontThrow","_env"]}
        
        return exception.__dict__
    @staticmethod
    def jsonize(exception:Exception) ->str:
        """
        Jsonizes exception object
        :param exception: exception to jsonize
        :return: Json string as exception
        """
        filteredDict = {key: val for key, val in ExceptionHelpers.dictionarize(exception).items() if key not in ["shouldExit","logIt","dontThrow"]}

        return json.dumps(filteredDict)
#
# Base Core exception
#
class CoreException(Exception,BaseException):
    def __init__(self,message:str=None,cause:Exception=None,dontThrow:bool=False,logIt:bool=False,shouldExit:bool=False):
        """
        Initializes core exception object
        :param message: exception message
        :param cause: exception cause as exception
        :param dontThrow: true if it is not to be thrwn at Act function call
        :param logIt: true if it is to be logged at Act funciton call
        """
        self.message=message
        self.__cause__= cause
        self.dontThrow = dontThrow
        self.logIt = logIt
        self.__initLineNo__()
        self.shouldExit = shouldExit
       # print("Exception type: ", exception_type)
       # print("File name: ", filename)
       # print("Line number: ", line_number)
    def __initLineNo__(self):
        """
        checks already thrown exception at the time of initialization
        get file and line info from sys.exc_info call
        """
        exception_type, exception_object, exception_traceback = sys.exc_info()
        if (exception_traceback != None):
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            self.__dict__['_file'] = filename
            self.__dict__['_line'] = line_number

    def ActWithLineAndFile(self,lineNo,module):
        """
        Adds line number and module name to dict object before calling Act method
        """
        if(not self.__dict__.__contains__('_line')):
           #self.__dict__['_line'] = sys._getframe().f_lineno
            self.__dict__['_line'] = lineNo

        if(not  self.__dict__.__contains__('_file')):
           # self.__dict__['_file']=sys.modules[__name__].__file__
            self.__dict__['_file']=module

        self.Act()

    def Act(self):
        """
        Acts according to log or throw boolean
        throws itself if throw boolean true at the moment of Act function
        logs exception if log boolean true at the moment of Act function
        :return: nothing
        """
        self.__dict__['_timeStamp']=datetime.now().__str__()
        self.__dict__['_env']= socket.gethostname()
        #self.__dict__['_env']= socket.gethostname()
        if(self.logIt):
            print(ExceptionHelpers.jsonize(self))

        if(not self.dontThrow):
            raise self
        
        if(self.shouldExit):
            exit(-1)

    def addData(self,key:object, value:object):
        """
        Adds data to dict object
        """
        self.__dict__[key] = value
        return self

    def shouldLog(self,shouldLog:bool):
        """
        Sets loggin boolean
        :param shouldLog: true if exception to be logged as json in Act function call
        :return: nothing
        """
        self.logIt = shouldLog
        return self
    def shouldThrow(self,shouldThrow:bool):
        """
        Sets throw boolean
        :param shouldThrow: true if throw itself in Act function call
        :return: nothing
        """
        self.dontThrow = not shouldThrow
        return self
    def shouldExit(self,shouldExit:bool):
        """
        Sets exit boolean
        :param shouldExit: if true exit appliation at Act function call
        :return: nothing
        """
        self.dontThrow = not shouldExit
        return self



"""
Thworn when a code snippet is interrupted by an unknown excepotion
Set actual exception as cause in catch block
"""
class UnknownExceptionCaughtException(CoreException):
    def __init__(self,message:str,cause:Exception=None,dontThrow:bool=False,logIt:bool=False,shouldExit = False):
        """
        Initializes object
        :param message: Exception message
        :param cause: Exception cause as exception
        :param dontThrow: true if it is not to be thrown
        :param logIt: true if exceptionto be logged as json
        """
        super(UnknownExceptionCaughtException, self)\
            .__init__(message=message,cause=cause,dontThrow=dontThrow,logIt=logIt,shouldExit=shouldExit)

"""
Thworn when a type mismatch caught
Set actual exception as cause in catch block
"""
class TypeMismatchException(CoreException):
    def __init__(self,message:str,cause:Exception=None,dontThrow:bool=False,logIt:bool=False,shouldExit = False):
        """
        Initializes object
        :param message: Exception message
        :param cause: Exception cause as exception
        :param dontThrow: true if it is not to be thrown
        :param logIt: true if exceptionto be logged as json
        """
        super(TypeMismatchException, self)\
            .__init__(message=message,cause=cause,dontThrow=dontThrow,logIt=logIt,shouldExit=shouldExit)



  