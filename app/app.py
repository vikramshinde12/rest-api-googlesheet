from flask import Flask
from api import api_sheet

app = Flask(__name__)

app.register_blueprint(api_sheet)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')