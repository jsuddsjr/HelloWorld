import pytest

from hello import Hello


class TestClass:
    def test_hello(self):
        x = Hello()
        x = x.greet("mom")
        assert x == "Hello mom!"
