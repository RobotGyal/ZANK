from unittest import TestCase, main as unittest_main, mock  # testing framework
from bson.objectid import ObjectId  # testing the database documents
from app import app


class ZankTests(TestCase):
    '''Tests for the Zank Flask web app.'''
    def setUp(self):
        '''Create a testing client, will be needed for each test.'''
        self.client = app.test_client()

        # show errors from Flask that are raised in testing
        app.config['TESTING'] = True

    # Home Page Route Test
    def test_home_page(self):
        '''User is able to get the home page, and see intro info about Zank.'''
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')

    # Show Route Test
    sample_code_id = ObjectId('5d55cffc4a3d4031f42827a3')
    # sample document in the db (fields may differ from what's below slightly)
    sample_code = {
        'title': "Guardrail Height Rules",
        "description": "A guardrail in an office space is at least 4 ft tall.",
    }


if __name__ == '__main__':
    unittest_main()
