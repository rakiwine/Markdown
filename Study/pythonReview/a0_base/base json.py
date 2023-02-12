#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/24
# file: base json.py
# Email:
# Author: rakiwine 

import json

dict_ = {0: "0", 1: 1, 2: 2, 3: 3, 4: 4}


json_ = json.dumps(dict_)

print(json_)

# key值字符串 value类型相同
print(json.loads(json_))

# json.dump()
# json.load()