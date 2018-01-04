"""
场景：json.load(file) 时，得到的数据编码格式为unicode
作用：将unicode编码格式转为utf-8编码格式
说明：input为load出来的json数据<type 'dict'>
Time: 2018/01/04 11:20
"""


def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
