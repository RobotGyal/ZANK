from unittest import TestCase, main as unittest_main, mock  # testing framework
from bson.objectid import ObjectId  # testing the database documents
from app import app


class ZankTests(TestCase):
    '''Tests for the Zank Flask web app.'''
    def setUp(self):
        '''Create a testing client, will be needed for each test.'''
        self.client = app.test_client()

        # show errors from Flask that are raised during testing
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

    # Search feature Route Test
    def test_get_search_results(self):
        '''User is able to see codes relevant to a search query they input.'''
        pass

    # Show Route Test (this is used to display details for one page)
    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_code(self, mock_find):
        """User is sees a specific rule of the building code in full detail."""
        mock_find.return_value = sample_code
        # retrieve the page using the url pattern fpr the show route
        result = self.client.get(f'/codes/{sample_code_id}')  # may differ
        self.assertEqual(result.status, '200 OK')


if __name__ == '__main__':
    unittest_main()
