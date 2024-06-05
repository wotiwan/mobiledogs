import hashlib


def hash_pass(password):
    hash = hashlib.new('md5')
    hash.update(password.encode())
    return hash.hexdigest()

