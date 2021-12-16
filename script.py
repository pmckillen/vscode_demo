"""
high level support for doing this and that.
"""


import requests


r = requests.get("https://bbc.co.uk")
print(r.status_code)
