import hmac
import os
from Flask import flask, make_response, jsonify

app = Flask(__name__)


def token_gen(tokens):
    h = hmac.new(secret, token.to_bytes(8, 'big'))
    while True:
        tokens += 1
        h.update(tokens.to_bytes(8, 'big'))
        yield h.hexdigest()


@app.route('/api/token/validate')
def validate_token():
    if "Token" in request.headers:
        token = request.headers['Token']
        if token in tokens:
            pass
        else:
            return make_response(jsonify({'error':'token not found'}), 400)
    else:
        return make_response(jsonify({'error':' no "Token" header found'}), 400)



secret_code = '''
def secret_function():
    print("test")
'''


secret = os.urandom(512)
tokens_amount = 0
tokens_g = token_gen(token_gen)
tokens = []
my_token = next(tokens_g)
tokens.append(my_token)
print(my_token)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11500)