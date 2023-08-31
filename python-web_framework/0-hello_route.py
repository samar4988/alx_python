#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Route: /
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL (/).
    """
    return "Hello HBNB!"
# Start the Flask application only when this script is run directly
if __name__ == '__main__':
    # Run the app on 0.0.0.0 (all available network interfaces) on port 5000
    app.run(host='0.0.0.0', port=5000)