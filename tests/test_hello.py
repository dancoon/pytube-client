import pytest

from pytube_client import say_hello


def test_say_hello(capfd):
    say_hello()
    out, err = capfd.readouterr()
    assert out == "Hello, Our first python package!\n"
