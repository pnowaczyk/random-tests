from incubator.hello import Hello


class TestHello():
    def test_say_contains_name(self):
        name = 'FRIDAY replacement for J.A.R.V.I.S'
        h = Hello(name)
        assert name in h.say()
