#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__="""
Gets options from the console command, Format the options and return a dict.  This is similar to the way non-GNU Unix systems work.

## Example
```python
import GetOptions
params_config = {
        'host':     {'must': False,  'data': True,    'short': 'H',    'long': 'host',  'default': 'localhost'},
        'port':     {'must': False,  'data': True,    'short': 'O',    'long': 'port',  'default': 3306},
        'user':     {'must': True,   'data': True,    'short': 'U',    'long': 'user'},
        'passwd':   {'must': True,   'data': True,    'short': 'P',    'long': 'passwd'},
        'db':       {'must': True,   'data': True,    'short': 'D',    'long': 'db'},
        'init':     {'must': True,   'data': False,   'short': 'I',    'long': 'init'},
    }
print(GetOptions.get(params_config))
```
+ Shell command: 
    - `python3 test.py -H localhost -U root -P abc123 -D thinkvue -I abc 123`
+ Print result:
    - `{'data': {'host': 'localhost', 'port': 3306, 'user': 'root', 'passwd': 'abc123', 'db': 'thinkvue' , 'init': True}, 'args': ["abc", "123"]}`

## Parameter Description

`GetOptions.get(params_config, params=None, is_show_help=True)`
- `params_config`:<Required>{type:`dict`} A dict used to describe parameters, each primary key has 5 fields:
  + `key`:{type:`string`} The primary key in the result returned
  + `must`:{type:`bool`} This is a required option?
  + `data`:{type:`bool`} Does it have member data?
  + `short`:{type:`string`} The short parameter, example:`-s`
  + `long`:{type:`string`} The long parameter, example:`--longParam`
  + `default`:{type:`string`} Default value
- `params`:[optional]{type:`list`} Default `sys.argv`
- `is_show_help`:[optional]{type:`bool`} Show help?
"""

# name="GetOptions"
from .GetOptions import get

__version__ = "1.0.3"
