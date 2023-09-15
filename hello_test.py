import pytest

from hello import Hello


class TestClass:
    def test_hello(self):
        x = Hello("hello")
        x = x.greet("world")
        assert x == "hello world"
