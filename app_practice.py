#  Import the Flask dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'

# Run a Flask App
# 1. In Anaconda Powershell in the proper directory enter this command: set FLASK_APP=app.py
# 2. To run the Flask app type the following command in the command line and press Enter: flask run
# 3. Running this command returns a line that says "Running on" followed by an address. This is the localhost address and a port number.
# 4. Copy and paste the localhost address into a web browser. Generally, a localhost will look something like this, for context: localhost:5000