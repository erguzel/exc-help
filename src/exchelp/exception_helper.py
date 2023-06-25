#exchelp
# Includes exception types to handle exceptions and report carriers
#
from __future__ import annotations
import json
from json import JSONEncoder
import sys
from enum import Enum


class baseall(object):
    def __init__(self) -> None:
        pass

    def isin(self, *keyorelms):
        if hasattr(self,'kwargs'):
            for key in keyorelms:
                if key in self.kwargs:
                    return True
        if hasattr(self,'args'):
            for key in keyorelms:
                if key in self.args:
                    return True
        return False
    
class kwargsbase(baseall):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        baseall.__init__(self)
    
    def addkvp(self,**kwargs):
        self.kwargs = self.kwargs | kwargs
        return self
    
    def popkvp(self,*keys):
        for key in keys:
            if key in self.kwargs:
                return self.kwargs.pop(key)

    def getkvp(self,key):
        if key in self.kwargs:
            return self.kwargs[key]

class argsbase(baseall):
    def __init__(self,*args):
        self.args = args
        baseall.__init__(self)
    
    def addelm(self, *args):
        self.args = self.args + args
        return self
    
    def popelm(self,index):
        res = self.args[index] if index < len(self.args) else None
        self.args = self.args[0:index] + self.args[index+1:]
        return res
    
    def getelm(self,index):
        pass


class argskwargssbase(argsbase,kwargsbase):
    def __init__(self,*args,**kwargs):
        argsbase.__init__(self,*args)
        kwargsbase.__init__(self,**kwargs)  
        
        

class JsonEncoders():
    def __init__(self) -> None:
        pass
    
    class DefaultJsonEncoder(JSONEncoder):
        def default(self,o):
            try:
                if is_jsondumpable(o) :return o 
                if isinstance(o,bytes):
                    return self.default(o=str(o))
                if isinstance(o,bytearray):
                    return self.default(o=str(bytes(o)))
                if isinstance(o,set):
                    return self.default(o=list(o))
                if hasattr(o,'__dict__'):
                    if isinstance(o,BaseException):
                        o.__dict__['_repr']=repr(o)
                    return self.default(o=o.__dict__)
                if isinstance(o,tuple):
                    return self.default(o=list(o))
                ## try iterate
                try:
                    for idx, el in enumerate(o):
                        isDict = isinstance(o,dict)
                        val = o[el] if isDict else o[idx]
                        val = self.default(o=val)
                        o[el if isDict else idx] = val
                    o = self.default(o=o)
                except Exception as e:## not iterable meaning unguessed type
                    o = self.default(o='<not-serializable>')
                return o
            except Exception as e:
                raise TypeError('dictionarize_data failed',e)
            


def is_jsondumpable(data)->bool:
    try:
        json.dumps(data)
        return True
    except:
        return False

class CoreException(argskwargssbase,Exception,BaseException):
    """
    kwargs:
    log : Logs json if true
    exit: Exists application without raising the actual exception
    throw: Raises the occured exception. In case of cover exception, it raises the actual(inner) exception
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def act(self, innerexception=None):
        acceptedactions = ('True','true','TRUE', True)

        if 'log' in self.kwargs:
            if  self.kwargs['log'] in acceptedactions:
                print(json.dumps(self,cls=JsonEncoders.DefaultJsonEncoder,indent=2))
        if 'exit' in self.kwargs:
            if self.kwargs['exit'] in acceptedactions:
                sys.exit('System is interrupted with a raised interruption object. Program is ended by user before raising the actual exception.')
        if 'throw' in self.kwargs:
            if self.kwargs['throw'] in acceptedactions:
                raise innerexception if innerexception else self

class CoverException(CoreException):
    """
    kwargs:
    log : Logs json if true
    exit: Exists application without raising the actual exception
    throw: Raises the occured exception. In case of cover exception, it raises the actual(inner) exception
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def act(self,innerexception):
        self.innerexception = innerexception
        return super().act(innerexception=innerexception)

class ReportObject():
    def __init__(self, **kwargs) -> None:
        self.__dict__ = self.__dict__ | kwargs
    def adddata(self,**kwargs):
        self.__dict__ = self.__dict__ | kwargs
        return self
    def toJson(self,verbose = False):
        js = json.dumps(self,cls = JsonEncoders.DefaultJsonEncoder,indent=2)
        if verbose:
            print(js)
        return js
    def getdata(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        return None



class TypeCheckMode(Enum):
    TYPE = 1
    SUBTYPE = 2
    #
    #
    #
def check_type(instance: object, ttype:type,typecheckmode: TypeCheckMode = TypeCheckMode.TYPE)->bool:
    """
    checks the instance type if it matches with ttype
    :param instance: variable to check type
    :param ttype: the type to be compared
    :param typecheckmode: check mode: TYPE checks with type() method
                                      SUBTYPE checks with isinstance() method
    :param strictmode: throws exception if true when type mismatch detected
    :return: True if types are matching
    """
    try:
        if typecheckmode == TypeCheckMode.SUBTYPE:
            if type(ttype) is tuple:
                if None in ttype:
                    raise TypeError('None can not be a candidate for a subtype check. Use type mode instead for None check')
        
        if typecheckmode == TypeCheckMode.TYPE:
            if type(ttype) != type:
                raise TypeError('ttype must be a type for a type check')

        match typecheckmode:
            case TypeCheckMode.SUBTYPE:
                return isinstance(instance,ttype)
            case TypeCheckMode.TYPE:
                return type(instance) ==  ttype
            case _:
                TypeError(f'Given enum type {typecheckmode} is in default value')       
    except Exception as e:
        raise  TypeError(f"Type checking failed",e)


class ReportObject():
    def __init__(self, **kwargs) -> None:
        self.__dict__ = self.__dict__ | kwargs
    def adddata(self,**kwargs):
        self.__dict__ = self.__dict__ | kwargs
        return self
    def toJson(self,verbose = False):
        js = json.dumps(self,cls = JsonEncoders.DefaultJsonEncoder,indent=2)
        if verbose:
            print(js)
        return js
