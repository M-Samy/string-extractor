from unittest import TestCase
from Extractor import Finder
from utils.helpers import validate


class TestHelper(TestCase):

    def setUp(self):
        self.string_list = ["asd", "asdd", "fre", "glk", "lmk", "example", "lempexa", "mkl",
                            "apmlexe", "peaxmel", "same_string", "exepmal"]
        self.emptyListFinder = Finder(string_list=[])

    def test_passed_list_type(self):
        result = validate(self.string_list)
        self.assertEqual(result.status, True)
        self.assertEqual(result.status_code, 200)

    def test_pass_empty_list(self):
        result = self.emptyListFinder.match('EMPTY_LIST')
        self.assertEqual(result.status, False)
        self.assertEqual(result.status_code, 400)

    def test_passed_not_valid_list_type(self):
        result = validate(string_list=None)
        self.assertEqual(result.status, False)
        self.assertEqual(result.status_code, 400)
