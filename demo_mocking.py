#!/usr/bin/env python
from demo_mocking_library import myapis


def foo():
    val = myapis.get_current_ip()
    if val == "127.0.0.0":
        return True
    else:
        return False
