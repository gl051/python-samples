#!/usr/bin/env python
from demo_mocking import foo

import unittest
from unittest.mock import patch


class FooTestCase(unittest.TestCase):

    # You patch from the module you are testing, since namespaces are imported
    @patch('demo_mocking.myapis')
    def test_foo(self, mock_a):
        # set up the mock
        mock_a.get_current_ip.return_value = "127.0.0.0"
        self.assertTrue(foo(), "Assert true")


if __name__ == '__main__':
    unittest.main()
