"""A simple webframework """

before_hooks = []
mapping = []

def default_notfound():
    return "Not Found"

notfound = default_notfound

def request(url):
    for h in before_hooks:
        h(url)

    for pattern, f in mapping:
        if pattern == url:
            return f()

    return notfound()

def before_request(f):
    before_hooks.append(f)
    return f

def route(path):
    #print "route", path, mapping
    def decorator(f):
        mapping.append((path,f))
        #print "decorator" , f, mapping
        return f
    return decorator

def on_notfound(f):
    global notfound
    notfound = f
    return f
