"""The web application calling the web framework bicycle"""

from bicycle import request, before_request, route
import time

@before_request
def log_request(url):
    print time.asctime(), url

@route("/")
def index:
    return "Welcome"

def main():
    print request("/")

if __name__ == "__main__":
    main()
