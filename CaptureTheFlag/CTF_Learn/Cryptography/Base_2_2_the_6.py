import base64
# Full url to this task: https://ctflearn.com/challenge/192
# Base64 encoding: https://pl.wikipedia.org/wiki/Base64
# library: https://docs.python.org/3/library/base64.html

encoded = b'Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9'
data = base64.b64decode(encoded)

print(data)