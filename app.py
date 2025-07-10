import falcon

class PageResource:
    def on_get(self, req, resp, page = 'index'):
        filepath = f'templates/{page}.html'
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
