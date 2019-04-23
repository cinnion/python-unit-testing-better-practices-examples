#!/usr/bin/env python3.6

import unittest
from unittest.mock import patch
import os
import sys

from vault import Vault


class TestVault(unittest.TestCase):

    def test_find_found(self):

        self.assertEqual(Vault._find("test_vault.py"), os.path.abspath(__file__))

    def test_find_matcher_wrong_type_error(self):
        with self.assertRaisesRegex(RuntimeError, "Can't find file test_vault.py"):
            Vault._find("test_vault.py", os.path.isdir)

    #
    # Isn't this a more meaningful name?
    #
    def test_find_matcherWrongType_RaisesError(self):
        with self.assertRaisesRegex(RuntimeError, "Can't find file test_vault.py"):
            Vault._find("test_vault.py", os.path.isdir)

    def test_find_not_found(self):
        with self.assertRaisesRegex(RuntimeError, "Can't find file test_vault2.py"):
            Vault._find("test_vault2.py")


    def test_getKeyFilePath_FileFound_ReturnsFoundPath(self):

        ## Setup
        find_returns = 'This is the found file'
        with patch('vault.Vault._find') as mocked_find:
            mocked_find.return_value = find_returns

            ## Test
            results = Vault.getKeyFilePath()
        
            ## Assert
            self.assertEqual(results, find_returns)
            mocked_find.assert_called_with(Vault.SECRET_KEY_FILE_NAME)
            
    def test_getKeyFilePath_FileNotFound_ReturnsNewPath(self):

        ## Setup
        expected_path = os.path.join(sys.path[0], Vault.SECRET_KEY_FILE_NAME)
        with patch('vault.Vault._find') as mocked_find:
            mocked_find.side_effect = RuntimeError("Can't find file")

            ## Test
            results = Vault.getKeyFilePath()

            ## Assert
            self.assertEqual(results, expected_path)
            mocked_find.assert_called_with(Vault.SECRET_KEY_FILE_NAME)
                    
if __name__ == '__main__':
    unittest.main()
