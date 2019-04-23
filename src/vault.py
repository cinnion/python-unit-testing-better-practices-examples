'''
Created on Apr 21, 2019

@author: cinnion
'''

import nacl.secret
import nacl.utils
import os
import sys

class Vault(object):
    """
    This class implements the Vault object, used to store and decode secrets stored in a securely encrypted format.
    """

    SECRET_KEY_FILE_NAME = "xyzzy"
    """
    The name of the file containing our secret.
    """
    
    @staticmethod
    def _find(pathname, matchFunc=os.path.isfile):
        """
        Search the Python search path for a file.
        
        @param pathname: The pathname of the file for which we are searching.
        @param matchFunc: The function to use for matching the file, defaulting to os.path.isfile.
        
        @return: The path to the file
        
        @raise RuntimeError: If the file cannot be found.
        """
        for dirname in sys.path:
            candidate = os.path.join(dirname, pathname)
            if matchFunc(candidate):
                return candidate
            
        raise RuntimeError("Can't find file {0!s}".format(pathname))

    @staticmethod
    def getKeyFilePath():
        """
        Search the Python search path for the secret key file.
        """
        try:
            keyfile_path = Vault._find(Vault.SECRET_KEY_FILE_NAME)
        except:
            keyfile_path = os.path.join(sys.path[0], Vault.SECRET_KEY_FILE_NAME)
        
        return keyfile_path

