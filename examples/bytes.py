# Usage of builtin function bytes.
# Keywords:
# bytes / encode / decode / utf-8 / chr / ord

as_bytes = "ABC".encode()  # ASCII 65 66 67
print([byte for byte in as_bytes])  # [65, 66, 67]
print(chr(as_bytes[0]), ord('A'))  # A 65

as_bytes = bytes("hello world", "utf-8")  # b'hello world' (representation of an object of type bytes)
as_str = as_bytes.decode("utf-8")  # hello world
