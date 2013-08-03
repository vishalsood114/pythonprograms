def json_encode(data):
    """ Takes a python data structure and converts it
    into a JSON string
    """
    if isinstance(data,bool):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance (data, (int,float)):
        return str(data)
    elif isinstance (data, str):
        return '"' + data + '"'
    elif isinstance (data, list):
        value = [json_encode(d) for d in data]
        return "[" + ",".join(value) +"]"
    elif isinstance (data, dict):
        values = [json_encode(keys) + ":" + json_encode(value) for keys,value in data.items()]
        return "{" + ",".join(values) +"}"

def show(x):
    print "%s\t%s" % (repr(x), json_encode(x))


show(True)
show(False)
show(1)
show(1.2)
show("hello")
show([1, 2, [3, 4, True]])
show({"a": [1, True], "b": {"name": "hello"}})
