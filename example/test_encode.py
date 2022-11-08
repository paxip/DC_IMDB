
from hypothesis import given
from example.encode import Encoder
import hypothesis.strategies as st
import unittest

class TestEncoding(unittest.TestCase):
    @given(st.text())
    def test_decode_inverts_encode(self, s):
        self.assertEqual(decode(encode(s)), s)
        
unittest.main(argv=[''], verbosity=2, exit=False)