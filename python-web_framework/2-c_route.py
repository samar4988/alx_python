#!/usr/bin/python3
"""
Copy the previous task to a new script that
starts a Flask web application
"""

from flask import Flask

# create a flask web application instance
app = Flask(__name__)

# Route /
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL (/).
    """
    return "Hello HBNB!"

# Route /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the root URL (/hbnb).
    """
    return "HBNB"
@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Route handler for /c/<text>"""
    # Replace underscore with spaces in the text
    text = text.replace('_', ' ')
    return f"C {text}"

# Start the Flask application only when this script is run directly
if __name__ == '__main__':
    # Run the app on 0.0.0.0 (all available network interfaces) on port 5000
    app.run(host='0.0.0.0', port=5000)