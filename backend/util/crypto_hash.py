import hashlib
import json
"""
The full-form of JSON is JavaScript Object Notation. It means that a script 
(executable) file which is made of text in a programming language, 
is used to store and transfer the data. 
Python supports JSON through a built-in package called json.
To use this feature, we import the json package in Python script. 
The text in JSON is done through quoted-string which 
contains the value in key-value mapping within { }. 
It is similar to the dictionary in Python.
"""
# def stringify(data):
#     return json.dumps(data)


def crypto_hash(*args):
    """ implemet SHA-256 on given arguments"""
    
    """
    json.dump()
json module in Python module provides a method called 
dump() which converts the Python objects into appropriate json objects. 
It is a slight variant of dumps() method.

The dumps() is used when the objects are required to be in 
string format and is used for parsing, printing, etc,
    """
    # A lambda function is a small anonymous function.
    # A lambda function can take any number of arguments, but can only have one expression.
    # The power of lambda is better shown when you use them as an anonymous function inside another function.
    
    """
    map() function returns a map object(which is an iterator) of the results 
    after applying the given function to each item of a given iterable (list, tuple etc.)
    
    Returns a list of the results after applying the given function  
    to each item of a given iterable (list, tuple etc.) 
    
    def addition(n): 
    return n + n 
  
    numbers = (1, 2, 3, 4) 
    result = map(addition, numbers) 
    print(list(result)) 
    
    Output : [2, 4, 6, 8]
        
    """
    # sort-used if the of input value change then the HASH value doesn't change
    stringified_args = sorted(map(lambda data:json.dumps(data) ,args))
    
    # print(f'stringified_args:{stringified_args}')
    joined_data = ''.join(stringified_args)
    # print(f'joined_data:{joined_data}')
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('GAUTY','MOHAN',3,534,'sad'):{crypto_hash('GAUTY','MOHAN',3,534,'sad')}")

if __name__=='__main__':
    main()