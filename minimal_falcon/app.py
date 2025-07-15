import falcon
import os

BASE_DIR = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

class PageResource:
    def on_get(self, req, resp, page = 'index'):
        filepath = os.path.join(TEMPLATES_DIR, f'{page}.html')
        try:
            with open(filepath, 'r', encoding = 'utf-8') as f:
                resp.text = f.read()
            resp.content_type = 'text/html'
        except FileNotFoundError:
            resp.status = falcon.HTTP_404
            resp.text = 'File not found'

app = falcon.App()

app.add_route('/', PageResource())
app.add_route('/{page}', PageResource())
