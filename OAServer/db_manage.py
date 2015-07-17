__author__ = 'Justin'

import json

def to_json(objs):
    jsObjs = []
    for temp in objs:
        dict = {}
        dict.update(temp.__dict__)
        jsObjs.append(dict)
    return jsObjs
