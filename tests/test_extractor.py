from unittest import TestCase
from Extractor import Finder


class TestFinder(TestCase):

    def setUp(self):
        self.string_list = ["asd", "asdd", "fre", "glk", "lmk", "example", "lempexa", "mkl",
                            "apmlexe", "peaxmel", "same_string", "exepmal"]
        self.emptyListFinder = Finder(string_list=[])
        self.finder = Finder(string_list=self.string_list)

    def test_single_match(self):
        result = self.finder.match('sad')
        self.assertEqual(result.status, True)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, ["asd"])

    def test_multiple_matches(self):
        result = self.finder.match('example')
        self.assertEqual(result.status, True)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, ["example", "lempexa", "apmlexe", "peaxmel", "exepmal"])

    def test_no_matches_with_case_sensitive(self):
        result = self.finder.match('Example')
        self.assertEqual(result.status, True)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, [])

    def test_match_for_the_same_string(self):
        result = self.finder.match('same_string')
        self.assertEqual(result.status, True)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, ["same_string"])

    def test_no_matches(self):
        result = self.finder.match('NO_MATCHES')
        self.assertEqual(result.status, True)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, [])

    def test_find_matches(self):
        self.assertEqual(
            self.finder.find(string="example"),
            ['example', 'lempexa', 'apmlexe', 'peaxmel', 'exepmal']
        )

    def test_find_no_matches(self):
        self.assertEqual(
            self.finder.find(string="backend"),
            []
        )
