"""A simple webframework """

before_hooks = []

def default_notfound():
    return "Not Found"

notfound = default_notfound

def request(url):
    for h in before_hooks:
        h(url)
    return notfound()

def before_request(f):
    before_hooks.append(f)
    return f

def route(path):
    def fake_decor(f):
        return f

    return fake_decor

def on_notfound(f):
    global notfound
    notfound = f
    return f
