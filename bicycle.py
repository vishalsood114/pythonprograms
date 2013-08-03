"""A simple webframework """

before_hooks = []

def request(url):
    for h in before_hooks:
        h(url)
    return "Not Found"

def before_request(f):
    before_hools.append(f)
    return f

def route(path):
    def fake_decor(f):
        return f

    return fake_decor


