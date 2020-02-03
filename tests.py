from unittest import TestCase, main as unittest_main
from app import app


class ZankTests(TestCase):
    '''Tests for the Zank Flask web app.'''
    def setUp(self):
        '''Create a testing client, will be needed for each test.'''
        self.client = app.test_client()

        # show errors from Flask that are raised in testing
        app.config['TESTING'] = True

    def test_home_page(self):
        '''User is able to get the home page, and see intro info about Zank.'''
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')


if __name__ == '__main__':
    unittest_main()
