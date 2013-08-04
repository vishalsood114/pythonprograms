import webappl
from bicycle import request 

def main():
    print request("/")
    print request("/login")

if __name__ == "__main__":
        main()
