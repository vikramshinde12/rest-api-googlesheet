from flask import Flask
from app.api import api_sheet

app = Flask(__name__)

app.register_blueprint(api_sheet)

app.run(debug=True)