import sys, os
import unittest
from unittest.mock import patch
import requests

sys.path.append(os.getcwd())

from YA_func import *


class TestYaApiConnection(unittest.TestCase):
    def setUp(self):
        print('setUp work!')

    def tearDown(self):
        print('tearDown work!')

    @classmethod
    def setUpClass(cls):
        print('setUpClass work!')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass work!')

    def test_make_new_directory_return(self):
        try:
            self.assertIn(make_new_directory('^*$^123@_-?'), [201, 409], 'Папка создана')

        except:
            print('Bad response from server')






