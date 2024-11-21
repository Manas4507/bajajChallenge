from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os

app = Flask(__name__)
CORS(app)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        return jsonify({"operation_code": 1}), 200

    if request.method == 'POST':
        data = request.json.get('data', [])
        file_b64 = request.json.get('file_b64', '')

        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_lowercase_alphabet = [max([x for x in alphabets if x.islower()], default='')]
        is_prime_found = any(is_prime(int(x)) for x in numbers)

        file_valid = False
        file_mime_type = ''
        file_size_kb = 0

        if file_b64:
            try:
                file_data = base64.b64decode(file_b64)
                file_size_kb = len(file_data) / 1024
                file_mime_type = 'application/octet-stream'  # Default MIME type
                file_valid = True
            except Exception as e:
                file_valid = False

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet,
            "is_prime_found": is_prime_found,
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        }

        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
