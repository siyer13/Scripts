import hashlib, uuid

def hash_string(val):
    salt = uuid.uuid4().hex
    hash_value = hashlib.sha256(val+salt).hexdigest()
    return hash_value


hash_value = hash_string("USA")
print hash_value
