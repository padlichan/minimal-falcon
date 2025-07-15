from wsgiref import simple_server
from app import app

if __name__ == "__main__":
    with simple_server.make_server("0.0.0.0", 8080, app) as httpd:
        print("Serving on http://0.0.0.0:8080")
        httpd.serve_forever()