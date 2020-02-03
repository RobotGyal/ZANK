from unittest import TestCase, main as unittest_main
from app import app


class ZankTests(TestCase):
    '''Tests for the Zank Flask web app.'''
    def setUp(self):
        '''Create a testing client, will be needed for each test.'''
        self.client = app.test_client()

        # show errors from Flask that are raised in testing
        app.config['TESTING'] = True


if __name__ == '__main__':
    unittest_main()
