# -*- coding:utf-8 -*-

# 使用python自带的json，将数据转换为json数据时，datetime格式的数据报错：datetimeTypeError: datetime.datetime(2017, 3, 21, 2, 11, 21) is not JSON serializable。
#
# 解决方法:
# 就是重写构造json类，遇到日期特殊处理，其余的用内置的就行。

import json
import datetime

import numpy


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        elif isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        elif isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)

        raise TypeError("Unknown type")



        # 使用时，调用上面定义的函数即可，如下：
        #     print( json.dumps(self_data, cls=DateEncoder)  )
