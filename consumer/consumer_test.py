import atexit
import unittest

from pact import Consumer, Provider, Term

from .consumer import user

pact = Consumer('Consumer').has_pact_with(Provider('Provider'))
pact.start_service()
atexit.register(pact.stop_service)


class GetUserInfoContract(unittest.TestCase):
    def test_get_user(self):
        expected = {
            'username': 'UserA',
            'id': 123,
            'groups': ['Editors'],
            'last_modified': Term(r'\d+-\d+-\d+T\d+:\d+:\d+', '2016-12-15T20:16:01'),
        }

        (pact
         .given('UserA exists and is not an administrator')
         .upon_receiving('a request for UserA')
         .with_request('get', '/users/UserA')
         .will_respond_with(200, body=expected))

        with pact:
            result = user('UserA')

        expected_result = expected.copy()
        expected_result['last_modified'] = expected_result['last_modified']._generate
        self.assertEqual(result, expected_result)
