"""
high level support for doing this and that.
"""

import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who):

    greeting = f"Hello, {who}"
    return greeting


print(greet("World"))
print(greet("Pat"))
r = requests.get("https://bbc.co.uk")
print(r.status_code)
