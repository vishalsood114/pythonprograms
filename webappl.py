"""The web application calling the web framework bicycle"""

from bicycle import request, before_request, route, on_notfound
import time

@before_request
def log_request(url):
    print time.asctime(), url

@route("/")
def index():
    return "Welcome"

@on_notfound
def not_found():
    return "404 - This is not the page your are looking for."

def main():
    print request("/")

if __name__ == "__main__":
    main()
