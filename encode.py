import base64
password = "my_password".encode("utf-8")

decoded = base64.b64decode("bXlfcGFzc3dvcmQ=")
print(decoded)