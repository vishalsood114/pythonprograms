"""The web application calling the web framework bicycle"""

from bicycle import request, before_request, route, on_notfound
import time

@before_request
def log_request(url):
    print time.asctime(), url

#@route("/")
#def index():
#    return "Welcome"

def index():
    return "Welcome"

decor = route("/")
index = decor(index)

@route("/login")
def login():
    return "Please login to continue.\nLOGIN: ____\nPASSWORD:____\nSUBMIT"

@on_notfound
def not_found():
    return "404 - This is not the page your are looking for."

