#Solely coded by Denvil with ♥️

from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

# Randomly generated secret key
secret_key = 'GxW5Z8vW5w9VxW5Z8v'
app.config['SECRET_KEY'] = secret_key

@app.route('/submit', methods=['POST'])
def handle_submission():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # You can add your own logic here to handle the form submission
    # For example, you can save the data to a database or send an email

    return jsonify({'message': 'Form submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
