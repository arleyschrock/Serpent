# -*- coding: utf-8 -*-
# Serpent: ast.literal_eval() compatible object tree serialization.
# Copyright 2013, Irmen de Jong (irmen@razorvine.net)
# Software license: "MIT software license". See http://opensource.org/licenses/MIT

from distutils.core import setup

import serpent

setup(
    name='serpent',
    version=serpent.__version__,
    py_modules = ["serpent"],
    license='MIT',
    author='Irmen de Jong',
    author_email='irmen@razorvine.net',
    description='Serialization based on ast.literal_eval',
    long_description="""
Serpent is a simple serialization library based on ast.literal_eval.

Because it only serializes literals and recreates the objects using ast.literal_eval(),
the serialized data is safe to transport to other machines (over the network for instance)
and de-serialize it there.

**API**

- ``ser_bytes = serpent.serialize(obj, indent=False)``      # serialize obj tree to bytes
- ``obj = serpent.deserialize(ser_bytes)``     # deserialize bytes back into object tree
- You can use ``ast.literal_eval`` yourself to deserialize, but ``serpent.deserialize`` works around a few corner cases. See source for details.

Serpent is more sophisticated than a simple repr() + literal_eval():

- it serializes directly to bytes (utf-8 encoded), instead of a string, so it can immediately be saved to a file or sent over a socket
- it encodes byte-types as base-64 instead of inefficient escaping notation that repr would use (this does mean you have
  to base-64 decode these strings manually on the receiving side to get your bytes back)
- it contains a few custom serializers for several additional Python types such as uuid, datetime, array and decimal
- it tries to serialize unrecognised types as a dict (you can control this with __getstate__ on your own types)
- it can create a pretty-printed (indented) output for readability purposes
- it outputs the keys of sets and dicts in alphabetical order (when pretty-printing)
- it works around a few quirks of ast.literal_eval() on the various Python implementations

Serpent allows comments in the serialized data (because it is just Python source code).
Serpent can't serialize object graphs (when an object refers to itself); it will then crash with a recursion error.

Works with Python 2.6+ (including 3.x), IronPython 2.7+, Jython 2.7+.

*There is also a Java and a .NET (C#) implementation available. This allows for easy data transfer between the various ecosystems.
You can get the full source distribution, a Java .jar file, and a .NET assembly dll.*  `Download location here <http://irmen.home.xs4all.nl/serpent/>`_


**Demo**

.. code:: python

 # This demo script is written for Python 3.2+
 # -*- coding: utf-8 -*-
 from __future__ import print_function
 import ast
 import uuid
 import datetime
 import pprint
 import serpent


 class DemoClass:
     def __init__(self):
         self.i=42
         self.b=False

 data = {
     "names": ["Harry", "Sally", "Peter"],
     "big": 2**200,
     "colorset": { "red", "green" },
     "id": uuid.uuid4(),
     "timestamp": datetime.datetime.now(),
     "class": DemoClass(),
     "unicode": "€"
 }

 # serialize it
 ser = serpent.serialize(data, indent=True)
 open("data.serpent", "wb").write(ser)

 print("Serialized form:")
 print(ser.decode("utf-8"))

 # read it back
 ser = open("data.serpent", "rb").read()
 data = serpent.deserialize(ser)
 print("Data:")
 pprint.pprint(data)

 # you can also use ast.literal_eval if you like
 ser_string = open("data.serpent", "r", encoding="utf-8").read()
 data2 = ast.literal_eval(ser_string)

 assert data2==data


When you run this (with python 3.2+) it prints:

.. code:: python

 Serialized form:
 # serpent utf-8 python3.2
 {
   'big': 1606938044258990275541962092341162602522202993782792835301376,
   'class': {
     '__class__': 'DemoClass',
     'b': False,
     'i': 42
   },
   'colorset': {
     'green',
     'red'
   },
   'id': 'e461378a-201d-4844-8119-7c1570d9d186',
   'names': [
     'Harry',
     'Sally',
     'Peter'
   ],
   'timestamp': '2013-04-02T00:23:00.924000',
   'unicode': '€'
 }
 Data:
 {'big': 1606938044258990275541962092341162602522202993782792835301376,
  'class': {'__class__': 'DemoClass', 'b': False, 'i': 42},
  'colorset': {'green', 'red'},
  'id': 'e461378a-201d-4844-8119-7c1570d9d186',
  'names': ['Harry', 'Sally', 'Peter'],
  'timestamp': '2013-04-02T00:23:00.924000',
  'unicode': '€'}
    """,

    keywords="serialization",
    platforms="any",
    classifiers= [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development"
    ],

)
