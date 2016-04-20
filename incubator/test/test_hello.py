import unittest

from incubator.hello import Hello


class TestHello(unittest.TestCase):
    def test_say_contains_name(self):
        name = 'FRIDAY replacement for J.A.R.V.I.S'
        h = Hello(name)
        self.assertIn(name, h.say())


if __name__ == '__main__':
    unittest.main()
