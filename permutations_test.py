import collections
import unittest

from permutations import get_permutations

class TestPermutations(unittest.TestCase):

    def test_empty_string(self):
        self.assertEquals(get_permutations(""), [""])

    def test_aaa(self):
        self.assertEquals(get_permutations("aaa"), ["aaa"])

    def test_bob(self):
        self.assertEquals(collections.Counter(get_permutations("bob")), collections.Counter(["bob", "bbo", "obb"]))

    def test_cake(self):
        self.assertEquals(collections.Counter(get_permutations("cake")), collections.Counter(["keca", "acek", "acke", "aeck", "aekc", "akce", "akec", "caek", "cake", "ceak", "ceka", "ckae", "ckea", "eack", "eakc", "ecak", "ecka", "ekac", "ekca", "kace", "kaec", "kcae", "kcea", "keac"]))

if __name__ == '__main__':
    unittest.main()
