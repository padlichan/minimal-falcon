from wsgiref import simple_server
from app import app

if __name__ == "__main__":
    with simple_server.make_server("127.0.0.1", 8000, app) as httpd:
        print("Serving on http://127.0.0.1:8000")
        httpd.serve_forever()