import unittest
from unittest.mock import patch
from app import *


class TestFunctions(unittest.TestCase):
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

    def test_check_document_existance_return_bool(self):
        self.assertTrue(check_document_existance('2207 876234'), True)
        self.assertTrue(check_document_existance('10006'), True)
        self.assertFalse(check_document_existance('100060'), False)

    @patch('builtins.input', side_effect = ['2207 876234', '11-2', '10006', '5455 028765'])
    def test_get_doc_owner_name(self, mock_input):
        self.assertIn(get_doc_owner_name(), ['Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'])

    def test_get_all_doc_owners_names(self):
        self.assertEqual(
            get_all_doc_owners_names(),
            {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'})

    def test_remove_doc_from_shelf(self):
        self.assertEqual(remove_doc_from_shelf('2207 876234'), '2207 876234')
        self.assertEqual(remove_doc_from_shelf('11-2'), '11-2')
        self.assertEqual(remove_doc_from_shelf('5455 028765'), '5455 028765')
        self.assertEqual(remove_doc_from_shelf('10006'), '10006')

    def test_add_new_shelf(self):
        self.assertTupleEqual(add_new_shelf(1), (1, True))
        self.assertTupleEqual(add_new_shelf(123), (123, True))

    def test_append_doc_to_shelf(self):
        append_doc_to_shelf('11-2', '3')
        self.assertIn('11-2', directories.get('3'))

    @patch('builtins.input', side_effect = ['11-2'])
    def test_delete_doc(self, mock_input):
        self.assertEqual(delete_doc(), ('11-2', True))

    @patch('builtins.input', side_effect = ['2207 876234', '11-2', '10006', '5455 028765'])
    def test_get_doc_shelf(self, mock_input):
        self.assertIn(get_doc_shelf(), ['1', '2', '3'])

    @patch('builtins.input', side_effect = ['123', 'passport', 'Justin Credible', 3])
    def test_add_new_doc(self, mock_input):
        self.assertEqual(add_new_doc(), 3)

    @patch('builtins.input', side_effect = ['q'])
    def test_secretary_program_start(self, mock_input):
        self.assertIsNone(secretary_program_start())


if __name__ == '__main__':
    unittest.main()