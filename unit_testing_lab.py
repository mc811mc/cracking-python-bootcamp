import unittest

class UnitTesting(unittest.TestCase):

    def test_abs(self):
        self.assertEqual(100, abs(-100))

    def test_bin(self):
        self.assertEqual('01101000', bin(h))

    def test_bool(self):
        self.assertTrue(True)

    # Return False
    def test_callable(self):
        x = 5
        self.assertTrue(True, callable(x))

    def test_chr(self):
        self.assertEqual(A, chr(65))

    def test_dict(self):
        self.assertEqual(dict(a=1, b=2, c=3, d=4), {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_divmond(self):
        self.assert(, divmod())
    
    def test_enumerate(self):
        self.assert(, enumerate())

    def test_float(self):
        self.assert(, float())

    def test_format(self):
        self.assert(, hex())

    def test_hex(self):
        self.assert(, int())

    def test_int(self):
        self.assert(, len())

    def test_len(self):
        self.assert(, list())

    def test_list(self):
        self.assert(, max())
    
    def test_max(self):
        self.assert(, min())

    def test_min(self):
        self.assert(, next())

    def test_next(self):
        self.assert(, oct())

    def test_oct(self):
        self.assert(, sorted())

    def test_sorted(self):
        self.assert(, sum())
    
    def test_sum(self):
        self.assertEqual(5 + 15, 20)

if __name__ == '__main__':
    unit_testing_lab.main()