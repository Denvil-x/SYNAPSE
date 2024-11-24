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

    # Save the message to a file
    with open('messages.txt', 'a') as file:
        file.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n")

    return jsonify({'message': 'Form submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
