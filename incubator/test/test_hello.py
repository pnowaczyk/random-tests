import pytest
from incubator.hello import Hello


class TestHello:
    @pytest.mark.parametrize('name_input', [
        'J.A.R.V.I.S',
        'FRIDAY replacement for J.A.R.V.I.S',
    ])
    def test_say_contains_name(self, name_input):
        h = Hello(name_input)
        assert name_input in h.say()
