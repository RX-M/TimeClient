"""Unit tests & Mock for the time_client.py module"""

import unittest
from unittest.mock import patch
import time_client


class TestTimeClient(unittest.TestCase):
    """Unit tests for the time_client() function"""

    RESULT_PREFIX = "Received:"
    DATA = b"57601 16-08-01 19:51:43 50 0 0 458.2 UTC(NIST) *"

    def setUp(self):
        '''Patch socket so no connection is made, recv returns data'''
        patcher = patch('time_client.socket.socket',
                        spec=True, **{'recv.return_value': self.DATA})
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_no_args(self):
        '''Should return the time from default servers'''
        result = time_client.get_time()
        print(result)
        self.assertEqual(result[:len(self.RESULT_PREFIX)], self.RESULT_PREFIX)


if __name__ == '__main__':
    unittest.main()
