from flask import Flask
import hashlib
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/hash/<hash_string>')
def encrypt_string(hash_string):
    hash_string = hash_string.lower()
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

if __name__ == '__main__':
   app.run(debug=True)
