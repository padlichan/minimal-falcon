#import falcon
import falcon
from falcon import testing
from minimal_falcon.app import app

class TestPages(testing.TestCase):
    def setUp(self):
        super().setUp()
        self.app = app

    def test_index_page(self):
        response = self.simulate_get('/')
        assert response.status == falcon.HTTP_200
        assert 'text/html' in response.content_type